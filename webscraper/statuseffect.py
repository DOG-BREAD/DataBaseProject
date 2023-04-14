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
            if(z==3):
                a=tableData[z].find_all("a")
                if(len(a)>1):
                    for b in range(1,len(a)):
                        c=a[b].get_text()
                        c=c.strip()
                        c=c.replace('\n','')
                        conData = conData.replace('\r', '')
                        if(c==''):
                            continue
                        print(c)
                    continue

            conData = tableData[z].get_text("")
            conData = conData.replace('\n','')
            conData = conData.replace('\r', '')
            conData = conData.strip()
            if (conData == ''):
                continue
            print(conData)

