# Survivors (Gets added to Characters table and Playable_Characters table, Skills table)
# TODO: Scrape each Survivors webpage to grab required attributes for Skills
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 00:57:55 2023

@authors: Samuel Jacobs, Josh Priest
"""

from bs4 import BeautifulSoup
import requests
import base64
import re
import mysql.connector
import dotenv
import os

dotenv.load_dotenv()

# Create the mysql.connector cursor to access the DB
mydb = mysql.connector.connect(
    host= os.getenv("host"),
    user= os.getenv("user"),
    password= os.getenv("password"),
    database= os.getenv("database")
)
mycursor = mydb.cursor()


""" html text sends a get requiest to the url which would send back a status code , add the '.text' to get the page back in text format """
html_text = requests.get("https://riskofrain2.fandom.com/wiki/Survivors").text
soup = BeautifulSoup(html_text, "lxml")

tableBody = soup.find_all("tbody")
tableRow = tableBody[0].find_all("tr")
#print(tableRow[0])
for x in range(1, len(tableRow)):

    tableData = tableRow[x].find_all("td")
    characterName = tableData[0].find("a")['title']     # charactersName
    print(characterName)
    characterPicture = tableData[0].find("img")['data-src']     # Icon
    print(characterPicture)
    characterHealth = tableData[2].get_text()   # BaseHealth
    print(characterHealth)
    characterDamage = tableData[3].get_text()   # BaseDamage
    print(characterDamage)
    characterHealthRegen = tableData[4].get_text()  # Health_Regen
    print(characterHealthRegen)
    characterClass= tableData[5].get_text()  # Class
    print(characterClass)
    characterArmor = tableData[6].get_text()        # Armor
    print(characterArmor)
    characterMovementSpeed = tableData[7].get_text()    # MvmtSpeed
    print(characterMovementSpeed)
    characterMass = tableData[8].get_text()     # Mass is in Playable_Characters
    print(characterMass)

   
    # TODO: Scrape each Survivors webpage to fill in Skills table

    # Splits damages into BaseDamage & Dmg_Scalar i.e 12 (+2.4)     12 = baseDmb  2.4 = dmgScalar
    damages = characterDamage.replace(")", "").replace("+", "").replace("(", "")
    damages = damages.split()
    BaseDamage = damages[0]
    Dmg_Scalar = damages[1]

    # Splits health into BaseHealth and Health_Scalar
    health = characterHealth.replace(")", "").replace("+", "").replace("(", "")
    health = health.split()
    BaseHealth = health[0]
    Health_Scalar = health[1]

    # Splits HealthRegen into Health_Regen 
    healthRegen = characterHealthRegen.replace("/s", "").replace(")", "").replace("+", "").replace("(", "")
    healthRegen = healthRegen.split()
    Health_Regen = healthRegen[0]

    # remove units from MvmtSpeed
    MvmtSpeed = characterMovementSpeed.split()
    MvmtSpeed = MvmtSpeed[0]
    Level = 0
    
    # insert into Playable_Characters table & Characters table

    # attributes for playable_Characters: CharName, Mass, Dmg_Scalar, Health_Scalar, HealthRegen_Scalar
    sql = "INSERT INTO characters (Armor, BaseDamage, BaseHealth, charactersName, Level, Health_Regen, Class, Icon, MvmtSpeed ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (int(characterArmor), int(BaseDamage), int(BaseHealth), characterName, Level, float(Health_Regen), characterClass, characterPicture, float(MvmtSpeed))
    mycursor.execute(sql, val)
    
    # attributes for Characters: Armor, BaseDamage, BaseHealth, charactersName, Health_Regen, Class, Icon, MvmtSpeed
    sql2 = "INSERT INTO playable_characters (CharName, Mass, Dmg_Scalar, MvmtSpeed_scalar) VALUES (%s, %s, %s, %s)"
    val2 = (characterName, int(characterMass), float(Dmg_Scalar), float(MvmtSpeed))
    mycursor.execute(sql2, val2)
     
    
    # Scrape each Survivor's individual page to grab skills for the skills table
    # attributes for skills table: cName, sName, icon, Cooldown, Descr, skillType, proc_coefficient
    url = "https://riskofrain2.fandom.com/wiki/" + characterName

    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, "lxml")


    divs = soup.find_all('div', {'class':'skillbox'})
    for div in divs:
        tables = div.find_all('table', {'class':'article-table skill'})
        for y in tables:
            sName = y.find('span', {'class':'mw-headline'}).text
            icon = y.find('th', {'class':'skillimage'}).a['href'] 
            
            tableRows = y.find_all('tr')
            # -2 because we don't care about the last two rows (Notes)
            # initalize Cooldown & ProcCoef since not every skill has one
            for j in range(2, len(tableRows)-2):
                Cooldown = "0"
                ProcCoef = "0"
                descr = ""
                val = tableRows[j].th.text

                if val == "Type\n":
                    Type = tableRows[j].td.text
                elif val == "Description\n":
                    descr = tableRows[j].td.text
                    #print("descr = ", descr)
                elif val == "Cooldown\n":
                    Cooldown = tableRows[j].td.text.replace("s","").strip()

                else:
                    ProcCoef = tableRows[j].td.text
            # attributes for skills table: cName, sName, icon, Cooldown, Descr, skillType, proc_coefficient
            sql3 = "INSERT INTO skills (cName, sName, icon, Cooldown, Description, Type, proc_coefficient) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val3 = (characterName, sName, icon, float(Cooldown), descr, Type, float(ProcCoef))
            mycursor.execute(sql3, val3)


    
    mydb.commit()



mycursor.close() 
mydb.close()