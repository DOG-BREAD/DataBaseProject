# @author Josh Priest
# Popluate the relationships tables

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

sql = "INSERT INTO spawns (Env, Items) SELECT environment.envName, items.IName FROM environment JOIN items"    
mycursor.execute(sql)

sql = "INSERT INTO generates (Unplayable_char, EnvName) SELECT unplayable_characters.charactersName, environment.EnvName FROM unplayable_characters JOIN environment;"    
mycursor.execute(sql)

sql = "INSERT INTO gives (Env, Items) SELECT items.IName, status_effects.Internal_name FROM items JOIN status_effects;"
mycursor.execute(sql)

mydb.commit()
mycursor.close()
mydb.close()