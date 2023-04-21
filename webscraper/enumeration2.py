import mysql.connector
import dotenv
import os

dotenv.load_dotenv()

# Create the mysql.connector cursor to access the DB
mydb = mysql.connector.connect(
    host=os.getenv("host"),
    user=os.getenv("user"),
    password=os.getenv("password"),
    database=os.getenv("database")
)
mycursor = mydb.cursor()

sql = "SELECT CharName FROM playable_characters"
# val = (int(characterArmor), int(BaseDamage), int(BaseHealth), characterName, Level, float(Health_Regen), characterClass, characterPicture, float(MvmtSpeed))
mycursor.execute(sql)

listofnames = []
for (NAME) in mycursor:
    listofnames += NAME

sql = "SELECT charactersName FROM drone"
# val = (int(characterArmor), int(BaseDamage), int(BaseHealth), characterName, Level, float(Health_Regen), characterClass, characterPicture, float(MvmtSpeed))
mycursor.execute(sql)

listofnames = []
for (NAME) in mycursor:
    listofnames += NAME

# insert into DB
# attributes for Characters: Armor, BaseDamage, BaseHealth, charactersName, Health_Regen, Class, Icon, MvmtSpeed
sql = "SELECT * FROM characters"
# val = (int(characterArmor), int(BaseDamage), int(BaseHealth), characterName, Level, float(Health_Regen), characterClass, characterPicture, float(MvmtSpeed))
mycursor.execute(sql)
result = mycursor.fetchall()
# fetch all values from the cursor

elite = ['Blazing ', 'Glacial ', 'Overloading ', 'Malachite ', 'Celestine ', 'Perfected ', 'Mending ', 'Voidtouched ']
for (Armor, BaseDamage, BaseHealth, charactersName, Level, Health_Regen, Class, Icon, MvmtSpeed) in result:
    if (charactersName in listofnames):
        continue


    else:

        for eliteType in elite:



print("Success!")
mydb.commit()
mycursor.close()
mydb.close()