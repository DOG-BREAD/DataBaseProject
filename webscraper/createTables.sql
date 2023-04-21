CREATE TABLE Characters(
	Armor INT,
	BaseDamage DOUBLE,
	BaseHealth INT,
	charactersName VARCHAR(80),
	Level INT,
	Health_Regen DOUBLE,
	Class VARCHAR(80),
	Icon LONGBLOB,
	MvmtSpeed DOUBLE,
	PRIMARY KEY(charactersName)
);



CREATE TABLE Playable_Characters (
	CharName VARCHAR(80),
	Mass INT,
	Outfit_color LONGBLOB,
	Dmg_Scalar DOUBLE,
	MvmtSpeed_Scalar DOUBLE,
	FOREIGN KEY (CharName) REFERENCES Characters(charactersName)
);


CREATE TABLE Skills(
	cName varchar(80),
	sName varChar(80),
	icon LONGBLOB,
	Cooldown TEXT,
	Description TEXT,
	Type varchar(80),
	proc_coefficient TEXT,
	FOREIGN KEY (cNAME) REFERENCES Playable_Characters(charName),
	PRIMARY KEY (sName)
);

CREATE TABLE Unplayable_Characters(
	Constant_Speed DOUBLE,		
	AI_Controlled VARCHAR(80),	
	Additional_Damage DOUBLE,	
	AI_Blacklist VARCHAR(80),	
	charactersName VARCHAR(80),	
	FOREIGN KEY (charName) REFERENCES Characters(charactersName) 
);

create table Environment(
	EnvName varchar(80),
    Stage varchar(80),
    Soundtrack TEXT,
    Description TEXT,
    Lunar_Seer_Quotes varchar(80),
    primary key(EnvName)
);


CREATE TABLE Status_Effects (
	Internal_name VARCHAR(80),
	PRIMARY KEY (Internal_name),
	Source TEXT,
	Description TEXT,
	Icon LONGBLOB,
	Effect VARCHAR(80),
	CharName VARCHAR(80),
	FOREIGN KEY (CharName) REFERENCES Characters(charactersName)
);

CREATE TABLE Affix_Buffs(
	Internal_name varchar(80),
	Power_of_elite varchar(80),
	PRIMARY KEY(Internal_name),
    FOREIGN KEY(internal_name) REFERENCES Status_Effects(internal_name)
);

CREATE TABLE Buffs(
	internal_name VARCHAR(80),
	helps_character VARCHAR(80),
	PRIMARY KEY(internal_name),
	FOREIGN KEY(internal_name) REFERENCES Status_Effects(internal_name)
);


CREATE TABLE Debuffs(
	internal_name VARCHAR(80),
	helps_enemy VARCHAR(80), 
	PRIMARY KEY (internal_name),
	FOREIGN KEY(internal_name) REFERENCES Status_Effects(internal_name)
);

CREATE TABLE Status (
	Current_character_status VARCHAR(80),
	Status_Name VARCHAR(80),
	FOREIGN KEY (Status_Name) REFERENCES Status_Effects(internal_name)
);

CREATE TABLE Cooldown_Buffs(
	internal_name VARCHAR(80),
	has_cool_down INT,
	PRIMARY KEY (internal_name),
	FOREIGN KEY (internal_name) REFERENCES Status_Effects(internal_name)
);

CREATE TABLE Items (
	Description TEXT,
	Rarity varchar(80),
	Color varchar(80),
	Icon LONGBLOB,
	IName varchar(80),
	charName varchar(80),
	PRIMARY KEY (IName),
	FOREIGN KEY (charName) REFERENCES Characters(charactersName)
);


CREATE TABLE Active(
	IName varchar(80),
	Cooldown TEXT,
	PRIMARY KEY (IName),
    FOREIGN KEY (IName) REFERENCES Items(IName)
);


CREATE TABLE Passive(
	Stack varchar(80),
	IName varchar(80),
	PRIMARY KEY (IName),
    FOREIGN KEY (IName) REFERENCES Items(IName)
);


CREATE TABLE Drone(
	abilities VARCHAR(80),
	cost INT,
	charactersName VARCHAR(80),
	charName varchar(80),
	PRIMARY KEY(charactersName),
	FOREIGN KEY(charactersName) REFERENCES Unplayable_Characters(charName),
	FOREIGN KEY(charName) REFERENCES Playable_Characters(CharName)
);

CREATE TABLE AIBlacklist(
	charactersName varchar(200),
	AIBlackList varchar(80),
	PRIMARY KEY(charactersName, AIBlackList),
	FOREIGN KEY (charactersName) REFERENCES unplayable_characters(charName)
);

CREATE TABLE gives(
	iname varchar(200),
	status_effect_name varchar(80),
	PRIMARY KEY(iname, status_effect_name),
	FOREIGN KEY (iname) REFERENCES items(IName),
	FOREIGN KEY (status_effect_name) REFERENCES status_effects(Internal_name)
);