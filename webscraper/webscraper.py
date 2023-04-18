# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 00:57:55 2023

@author: Samuel Jacobs & Josh Priest
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
html_text = requests.get("https://riskofrain2.fandom.com/wiki/Items").text
soup = BeautifulSoup(html_text, "lxml")

#collect the anchor tags from each of the items
counter =0

tableBody = soup.find_all("tbody")
for eachTableBody in range(1, len(tableBody)-1):

    tableRow = tableBody[eachTableBody].find_all("tr")
    if(eachTableBody > 6 ):
        print("--------------------------------------" + " active ")
        for eachRow in range(1, len(tableRow)):
            tableData = tableRow[eachRow].find_all("td")
            itemName = tableData[0]['data-sort-value']
            print("Name = ", itemName)  # prints name atm

            url = "https://riskofrain2.fandom.com/wiki/"
            urlLink = itemName.replace(" ", "_")
            url += urlLink
            print("url = ", url)

            
            # Scrape each page for rarity 
            html = requests.get(url).text
            innerSoup = BeautifulSoup(html, "lxml")
            table = innerSoup.find('table', {'class':'infoboxtable'})
            Rarity = table.find("a", {'title':'Items'}).text.strip()

            # Set color
            if Rarity == "Common":
                Color = "White"
            elif Rarity == "Uncommon":
                Color == "Green"
            elif Rarity == "Legendary":
                Color = "Red"
            elif Rarity.startswith("Boss"):
                Color = "Yellow"
            elif Rarity == "Lunar":
                Color = "Blue"
            elif Rarity == "Void":
                Color = "Purple"
            elif Rarity == "Equipment":
                Color = "Orange"

            print("Rarity = ", Rarity)
            print("Color = ", Color)
            

            tableRowImageName = tableData[0].find("img")['alt']
            tableRowImageSource = tableData[0].find("img")['data-src']
            print(tableRowImageName)
            print("Icon = ", tableRowImageSource)
            itemDescription = re.sub(r'\n', '', tableData[1].get_text())  # returns all the human readable text
            print("Description = ", itemDescription)
            itemStack = re.sub(r'\n', '', tableData[2].get_text())
            print("cooldown = ", itemStack)
            counter += 1
            print("\n\n\n")

            # add active sql connector here
            # insert into items table then active table 
            sql = "INSERT INTO items(Description, Rarity, Color, Icon, IName, charName) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (itemDescription, Rarity, Color, tableRowImageSource, itemName, "Acrid")
            mycursor.execute(sql, val)

            sql2 = "INSERT INTO active(IName, Cooldown) VALUES (%s, %s)"
            val2 = (itemName, itemStack)
            mycursor.execute(sql2, val2)

        continue
    else:  
        for eachRow in range(1,len(tableRow)):
            tableData= tableRow[eachRow].find_all("td")
            itemName = tableData[0]['data-sort-value']
            print("Name = ", itemName) #prints name atm

            url = "https://riskofrain2.fandom.com/wiki/"
            urlLink = itemName.replace(" ", "_")
            url += urlLink
            print("url = ", url)


            # Scrape each page for rarity 
            html2 = requests.get(url).text
            innerSoup = BeautifulSoup(html2, "lxml")
            table = innerSoup.find('table', {'class':'infoboxtable'})
            Rarity = table.find("a", {'title':'Items'}).text.strip()

            # Set color
            if Rarity == "Common":
                Color = "White"
            elif Rarity == "Uncommon":
                Color == "Green"
            elif Rarity == "Legendary":
                Color = "Red"
            elif Rarity.startswith("Boss"):
                Color = "Yellow"
            elif Rarity == "Lunar":
                Color = "Blue"
            elif Rarity == "Void":
                Color = "Purple"
            elif Rarity == "Equipment":
                Color = "Orange"
            
            print("Rarity = ", Rarity)
            print("Color = ", Color)

            tableRowImageName = tableData[0].find("img")['alt']
            tableRowImageSource = tableData[0].find("img")['data-src']
            print(tableRowImageName)
            print("Icon = ", tableRowImageSource)
            itemDescription = re.sub(r'\n','',tableData[1].get_text()) #returns all the human readable text
            print("Description = ", itemDescription)
            itemStack = re.sub(r'\n','',tableData[2].get_text())
            print("Stack = ", itemStack)
            counter+=1
            print("\n\n\n")

            #add passive sql connector here
            #add to items and then passive table
            sql = "INSERT INTO items(Description, Rarity, Color, Icon, IName, charName) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (itemDescription, Rarity, Color, tableRowImageSource, itemName, "Acrid")
            mycursor.execute(sql, val)

            sql2 = "INSERT INTO passive(IName, Stack) VALUES (%s, %s)"
            val2 = (itemName, itemStack)
            mycursor.execute(sql2, val2)

    print(counter)

print("Success")        
mydb.commit()
mycursor.close() 
mydb.close()