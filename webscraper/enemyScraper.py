# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 00:57:55 2023

@author: Samuel Jacobs & Josh Priest
"""

from bs4 import BeautifulSoup
import requests
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
html_text = requests.get("https://riskofrain2.fandom.com/wiki/Monsters").text
soup = BeautifulSoup(html_text, "lxml")
tbody = soup.find("tbody")
rows = tbody.find_all("tr")
Level = 1

for data in rows[1:]:
    x = data.find_all("td")
    characterName = x[1].span.a.text.strip()
    if len(characterName) < 1:
        characterName = x[1].find_all('span', {'class':'tooltip'})
        characterName = characterName[1].span.text.strip()
    print("Characters Name = ",characterName)
    print("\n")
    icon = x[1].find("img")['data-src']
    Health = x[2].text
    Damage = x[3].text
    HealthRegen = x[4].text
    Armor = x[5].text
    MovementSpeed = x[6].text
    Class = x[7].text
    Type = x[8].text

    # split Health to get BaseHealth
    Health = Health.split()
    BaseHealth = Health[0]

    # split Damage to get BaseDamage & Additional_Damage (unplayable_characters)
    Damage = Damage.split()
    BaseDamage = Damage[0]
    Additional_Damage = Damage[1].replace("(+", "").replace(")", "")

    # split HealthRegen to grab first value
    HealthRegen = HealthRegen.split()
    Health_Regen = HealthRegen[0].replace("/s", "")

    # clean MovementSpeed for DB
    MovementSpeed = MovementSpeed.split()
    MvmtSpeed = MovementSpeed[0]

    #insert into DB
    # attributes for Characters: Armor, BaseDamage, BaseHealth, charactersName, Health_Regen, Class, Icon, MvmtSpeed
    sql = "INSERT INTO characters (Armor, BaseDamage, BaseHealth, charactersName, Level, Health_Regen, Class, Icon, MvmtSpeed ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (int(Armor), float(BaseDamage), int(BaseHealth), characterName, Level, float(Health_Regen), Class, icon, float(MvmtSpeed))
    mycursor.execute(sql, val)

    # attributes for unplayable_characters: Constant_Speed, AI_Controlled, Additional_Damage, AI_Blacklist (leave null for manual input), charactersName
    sql2 = "INSERT INTO unplayable_characters (Constant_Speed, AI_Controlled, Additional_Damage, charactersName) VALUES (%s, %s, %s, %s)"
    val2 = (float(MvmtSpeed), Class, float(Additional_Damage), characterName)
    mycursor.execute(sql2, val2)

print("Success!")
mydb.commit()
mycursor.close() 
mydb.close()