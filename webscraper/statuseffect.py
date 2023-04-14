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
html_text = requests.get("https://riskofrain2.fandom.com/wiki/Status_Effects").text
soup = BeautifulSoup(html_text, "lxml")

tableBody = soup.find_all("tbody")


for x in range (0, len(tableBody)-1):
    tableRow = tableBody[x].find_all("tr")

    for y in range(0, len(tableRow)):
        tableData =tableRow[y].find_all("td")

        for z in range(0,len(tableData)):
            conData = tableData[z].get_text()
            print(conData)

