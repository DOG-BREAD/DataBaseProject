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
html_text = requests.get("https://riskofrain2.fandom.com/wiki/Artifacts").text
soup = BeautifulSoup(html_text, "lxml")

tableBody = soup.find_all("tbody")
tableRow = tableBody[1].find_all("tr")
#print(tableRow[0])
for x in range(1, len(tableRow)):

    tableData = tableRow[x].find_all("td")
    artifactName = tableData[0].get_text()
    print(artifactName)
    artifactDescription = tableData[1].get_text()
    print(artifactDescription)
    artifactCode = tableData[2].get_text()
    print(artifactCode)
#print(tableBody[0])
