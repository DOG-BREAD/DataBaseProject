# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 00:57:55 2023

@author: Samuel Jacobs
"""

from bs4 import BeautifulSoup
import requests
import base64
import re



""" html text sends a get requiest to the url which would send back a status code , add the '.text' to get the page back in text format """
html_text = requests.get("https://riskofrain2.fandom.com/wiki/Monsters").text
soup = BeautifulSoup(html_text, "lxml")

tableBody = soup.find_all("tbody")
tableRow = tableBody[0].find_all("tr")
#print(tableRow[0])
for x in range(1, len(tableRow)):

    tableData = tableRow[x].find_all("td")
    characterName = tableData[0].find("a")['title']
    print(characterName)
    characterPicture = tableData[0].find("img")['data-src']
    print(characterPicture)
    characterHealth = tableData[2].get_text()
    print(characterHealth)
    characterDamage = tableData[3].get_text()
    print(characterDamage)
    characterHealthRegen = tableData[4].get_text()
    print(characterHealthRegen)
    characterClass= tableData[5].get_text()
    print(characterClass)
    characterArmor = tableData[6].get_text()
    print(characterArmor)
    characterMovementSpeed = tableData[7].get_text()
    print(characterMovementSpeed)
    characterMass = tableData[8].get_text()
    print(characterMass)
#print(tableBody[0])
