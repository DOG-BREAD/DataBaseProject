# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 00:57:55 2023

@author: Samuel Jacobs
"""

from bs4 import BeautifulSoup
import requests
import base64
import re



""" html text sends a get requiest to the url which would send back a status code , add the '.text' to get the page back in text format """
html_text = requests.get("https://riskofrain2.fandom.com/wiki/Items").text
soup = BeautifulSoup(html_text, "lxml")

#collect the anchor tags from each of the items
counter =0

tableBody = soup.find_all("tbody")
for eachTableBody in range(1, len(tableBody)-1):

    tableRow = tableBody[eachTableBody].find_all("tr")

    for eachRow in range(1,len(tableRow)):
        tableData= tableRow[eachRow].find_all("td")
        itemName = tableData[0]['data-sort-value']
        print(itemName) #prints name atm
        tableRowImageName = tableData[0].find("img")['alt']
        tableRowImageSource = tableData[0].find("img")['data-src']
        print(tableRowImageName)
        print((tableRowImageSource))
        itemDescription = re.sub(r'\n','',tableData[1].get_text()) #returns all the human readable text
        print(itemDescription)
        itemStack = re.sub(r'\n','',tableData[2].get_text())
        print(itemStack)
        counter+=1


    print(counter)