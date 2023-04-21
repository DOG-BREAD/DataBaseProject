# authors: Samuel Jacobs, Josh Priest

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
html_text = requests.get("https://riskofrain2.fandom.com/wiki/Category:AIBlacklist_Items").text
soup = BeautifulSoup(html_text, "lxml")

aiBlacklistString=""
list = soup.find_all("ul")

sql = "select charactersName from unplayable_characters"
mycursor.execute(sql)
results = mycursor.fetchall()
names = [result[0] for result in results]
    
list_of_items = []
for x in range(10,24):
    a= list[x].find_all("li")

    for y in range (0, len(a)):
        d = a[y].get_text()
        list_of_items.append(d)

for name in names:
    for item in list_of_items:
        
        # insert pair into AiBlacklist table
        sql2 = "INSERT INTO AiBlacklist (charactersName, AIBlacklist) VALUES (%s, %s)"
        val2 = (name, item)
        mycursor.execute(sql2, val2)
        print(f"(name, pair) ", name, item)


mydb.commit()
mycursor.close() 
mydb.close()