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

sql = "SELECT CharName FROM playable_characters"
#val = (int(characterArmor), int(BaseDamage), int(BaseHealth), characterName, Level, float(Health_Regen), characterClass, characterPicture, float(MvmtSpeed))
mycursor.execute(sql)

listofnames=[]
for(NAME) in mycursor:
    listofnames+= NAME

sql = "SELECT charactersName FROM drone"
#val = (int(characterArmor), int(BaseDamage), int(BaseHealth), characterName, Level, float(Health_Regen), characterClass, characterPicture, float(MvmtSpeed))
mycursor.execute(sql)

listofnames=[]
for(NAME) in mycursor:
    listofnames+= NAME

#insert into DB
# attributes for Characters: Armor, BaseDamage, BaseHealth, charactersName, Health_Regen, Class, Icon, MvmtSpeed
sql = "SELECT * FROM characters "
#val = (int(characterArmor), int(BaseDamage), int(BaseHealth), characterName, Level, float(Health_Regen), characterClass, characterPicture, float(MvmtSpeed))
mycursor.execute(sql)
result = mycursor.fetchall()
#fetch all values from the cursor

elite = ['Blazing ','Glacial ', 'Overloading ', 'Malachite ', 'Celestine ', 'Perfected ', 'Mending ', 'Voidtouched ']
for(Armor, BaseDamage, BaseHealth, charactersName, Level, Health_Regen, Class, Icon, MvmtSpeed) in result:
    if(charactersName in listofnames ):
        continue
    if(Armor== None):
        Armor=0
    else:
        othercharactersName = "Other " + charactersName
        sql = "INSERT INTO characters (Armor, BaseDamage, BaseHealth, charactersName, Level, Health_Regen, Class, Icon, MvmtSpeed ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (int(Armor), int(BaseDamage), int(BaseHealth), othercharactersName, 1, float(Health_Regen), Class, Icon,
               float(MvmtSpeed))
        mycursor.execute(sql, val)

        # attributes for unplayable_characters: Constant_Speed, AI_Controlled, Additional_Damage, AI_Blacklist (leave null for manual input), charactersName
        sql2 = "INSERT INTO unplayable_characters (Constant_Speed, AI_Controlled, Additional_Damage, charactersName) VALUES (%s, %s, %s, %s)"
        val2 = (float(MvmtSpeed), Class, float(0), othercharactersName)
        mycursor.execute(sql2, val2)

        # other
        sql = "INSERT INTO enemies (charactersName, Family, SB_Flag, MAP_SPAWN_REQUIREMENTS, SM_FLAG, special_spawn_requirements, OM_Flag, survivar_ally, E_flag, Effect, damage_boost, health_boost, Chance_to_drop_buff ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (othercharactersName, "", False, "", False, "", True, "survivar_ally", False, "", float(0), float(0), float(0))
        mycursor.execute(sql, val)
        for eliteType in elite:

            ElitecharactersName = eliteType + charactersName
            print(charactersName)
            sql = "INSERT INTO characters (Armor, BaseDamage, BaseHealth, charactersName, Level, Health_Regen, Class, Icon, MvmtSpeed ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (int(Armor), int(BaseDamage), int(BaseHealth), ElitecharactersName, Level, float(Health_Regen), Class, Icon, float(MvmtSpeed))
            mycursor.execute(sql, val)

            # attributes for unplayable_characters: Constant_Speed, AI_Controlled, Additional_Damage, AI_Blacklist (leave null for manual input), charactersName
            sql2 = "INSERT INTO unplayable_characters (Constant_Speed, AI_Controlled, Additional_Damage, charactersName) VALUES (%s, %s, %s, %s)"
            val2 = (float(MvmtSpeed), Class, float(0), ElitecharactersName)
            mycursor.execute(sql2, val2)


            # elite
            sql = "INSERT INTO enemies (charactersName, Family, SB_Flag, MAP_SPAWN_REQUIREMENTS, SM_FLAG, special_spawn_requirements, OM_Flag, survivar_ally, E_flag, Effect, damage_boost, health_boost, Chance_to_drop_buff ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (
            ElitecharactersName, "", False, "", False, "", False, "survivar_ally", True, str(eliteType), float(0),
            float(0), float(0))
            mycursor.execute(sql, val)

            EliteOthercharactersName = "Other " + eliteType + charactersName
            sql = "INSERT INTO characters (Armor, BaseDamage, BaseHealth, charactersName, Level, Health_Regen, Class, Icon, MvmtSpeed ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (int(Armor), int(BaseDamage), int(BaseHealth), EliteOthercharactersName, Level, float(Health_Regen), Class, Icon,
               float(MvmtSpeed))
            mycursor.execute(sql, val)

            # attributes for unplayable_characters: Constant_Speed, AI_Controlled, Additional_Damage, AI_Blacklist (leave null for manual input), charactersName
            sql2 = "INSERT INTO unplayable_characters (Constant_Speed, AI_Controlled, Additional_Damage, charactersName) VALUES (%s, %s, %s, %s)"
            val2 = (float(MvmtSpeed), Class, float(0), EliteOthercharactersName)
            mycursor.execute(sql2, val2)

            # other
            sql = "INSERT INTO enemies (charactersName, Family, SB_Flag, MAP_SPAWN_REQUIREMENTS, SM_FLAG, special_spawn_requirements, OM_Flag, survivar_ally, E_flag, Effect, damage_boost, health_boost, Chance_to_drop_buff ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (
                EliteOthercharactersName, "", False, "", False, "", True, "survivar_ally", True, str(eliteType), float(0),
                float(0), float(0))
            mycursor.execute(sql, val)

print("Success!")
mydb.commit()
mycursor.close()
mydb.close()