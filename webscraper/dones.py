from bs4 import BeautifulSoup
import requests
import base64
import re



""" html text sends a get requiest to the url which would send back a status code , add the '.text' to get the page back in text format """

drones = ["https://riskofrain2.fandom.com/wiki/Emergency_Drone" , "https://riskofrain2.fandom.com/wiki/Equipment_Drone" ,"https://riskofrain2.fandom.com/wiki/Gunner_Drone"
          ,"https://riskofrain2.fandom.com/wiki/Gunner_Turret","https://riskofrain2.fandom.com/wiki/Healing_Drone" ,"https://riskofrain2.fandom.com/wiki/Incinerator_Drone",
          "https://riskofrain2.fandom.com/wiki/Missile_Drone", "https://riskofrain2.fandom.com/wiki/Squid_Polyp",  "https://riskofrain2.fandom.com/wiki/TC-280_Prototype",
          "https://riskofrain2.fandom.com/wiki/The_Back-up"]
for x in range (0, len(drones)):
    html_text = requests.get(drones[x]).text

    soup = BeautifulSoup(html_text, "lxml")

    tableBody = soup.find_all("tbody")
    nam = tableBody[0].find_all("th")
    print(nam[0].get_text())
    tableRow = tableBody[0].find_all("td")

    #for x in range(2, len(tableRow), 2):
     #   print(tableRow[x].get_text())

    #health
    print(tableRow[2].get_text())
    #health regen
    print(tableRow[4].get_text())
    #move
    print(tableRow[6].get_text())
    #speed
    print(tableRow[8].get_text())
    #armor
    print(tableRow[10].get_text())
