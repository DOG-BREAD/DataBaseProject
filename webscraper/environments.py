# Python script that scrapes the Environment page from risk of rain 2 wiki
# @authors: Akito Minosoko, Josh Priest
# @date 4/18/2023

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

html_text = requests.get("https://riskofrain2.fandom.com/wiki/Environments").text
soup = BeautifulSoup(html_text, "lxml")

stageSection = soup.find_all("h2")

for x in range (1, 8):
    #Stage Name = the actual list that stores the name of the sages
    stageName = stageSection[x].get_text()
    if(stageName[len(stageName)-1] == 's'):
        stageName = stageName[:-1]
    galleryBoxSection = stageSection[x].find_next("ul", attrs={"class":"gallery mw-gallery-traditional fix"})
    galleryBoxes = galleryBoxSection.find_all("li", attrs={"class":"gallerybox"})

    for galleryBox in galleryBoxes:
        envName = galleryBox.find_next("span", attrs={"style":"white-space: nowrap;"})
        envURL = "https://riskofrain2.fandom.com/wiki/" + envName.get_text()[2:].replace(" ", "_")
        

        html_text = requests.get(envURL).text
        soup = BeautifulSoup(html_text, "lxml")

        table = soup.find("table", attrs={"class":"infoboxtable"})
        tr = table.find_all("tr")
        

        
        if (len(tr) == 11):
            print(envName.get_text()[2:])   #EnvName
            Name = envName.get_text()[2:]
            print(stageName)                #stage

            #Sound Track
            soundTrack = tr[4].find_all("td")
            print(soundTrack[1].get_text().strip())     # Soundtrack
            soundTrack = soundTrack[1].get_text().strip()

            #Description
            #There was unnecessary traversal into nondisplaying text and used replace method to clean up
            print(tr[10].find("td").get_text().strip().replace("MithrixKing of NothingHP: 1000 (+300 per level)Damage: 16 (+3.2 per level)Class: Melee / RangedSpeed: 15 m/sArmor: 20", "").replace("   ", " "))        #Description
            Description = tr[10].find("td").get_text().strip().replace("MithrixKing of NothingHP: 1000 (+300 per level)Damage: 16 (+3.2 per level)Class: Melee / RangedSpeed: 15 m/sArmor: 20", "").replace("   ", " ")

            #Lunar Seer Quote
            print(tr[7].find("td").get_text().strip(), "\n")    # Lunar_Seer_Quotes
            Lunar_Seer_Quotes = tr[7].find("td").get_text().strip()
            

        elif(len(tr) == 8):
            print(envName.get_text()[2:])       # EnvName
            Name = envName.get_text()[2:]
            print(stageName)                    # Stage

            #Sound Track
            soundTrack = tr[4].find_all("td")
            print(soundTrack[1].get_text().strip())     # Soundtrack
            soundTrack = soundTrack[1].get_text().strip()

            #Lunar Seer Quote (with no description)
            if(tr[6].find("td").get_text().strip() == "Lunar Seer Quote"):
                print("N/A")    #Description
                print(tr[7].find("td").get_text().strip(), "\n")        #Lunar_Seer_Quote
                Description = "N/A"
                Lunar_Seer_Quotes = tr[7].find("td").get_text().strip()

            #Description (with no lunar seer quote)
            else:
                print(tr[7].find("td").get_text().strip().replace("MithrixKing of NothingHP: 1000 (+300 per level)Damage: 16 (+3.2 per level)Class: Melee / RangedSpeed: 15 m/sArmor: 20","").replace("   ", " "))      # Description
                print("N/A", "\n") #Lunar_Seer_Quotes
                Description = tr[7].find("td").get_text().strip().replace("MithrixKing of NothingHP: 1000 (+300 per level)Damage: 16 (+3.2 per level)Class: Melee / RangedSpeed: 15 m/sArmor: 20","").replace("   ", " ")
                Lunar_Seer_Quotes = "N/A"


        #print("Name = ", Name)
        #print("Stage = ", stageName)
        #print("Soundtrack = ", soundTrack)
        #print("Description = ", Description)
        #print("Lunar_Seer_Quotes = ", Lunar_Seer_Quotes)
        # attributes for Environment: EnvName, Stage, Soundtrack, Description, Lunar_Seer_Quotes
        sql = "INSERT INTO environment (EnvName, Stage, Soundtrack, Description, Lunar_Seer_Quotes) VALUES (%s, %s, %s, %s, %s)"
        val = (Name, stageName, soundTrack, Description, Lunar_Seer_Quotes)
        mycursor.execute(sql, val)

    

mydb.commit()
mycursor.close() 
mydb.close()
#No desc but yes lunar seer quote: 
#-aphelian sanctuary (stage 2, 3rd)
#-Siren's Call (stage 4, 2nd)
#-Fifth stage
