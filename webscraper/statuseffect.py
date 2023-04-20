# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 00:57:55 2023

@author: Samuel Jacobs & Josh Priest
"""

from bs4 import BeautifulSoup
import requests
import base64
import re
import dotenv
import os
import mysql.connector

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
html_text = requests.get("https://riskofrain2.fandom.com/wiki/Status_Effects").text
soup = BeautifulSoup(html_text, "lxml")


tables = soup.find_all('table', {'class':"article-table floatheader"})
# tables[0] = Affix Buffs
# tables[1] = Buffs
# tables[2] = Cooldown Buffs
# tables[3] = Debuffs
i = 0
for x in tables:    # for each table
    tbody = x.find("tbody")
    tableRows = tbody.find_all("tr")
    for y in tableRows[1:]:     # for each row in table x
        tableData = y.find_all("td")
        Icon = tableData[0].a['href']
        #name = tableData[1].text.strip()
        Description = tableData[2].text.strip()
        listOfSources = []
        sources = tableData[3].find_all("li")

        for z in sources:
            name = z.find_all("a")
            if len(name) > 1:
                name = name[1].text.strip()
            elif len(name) == 1:
                name = z.a.text.strip()
            else:
                name = z.text
            
            if len(name) > 0:
                listOfSources.append(name)


        

        Internal_name = tableData[4].text.strip()
        print("Internal name = ", Internal_name)

        # convert listOfSources to one string
        Source = ""
        seperator = ", "
        Source = seperator.join(listOfSources)
        print("Source = ", Source)

        # insert into Status_Effects table & then each coreelating table - Note Inserting in Acrid as Default value
        sql = "INSERT INTO status_effects (Internal_name, Source, Description, Icon, Effect, CharName) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (Internal_name, Source, Description, Icon, "0%", "Acrid")
        mycursor.execute(sql, val)

        print("i = ", i)

        #Affix buffs
        if i == 0:
            sql2 = "INSERT INTO affix_buffs (Internal_name, power_of_elite) VALUES (%s, %s)"
            val2 = (Internal_name, "")
            mycursor.execute(sql2, val2)
        #Buffs
        elif i == 1:
            sql2 = "INSERT INTO buffs (Internal_name, helps_character) VALUES (%s, %s)"
            val2 = (Internal_name, 0)
            mycursor.execute(sql2, val2)
        #Cooldown Buffs
        elif i == 2:
            sql2 = "INSERT INTO Cooldown_buffs (Internal_name, has_cool_down) VALUES (%s, %s)"
            val2 = (Internal_name, 0)
            mycursor.execute(sql2, val2)
        #Debuffs
        elif i == 3:
            sql2 = "INSERT INTO debuffs (Internal_name, helps_enemy) VALUES (%s, %s)"
            val2 = (Internal_name, "")
            mycursor.execute(sql2, val2)
    
    
    i += 1  

# Status table will be manualy populated
mydb.commit()
mycursor.close() 
mydb.close()