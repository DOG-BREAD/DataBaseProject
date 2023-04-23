'''
Author: Akito Minisoto
'''
import random
import string
import mysql.connector
import dotenv
import os

dotenv.load_dotenv()
mydb = mysql.connector.connect(
    host= os.getenv("host"),
    user= os.getenv("user"),
    password= os.getenv("password"),
    database= os.getenv("database")
)
mycursor = mydb.cursor()

def generateStatus(choices):
    while True:
        # Choose a random number of elements from the list (up to 3)
        numOfChoices = random.randint(1, 3)
        chosen = random.sample(choices, numOfChoices)
        # Concatenate the chosen elements
        theComb = ', '.join(chosen)
        # Ensure that the string is unique
        if theComb not in generateStatus.generatedStatus:
            generateStatus.generatedStatus.add(theComb)
            return theComb
        
generateStatus.generatedStatus = set()
elements = [ 'Blinded', 'Confused', 'Cursed', 'Dazed',
            'Deafened', 'Enraged', 'Exhausted', 'Fearful', 'Frozen',
            'Hypnotized', 'Immobilized', 'Invisible', 'Paralyzed',
            'Petrified', 'Silenced', 'Slowed', 'Stunned', 'Weakened',
            'Burned', 'Chilled', 'Electrified', 'Radiated', 'Suffocating',
            'Drained', 'Regenerating', 'Berserk', 'Charmed', 'Corroded',
            'Disarmed', 'Diseased', 'Entangled', 'Frenzied',
            'Glowing', 'Hasted', 'Haunted', 'Hexed', 'Infected', 'Maddened',
            'Magnetic', 'Molten', 'Necrotic', 'Pacified', 'Possessed', 'Protected',
            'Rejuvenated', 'Shocked', 'Sickened', 'Spectral', 'Trapped', 'Vampiric',
            'Venomous', 'Wounded']
current_character_statusChoices = ['Positive', 'Negative']
for x in range (1, 215):
    generated_string = generateStatus(elements)
    #print(generated_string, "\n")
    mycursor.execute("SELECT description FROM status_effects ORDER BY RAND() LIMIT 1")
    description = mycursor.fetchone()
    print(description)
    mycursor.execute("SELECT icon FROM status_effects ORDER BY RAND() LIMIT 1")
    icon = mycursor.fetchone()
    print(icon)
    mycursor.execute("SELECT source FROM status_effects ORDER BY RAND() LIMIT 1")
    source = mycursor.fetchone()
    print(source)
    mycursor.execute("SELECT charName FROM status_effects ORDER BY RAND() LIMIT 1")
    charName = mycursor.fetchone()
    print(charName)
    mycursor.execute("SELECT effect FROM status_effects ORDER BY RAND() LIMIT 1")
    effect = mycursor.fetchone()
    print(effect)


    sql = "INSERT INTO status_effects (internal_name, description, icon, source, charName, effect) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (generated_string, description[0], icon[0], source[0], charName[0], effect[0])
    mycursor.execute(sql, val)

    sql = "INSERT INTO status (status_name, current_character_status) VALUES (%s, %s)"
    current_character_status = random.choice(current_character_statusChoices)
    val = (generated_string, current_character_status)
    mycursor.execute(sql, val)


print("Success")
mydb.commit()
mycursor.close()
mydb.close()