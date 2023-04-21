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

sql = "SELECT CharName FROM playable_characters (NAME) VALUES (%s)"
#val = (int(characterArmor), int(BaseDamage), int(BaseHealth), characterName, Level, float(Health_Regen), characterClass, characterPicture, float(MvmtSpeed))
mycursor.execute(sql)

listofnames=[]
for(NAME) in mycursor:
    listofnames+= NAME

#insert into DB
# attributes for Characters: Armor, BaseDamage, BaseHealth, charactersName, Health_Regen, Class, Icon, MvmtSpeed
sql = "SELECT * FROM characters (Armor, BaseDamage, BaseHealth, charactersName, Level, Health_Regen, Class, Icon, MvmtSpeed ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
#val = (int(characterArmor), int(BaseDamage), int(BaseHealth), characterName, Level, float(Health_Regen), characterClass, characterPicture, float(MvmtSpeed))
mycursor.execute(sql)

elite = ['Blazing ','Glacial ', 'Overloading ', 'Malachite ', 'Celestine ', 'Perfected ', 'Mending ', 'Voidtouched ']
for(Armor, BaseDamage, BaseHealth, charactersName, Level, Health_Regen, Class, Icon, MvmtSpeed) in mycursor:
    if(charactersName in listofnames ):
        continue
    else:
        charactersName = "Other " + charactersName
        sql = "INSERT INTO characters (Armor, BaseDamage, BaseHealth, charactersName, Level, Health_Regen, Class, Icon, MvmtSpeed ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (int(Armor), int(BaseDamage), int(BaseHealth), charactersName, Level, float(Health_Regen), Class, Icon,
               float(MvmtSpeed))
        mycursor.execute(sql, val)

        for eliteType in elite:

            charactersName = eliteType + charactersName
            sql = "INSERT INTO characters (Armor, BaseDamage, BaseHealth, charactersName, Level, Health_Regen, Class, Icon, MvmtSpeed ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (int(Armor), int(BaseDamage), int(BaseHealth), charactersName, Level, float(Health_Regen), Class, Icon, float(MvmtSpeed))
            mycursor.execute(sql, val)

            charactersName = "Other " + eliteType + charactersName
            sql = "INSERT INTO characters (Armor, BaseDamage, BaseHealth, charactersName, Level, Health_Regen, Class, Icon, MvmtSpeed ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (int(Armor), int(BaseDamage), int(BaseHealth), charactersName, Level, float(Health_Regen), Class, Icon,
               float(MvmtSpeed))
            mycursor.execute(sql, val)



print("Success!")
mydb.commit()
mycursor.close()
mydb.close()