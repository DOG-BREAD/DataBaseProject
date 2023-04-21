# @date 4/18/2023
# @author:  Josh Priest, Samuel Jacobs

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


drones = ["https://riskofrain2.fandom.com/wiki/Emergency_Drone"  
          ,"https://riskofrain2.fandom.com/wiki/Equipment_Drone"
          ,"https://riskofrain2.fandom.com/wiki/Gunner_Drone"
          ,"https://riskofrain2.fandom.com/wiki/Gunner_Turret"
          ,"https://riskofrain2.fandom.com/wiki/Healing_Drone" 
          ,"https://riskofrain2.fandom.com/wiki/Incinerator_Drone"
          ,"https://riskofrain2.fandom.com/wiki/Missile_Drone"
          ,"https://riskofrain2.fandom.com/wiki/TC-280_Prototype"]
          
for x in range (0, len(drones)):
    html_text = requests.get(drones[x]).text

    soup = BeautifulSoup(html_text, "lxml")
    table = soup.find("table", {'class':'infoboxtable'})
    table_rows = table.find_all("tr")

    # always has Name, Icon, Health, Health_Regen
    # could have Heal/Damage, Speed, Armor, Base_Cost
    # Manually scrape remaining 4 drones 

    # Item_Name = table_rows[0], Icon = table_rows[1], Health = table_rows[2], Health_Regen = table_rows[3]
    #  Heal/Damage = table_rows[4], Speed = table_rows[5], Armor = table_rows[6], Base_Cost = table_rows[7] 
    item_name = table_rows[0].text.strip()
    
    icon = table_rows[1].a['href']
    
    health = table_rows[2].text.strip()
    health = health.replace("Health\n", "")

    health_regeneration = table_rows[3].text.strip()
    health_regeneration = health_regeneration.replace("Health Regen\n", "")


    damage = 0
    heal = 0
    speed = 0
    armor = 0
    base_cost = 0
    BaseDamage = 0

    for tr in table_rows[4:]:
        td = tr.find_all('td')
        row = [i.text for i in td]
        
        if row[0] == "Damage":
            damage = row[1]
            damage = damage.replace("\n", "")
            BaseDamage = damage.split(" ")[0]
        elif row[0] == "Heal":
            heal = row[1]
            heal = heal.replace("\n", "")
        elif row[0] == "Speed":
            speed = row[1]
            speed = speed.replace("\n", "")
            MovementSpeed = speed.split(" ")[0]
        elif row[0] == "Armor":
            armor = row[1]
            armor = armor.replace("\n", "")
        elif row[0] == "Base Cost":
            base_cost = row[1]
            base_cost = base_cost.replace("\n", "")
        
    print("name = ", item_name)
    print("icon = ", icon)
    print("health = ", health)
    print("health_regen = ", health_regeneration)
    print("damage = ", damage)
    print("heal = ", heal)
    print("speed = ", speed)
    print("armor = ", armor)
    print("base_cost = ", base_cost)
    print("\n")


    # TODO: parse health, health_regen, damage, heal, speed, base_cost to insert into DB
    # split health and grab first value for health and second for health_scalar
    health = health.split(" ")
    BaseHealth = health[0]
    Health_Scalar = health[1].replace("(+", "")


    # split health_regen and grab first value for health_regen and remove '/s' from first value
    health_regen = health_regeneration.split(" ")[0]
    health_regen = health_regen[0].replace("/s", "")

    # if base_cost is a 'str' and starts with '$' so remove it
    if isinstance(base_cost, str) and base_cost.startswith('$'):
        base_cost = base_cost.replace("$", "")

    # If MovementSpeed contains alphabet characters, set it to 0
    if MovementSpeed.isalpha():
        MovementSpeed = 0
    

    # 

    

    #insert into Drone table with charactersName == nam and charName "Acrid" as default. Will randomize playable characters names for charName
    #insert into characters --> unplayable_Characters --> Drone
    

    # attributes for Characters: Armor, BaseDamage, BaseHealth, charactersName, Health_Regen, Class, Icon, MvmtSpeed
    sql = "INSERT INTO Characters (Armor, BaseDamage, BaseHealth, charactersName, Level, Health_Regen, Class, Icon, MvmtSpeed ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (int(armor), float(BaseDamage), int(BaseHealth), item_name, 1, float(health_regen), "Drone", icon, float(MovementSpeed))
    mycursor.execute(sql, val)


    # attributes for Unplayable_Characters: charName, Constant_speed, AI_Controlled, AI_Blacklist
    sql2 = "INSERT INTO Unplayable_Characters (charactersName, Constant_speed, AI_Controlled) VALUES (%s, %s, %s)"
    val2 = (item_name, float(MovementSpeed), "Drone")
    mycursor.execute(sql2, val2)

    # attributes for Drone: abilities, cost, charactersName, charName
    
    #charName = playable characters name
    #charactersName = drone's name
    sql3 = "INSERT INTO Drone (cost, charactersName, charName) VALUES (%s, %s, %s)"
    val3 = (int(base_cost), item_name, "Acrid")
    mycursor.execute(sql3, val3)


    

mydb.commit()
mycursor.close()
mydb.close()