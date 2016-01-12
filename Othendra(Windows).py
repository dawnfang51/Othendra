#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import sys
import random
import os
import pickle
import time

cls = os.system('cls')


Weapons = {"Battleaxe" : 100,
		   "Wooden Staff" : 130,
		   "Dark Saber" : 700,
		   "Jade Staff" : 750,
		   "Sword of Dawn" : 1500,
		   "Holy Staff" : 1700,
		   "Demon Blade" : 3000,
		   "Phoenix Staff" : 3500,
		   "Death's Blade" : 6000,
		   "Staff of Fallen Ashes" : 7000,
		   "Excalibur" : 10000,
		   "Grandmaster Staff" : 15000,
		   "Rusty Sword" : 30
			}
			
Bows = {"Wooden Bow" : 100,
		"Steel Bow" : 700,
		"Lightning Bow" : 1500,
		"Bow of Hellfire" : 3000,
		"Phantom Bow" : 6000,
		"Dragon Bow" : 11000
		}

armH = {"Leather Helmet" : 50, "Worn Helmet" : 10, "Steal Helmet" : 100, "Plasma Helmet" : 200, "Demon Helmet" : 400, "Phantom Helmet" : 700, "Champion Helmet" : 1750,
	    "Mage Hood" : 50, "Worn Helmet" : 10, "Priest Hood" : 100, "Phoenix Hood" : 200, "Necromancer Hood" : 400, "Death's Hood" : 700, "Arch Mage Hood" : 1750}
armB = {"Leather Tunic" : 100, "Worn Shirt" : 20, "Steal Armor" : 200, "Plasma Armor" : 400, "Demon Armor" : 750, "Phantom Armor" : 2000, "Champion Armor" : 5000, 
		"Mage Robe" : 100, "Worn Shirt" : 20, "Priest Robe" : 200, "Phoenix Robe" : 400, "Necromancer Robe" : 750, "Death's Robe" : 2000, "Arch Mage Robe" : 5000}
armA = {"Leather Gauntlets" : 30, "Worn Gloves" : 6, "Steal Gauntlets" : 50, "Plasma Gauntlets" : 100, "Demon Gauntlets" : 225, "Phantom Gauntlets" : 300, "Champion Gauntlets" : 750,
		"Mage Gloves" : 30, "Worn Gloves" : 6, "Priest Gloves" : 50, "Phoenix Gloves" : 100, "Necromancer Gloves" : 225, "Death's Gloves" : 300, "Arch Mage Gloves" : 750}
armL = {"Leather Greaves" : 70, "Worn Pants" : 12, "Steal Greaves" : 100, "Plasma Greaves" : 200, "Demon Greaves" : 400, "Phantom Greaves" : 700, "Champion Greaves" : 1750,
		"Mage Pants" : 70, "Worn Pants" : 12, "Priest Pants" : 100, "Phoenix Pants" : 200, "Necromancer Pants" : 400, "Death's Greaves" : 700, "Arch Mage Pants" : 1750}
armF = {"Leather Boots" : 30, "Worn Boots" : 6, "Steal Boots" : 50, "Plasma Boots" : 100, "Demon boots" : 225, "Phantom Boots" : 300, "Champion Boots" : 750,
		"Mage Boots" : 30, "Worn Boots" : 6, "Priest Boots" : 50, "Phoenix Boots" : 100, "Necromancer boots" : 225, "Death's Boots" : 300, "Arch Mage Boots" : 750}

class Player:
	def __init__(self, name):
		self.name = name
		self.base_defe = 0
		self.base_mdefe = 0
		self.weap = "Rusty Sword"
		self.wbow = "None"
		self.armH = "Worn Helmet"
		self.armB = "Worn Shirt"
		self.armA = "Worn Gloves"
		self.armL = "Worn Pants"
		self.armF = "Worn Boots"
		self.gold = 200
		self.orichalcum = 0 
		self.base_stre = 1
		self.base_magi = 1
		self.base_rang = 1
		self.mana = self.maxmana
		self.level = 1
		self.exp = 0
		self.maxexp = 100
		self.expdiff = 50
		self.pots = 0
		self.arrows = 0
		self.q1c = False
		self.q2c = False
		self.q3c = False
		self.q1 = False
		self.q2 = False
		self.q3 = False
		self.q4c = False
		self.q5c = False
		self.q6c = False
		self.q4 = False
		self.q5 = False
		self.q6 = False
		self.q7c = False
		self.q8c = False
		self.q9c = False
		self.q7 = False
		self.q8 = False
		self.q9 = False
		self.q10c = False
		self.q11c = False
		self.q12c = False
		self.q10 = False
		self.q11 = False
		self.q12 = False
		self.q13c = False
		self.q14c = False
		self.q15c = False
		self.q13 = False
		self.q14 = False
		self.q15 = False
		self.q16c = False
		self.q17c = False
		self.q18c = False
		self.q16 = False
		self.q17 = False
		self.q18 = False
		self.q19c = False
		self.q19 = False
		self.qenemy = "None"
		self.qenemykillcount = 0
		self.kamount = 0
		self.reward = 0
		self.QuestActive = False
		self.qtitle = "None"
		self.health = self.maxhealth
		self.inventory = ["Rusty Sword", 
						  "Worn Shirt", 
						  "Worn Pants", 
						  "Worn Boots",
						  "Worn Helmet",
						  "Worn Gloves"]
		self.spells = []
		self.weaps = ["Rusty Sword"]
		self.bows = []
		self.armsH = ["Worn Helmet"]
		self.armsB = ["Worn Shirt"]
		self.armsL = ["Worn Pants"]
		self.armsA = ["Worn Gloves"]
		self.armsF = ["Worn Boots"]
					

# Weapon Buffs	
	@property
	def stre(self):
		stre = self.base_stre
		if self.weap == "Rusty Sword":
			stre += 10
		
		if self.weap == "Battleaxe":
			stre += 15
		
		if self.weap == "Wooden Staff":
			stre += 10
			
		if self.weap == "Dark Saber":
			stre += 25
				
		if self.weap == "Jade Staff":
			stre += 20
				
		if self.weap == "Sword of Dawn":
			stre += 40
		
		if self.weap == "Holy Staff":
			stre += 30
			
		if self.weap == "Demon Blade":
			stre += 60
		
		if self.weap == "Phoenix Staff":
			stre += 45
			
		if self.weap == "Death's Blade":
			stre += 80


		if self.weap == "Staff of Fallen Ashes":
			stre += 60
		
		if self.weap == "Excalibur":
			stre += 100
			
		if self.weap == "Grandmaster Staff":
			stre += 80
		return stre
	
#Magic Buffs
	@property
	def magi(self):
		magi = self.base_magi
		if self.weap == "Wooden Staff":
			magi += 15
		
		if self.weap == "Jade Staff":
			magi += 25
		
		if self.weap == "Holy Staff":
			magi += 40
		
		if self.weap == "Phoenix Staff":
			magi += 60
		
		if self.weap == "Staff of Fallen Ashes":
			magi += 80
		
		if self.weap == "Grandmaster Staff":
			magi += 100
		return magi

# Range Buff
	@property
	def rang(self):
		rang = self.base_rang
		if self.wbow == "Wooden Bow":
			rang += 20
			
		if self.wbow == "Steel Bow":
			rang += 30
		
		if self.wbow == "Lightning Bow":
			rang += 45
		
		if self.wbow == "Bow of Hellfire":
			rang += 70
		
		if self.wbow == "Phantom Bow":
			rang += 90
		
		if self.wbow == "Dragon Bow":
			rang += 120
		return rang

	
# Armor Buffs #		
	@property
	def defe(self):
		defe = self.base_defe
		## ARMOR BUFFS H ##
		if self.armH == "Worn Helmet":
			defe += 2 
		elif self.armH == "Leather Helmet":
			defe += 4
		elif self.armH == "Steel Helmet":
			defe += 7 
		elif self.armH == "Plasma Helmet":
			defe += 20 
		elif self.armH == "Demon Helmet":
			defe += 30 
		elif self.armH == "Phantom Helmet":
			defe += 40 
		elif self.armH == "Champion Helmet":
			defe += 50  
			
		elif self.armH == "Mage Hood":
			defe += 3
		elif self.armH == "Priest Hood":
			defe += 4 
		elif self.armH == "Phoenix Hood":
			defe += 10 
		elif self.armH == "Necromancer Hood":
			defe += 15 
		elif self.armH == "Death's Hood":
			defe += 20 
		elif self.armH == "Arch Mage Hood":
			defe += 25  
	## ARMOR BUFFS B
		if self.armB == "Worn Shirt":
			defe += 4 
		elif self.armB == "Leather Tunic":
			defe += 10
		elif self.armB == "Steel Armor":
			defe += 25
		elif self.armB == "Plasma Armor":
			defe += 40
		elif self.armB == "Demon Armor":
			defe += 60
		elif self.armB == "Phantom Armor":
			defe += 80
		elif self.armB == "Champion Armor":
			defe += 100
			
		elif self.armB == "Mage Robe":
			defe += 5
		elif self.armB == "Priest Robe":
			defe += 12 
		elif self.armB == "Phoenix Robe":
			defe += 20 
		elif self.armB == "Necromancer Robe":
			defe += 30 
		elif self.armB == "Death's Robe":
			defe += 40 
		elif self.armB == "Arch Mage Robe":
			defe += 50 
	## ARMOR BUFFS A
		if self.armA == "Worn Gloves":
			defe += 1 
		elif self.armA == "Leather Gauntlets":
			defe += 3 
		elif self.armA == "Steel Gauntlets":
			defe += 5 
		elif self.armA == "Plasma Gauntlets":
			defe += 10 
		elif self.armA == "Demon Gauntlets":
			defe += 15 
		elif self.armA == "Phantom Gauntlets":
			defe += 20 
		elif self.armA == "Champion Gauntlets":
			defe += 25 
		
		elif self.armA == "Mage Gloves":
			defe += 2
		elif self.armA == "Priest Gloves":
			defe += 3 
		elif self.armA == "Phoenix Gloves":
			defe += 5 
		elif self.armA == "Necromancer Gloves":
			defe += 8 
		elif self.armA == "Death's Gloves":
			defe += 10 
		elif self.armA == "Arch Mage Gloves":
			defe += 15 
			
		## ARMOR BUFFS L
		if self.armL == "Worn Pants":
			defe += 2
		elif self.armL == "Leather Greaves":
			defe += 5
		elif self.armL == "Steel Greaves":
			defe += 8
		elif self.armL == "Plasma Greaves":
			defe += 20
		elif self.armL == "Demon Greaves":
			defe += 30
		elif self.armL == "Phantom Greaves":
			defe += 40
		elif self.armL == "Champion Greaves":
			defe += 50
		
		elif self.armL == "Mage Pants":
			defe += 3
		elif self.armL == "Priest Pants":
			defe += 4 
		elif self.armL == "Phoenix Pants":
			defe += 10 
		elif self.armL == "Necromancer Pants":
			defe += 15 
		elif self.armL == "Death's Greaves":
			defe += 20 
		elif self.armL == "Arch Mage Pants":
			defe += 25 
			
		## ARMOR BUFFS F
		if self.armF == "Worn Boots":
			defe += 1
		elif self.armF == "Leather Boots":
			defe += 3
		elif self.armF == "Steel Boots":
			defe += 5
		elif self.armF == "Plasma Boots":
			defe += 10
		elif self.armF == "Demon Boots":
			defe += 15
		elif self.armF == "Phantom Boots":
			defe += 20
		elif self.armF == "Champion Boots":
			defe += 25
		
		elif self.armF == "Mage Boots":
			defe += 2
		elif self.armF == "Priest Boots":
			defe += 3 
		elif self.armF == "Phoenix Boots":
			defe += 5 
		elif self.armF == "Necromancer Boots":
			defe += 8 
		elif self.armF == "Death's Boots":
			defe += 10 
		elif self.armF == "Arch Mage Boots":
			defe += 15 
		return defe
	
	@property
	def mdefe(self):
		mdefe = self.base_mdefe
		
		#Armor Buffs H
		if self.armH == "Mage Hood":
			mdefe += 3
		elif self.armH == "Priest Hood":
			mdefe += 4 
		elif self.armH == "Phoenix Hood":
			mdefe += 10 
		elif self.armH == "Necromancer Hood":
			mdefe += 15 
		elif self.armH == "Death's Hood":
			mdefe += 20 
		elif self.armH == "Arch Mage Hood":
			mdefe += 25  
		#Armor Buffs B
		if self.armB == "Mage Robe":
			mdefe += 5
		elif self.armB == "Priest Robe":
			mdefe += 12 
		elif self.armB == "Phoenix Robe":
			mdefe += 20 
		elif self.armB == "Necromancer Robe":
			mdefe += 30 
		elif self.armB == "Death's Robe":
			mdefe += 40 
		elif self.armB == "Arch Mage Robe":
			mdefe += 50 
		#Armor Buffs A
		if self.armA == "Mage Gloves":
			mdefe += 2
		elif self.armA == "Priest Gloves":
			mdefe += 3 
		elif self.armA == "Phoenix Gloves":
			mdefe += 5 
		elif self.armA == "Necromancer Gloves":
			mdefe += 8 
		elif self.armA == "Death's Gloves":
			mdefe += 10 
		elif self.armA == "Arch Mage Gloves":
			mdefe += 15 
		#Armor Buffs L
		if self.armL == "Mage Pants":
			mdefe += 3
		elif self.armL == "Priest Pants":
			mdefe += 4 
		elif self.armL == "Phoenix Pants":
			mdefe += 10 
		elif self.armL == "Necromancer Pants":
			mdefe += 15 
		elif self.armL == "Death's Greaves":
			mdefe += 20 
		elif self.armL == "Arch Mage Pants":
			mdefe += 25 
		#Armor Buffs F
		if self.armF == "Mage Boots":
			mdefe += 2
		elif self.armF == "Priest Boots":
			mdefe += 3 
		elif self.armF == "Phoenix Boots":
			mdefe += 5 
		elif self.armF == "Necromancer Boots":
			mdefe += 8 
		elif self.armF == "Death's Boots":
			mdefe += 10 
		elif self.armF == "Arch Mage Boots":
			mdefe += 15 
		return mdefe
	
	@property
	def maxhealth(self):
		maxhealth = 100 + self.defe
		return maxhealth
	
	@property
	def maxmana(self):
		maxmana = 100 + self.mdefe 
		return maxmana

global Player_name

def name():
	os.system('cls')
	global Player_name
	Player_name = raw_input("What is your name? ")
	os.system('cls')
	print ("""In the Kingdom of Valkria there has been an
outbreak of monsters. The King requests all warriors to go 
and erradicate every single one of these beasts. %s you will be
sent to a stronghold called Othendra. You will have to train your skills
to be able to defeat Vlokyrryn, a dragon located in the Realm of Zero.
Once Vlokyrryn is defeated will the Kingdom of Valkria be safe. 
%s you must defeat Vlokyrryn because you are the only one capable of doing 
so. No one in the Kingdom's army has anywhere near the power or capability
of defeating Vlokyrryn except for you, %s.\n""") % (Player_name, Player_name, Player_name) 
	raw_input("Press any button to continue... ")
	global PlayerIG
	PlayerIG = Player(Player_name)



def intro():
	global MBurn
	MBurn = False
	os.system('cls')
	print """Welcome to Othendra, a medieval-based role-playing game 
	created by Vincent Gizzarelli.
		copyright 2015\n
----------------------------
-What would you like to do?-
----------------------------
1.) Start
2.) Load Game
3.) Exit
\n
"""
	option = raw_input("> ")
	if option == "1":
		name()
	elif option == "2":
		# Loads previous save data
		os.system('cls')
		global PlayerIG
		print "What save state would you like to load?"
		print " "
		print "1.) save_state1"
		print "2.) save_state2"
		print "3.) save_state3"
		print "4.) save_state4"
		print "5.) save_state5"
		print " "
		print "Press 'b' to go back."
		option = raw_input(' ')
		if option == '1':
			if os.path.exists("savefile1") == True:
				os.system('cls')
				with open('savefile1', 'rb') as f:
					PlayerIG = pickle.load(f)
				print "Loaded last save state..."
				option = raw_input(" ")
			else:
				print "You have no save_file for save_sate1"
				option = raw_input(' ')
				intro()
		elif option == '2':
			if os.path.exists("savefile2") == True:
				os.system('cls')
				with open('savefile2', 'rb') as f:
					PlayerIG = pickle.load(f)
				print "Loaded last save state..."
				option = raw_input(" ")
			else:
				print "You have no save_file for save_sate2"
				option = raw_input(' ')
				intro()
		elif option == '3':
			if os.path.exists("savefile3") == True:
				os.system('cls')
				with open('savefile3', 'rb') as f:
					PlayerIG = pickle.load(f)
				print "Loaded last save state..."
				option = raw_input(" ")
			else:
				print "You have no save_file for save_sate3"
				option = raw_input(' ')
				intro()
		elif option == '4':
			if os.path.exists("savefile4") == True:
				os.system('cls')
				with open('savefile4', 'rb') as f:
					PlayerIG = pickle.load(f)
				print "Loaded last save state..."
				option = raw_input(" ")
			else:
				print "You have no save_file for save_sate4"
				option = raw_input(' ')
				intro()
		elif option == '5':
			if os.path.exists("savefile5") == True:
				os.system('cls')
				with open('savefile5', 'rb') as f:
					PlayerIG = pickle.load(f)
				print "Loaded last save state..."
				option = raw_input(" ")
			else:
				print "You have no save_file for save_sate5"
				option = raw_input(' ')
				intro()
		elif option == 'b':
			intro()
		# If there is no previous save data will give an error
		else:
			os.system('cls')
			print "No save file exists..."
			option = raw_input(" ")
			intro()
		
	elif option == "3":
		sys.exit()
	else:
		print "\nSorry there was no option for \"%s\" \n\n" % option
		intro()

intro()


def start():
	os.system('cls')
	if PlayerIG.QuestActive == False:
		PlayerIG.qtitle = "None"
	if PlayerIG.exp >= PlayerIG.maxexp:
		levelup()
	print ("\n")
	print "###############################"
	print "     Welcome to Othendra"
	print "###############################"
	print "\n"
	print "Name: %s	 Gold: %s  Health: %s/%d  Mana: %d/%d" % (PlayerIG.name, PlayerIG.gold, PlayerIG.health, PlayerIG.maxhealth, PlayerIG.mana, PlayerIG.maxmana)
	print "Exp: %s/%s   Potions: %d   Arrows: %d" % (PlayerIG.exp, PlayerIG.maxexp, PlayerIG.pots, PlayerIG.arrows)
	print "Level: %d   Quest: %s" % (PlayerIG.level, PlayerIG.qtitle)
	print "\n"
	print "What would you like to do?"
	print "--------------------------"
	print "1.)  Fight"
	print "2.)  Shop"
	print "3.)  Healer"
	print "4.)  Stats"
	print "5.)  Inventory"
	print "6.)  Arch Mage"
	print "7.)  Quest Room"
	print "8.)  Trader"
	print "9.)  Monster Guide"
	print "10.) Save Game"
	print "11.) Exit (\"There is no current save system.\")"
	option = raw_input("> ")
	
	if option == "1":
		fightmap()
	elif option == "2":
		shop()
	elif option == "3":
		healer()
	elif option == "4":
		stats()
	elif option == "5":
		inventory()
	elif option == "6":
		archmage()
	elif option == "7":
		questboard()
	elif option == "8":
		trader()
	elif option == "10":
		os.system('cls')
		print "What save slot would you like to use?"
		print "1.) save_slot1"
		print "2.) save_slot2"
		print "3.) save_slot3"
		print "4.) save_slot4"
		print "5.) save_slot5"
		option = raw_input(' ')
		if option == '1':
			os.system('cls')
			with open('savefile1', 'wb') as f:
				pickle.dump(PlayerIG, f)
			print "\nGame has been saved...\n"
			option = raw_input(" ")
			start()
		elif option == '2':
			os.system('cls')
			with open('savefile2', 'wb') as f:
				pickle.dump(PlayerIG, f)
			print "\nGame has been saved...\n"
			option = raw_input(" ")
			start()
		elif option == '3':
			os.system('cls')
			with open('savefile3', 'wb') as f:
				pickle.dump(PlayerIG, f)
			print "\nGame has been saved...\n"
			option = raw_input(" ")
			start()
		elif option == '4':
			os.system('cls')
			with open('savefile4', 'wb') as f:
				pickle.dump(PlayerIG, f)
			print "\nGame has been saved...\n"
			option = raw_input(" ")
			start()
		elif option == '5':
			os.system('cls')
			with open('savefile5', 'wb') as f:
				pickle.dump(PlayerIG, f)
			print "\nGame has been saved...\n"
			option = raw_input(" ")
			start()
		else:
			start()
	elif option == "11":
		sys.exit()
	else:
		print "\nThere is no option for %s.\n" % option
		option = raw_input("Press any button to continue...\n")
		start()


### FOREST MONSTERS ###
class Goblin:
	def __init__(self, name):
		self.name = "Goblin"
		self.maxhealth = 40
		self.health = self.maxhealth
		self.attack = 10
		self.goldgain = 7
	@property
	def expgain(self):
		expgain = int(1.5 * (20 / (PlayerIG.level / 2)))
		return expgain
GoblinIG = Goblin("Goblin")

class Wolf:
	def __init__(self, name):
		self.name = "Dire Wolf"
		self.maxhealth = 50
		self.health = self.maxhealth
		self.attack = 15
		self.goldgain = 10
	@property
	def expgain(self):
		expgain = int(1.5 * (30 / (PlayerIG.level / 2)))
		return expgain
WolfIG = Wolf("Dire Wolf")

class Gnoll:
	def __init__(self, name):
		self.name = "Gnoll"
		self.maxhealth = 60
		self.health = self.maxhealth
		self.attack = 10
		self.goldgain = 20
	@property
	def expgain(self):
		expgain = int(1.5 * (60 / (PlayerIG.level / 2)))
		return expgain
GnollIG = Gnoll("Gnoll")


### Cave MONSTERS ###
class Troll:
	def __init__(self, name):
		self.name = "Cave Troll"
		self.maxhealth = 70
		self.health = self.maxhealth
		self.attack = 20
		self.goldgain = 20
	@property
	def expgain(self):
		expgain = int(1.5 * (150 / (PlayerIG.level / 2)))
		return expgain
TrollIG = Troll("Cave Troll")

class StoneSerpeant:
	def __init__(self, name):
		self.name = "Stone Serpeant"
		self.maxhealth = 80
		self.health = self.maxhealth
		self.attack = 35
		self.goldgain = 25
	@property
	def expgain(self):
		expgain = int(1.5 * (170 / (PlayerIG.level / 2)))
		return expgain
StoneSerpeantIG = StoneSerpeant("Stone Serpeant")

class Golem:
	def __init__(self, name):
		self.name = "Golem"
		self.maxhealth = 90
		self.health = self.maxhealth
		self.attack = 30
		self.goldgain = 30
	@property
	def expgain(self):
		expgain = int(1.5 * (200 / (PlayerIG.level / 2)))
		return expgain
GolemIG = Golem("Golem")

class Orc:
	def __init__(self, name):
		self.name = "Savage Orc"
		self.maxhealth = 100
		self.health = self.maxhealth
		self.attack = 20
		self.goldgain = 40
	@property
	def expgain(self):
		expgain = int(1.5 * (230 / (PlayerIG.level / 2)))
		return expgain
OrcIG = Orc("Savage Orc")

#Mountian monsters
class Griffon:
	def __init__(self, name):
		self.name = "Griffon"
		self.maxhealth = 200
		self.health = self.maxhealth
		self.attack = 20
		self.goldgain = 50
	@property
	def expgain(self):
		expgain = int(1.5 * (500 / (PlayerIG.level / 2)))
		return expgain
GriffonIG = Griffon("Griffin")

class Behemoth:
	def __init__(self, name):
		self.name = "Behemoth"
		self.maxhealth = 300
		self.health = self.maxhealth
		self.attack = 35
		self.goldgain = 75
	@property
	def expgain(self):
		expgain = 1.5 * (700 / (PlayerIG.level / 2))
		return expgain
BehemothIG = Behemoth("Behemoth")

class Dragon:
	def __init__(self, name):
		self.name = "Dragon"
		self.maxhealth = 200
		self.health = self.maxhealth
		self.attack = 40
		self.goldgain = 100
	@property
	def expgain(self):
		expgain = 1.5 * (1000 / (PlayerIG.level / 2))
		return expgain
DragonIG = Dragon("Dragon")

# Underworld Monsters
class Demon:
	def __init__(self, name):
		self.name = "Demon"
		self.maxhealth = 300
		self.health = self.maxhealth
		self.attack = 40
		self.goldgain = 130
	@property
	def expgain(self):
		expgain = int(1.5 * (1500 / (PlayerIG.level / 2)))
		return expgain
DemonIG =Demon("Demon")

class Chimera:
	def __init__(self, name):
		self.name = "Chimera"
		self.maxhealth = 400
		self.health = self.maxhealth
		self.attack = 30
		self.goldgain = 150
	@property
	def expgain(self):
		expgain = int(1.5 * (1700 / (PlayerIG.level / 2)))
		return expgain
ChimeraIG = Chimera("Chimera")

class Cerebrus:
	def __init__(self, name):
		self.name = "Cerebrus"
		self.maxhealth = 400
		self.health = self.maxhealth
		self.attack = 40
		self.goldgain = 180
	@property
	def expgain(self):
		expgain = int(1.5 * (1900 / (PlayerIG.level / 2)))
		return expgain
CerebrusIG = Cerebrus("Cerebrus")

class Hydra:
	def __init__(self, name):
		self.name = "Hydra"
		self.maxhealth = 500
		self.health = self.maxhealth
		self.attack = 45
		self.goldgain = 250
	@property
	def expgain(self):
		expgain = int(1.5 * (2100 / (PlayerIG.level / 2)))
		return expgain
HydraIG = Hydra("Hydra")

# Realm of Xero Monsters
class Phoenix:
	def __init__(self, name):
		self.name = "Phoenix"
		self.maxhealth = 750
		self.health = self.maxhealth
		self.attack = 50
		self.goldgain = 350
	@property
	def expgain(self):
		expgain = int(1.5 * (3000 / (PlayerIG.level / 2)))
		return expgain
PhoenixIG = Phoenix("Phoenix")

class Cthulu:
	def __init__(self, name):
		self.name = "Cthulhu"
		self.maxhealth = 1000
		self.health = self.maxhealth
		self.attack = 60
		self.goldgain = 500
	@property
	def expgain(self):
		expgain = int(1.5 * (4000 / (PlayerIG.level / 2)))
		return expgain
CthuluIG = Cthulu("Cthulhu")

class Leviathan:
	def __init__(self, name):
		self.name = "Leviathan"
		self.maxhealth = 800
		self.health = self.maxhealth
		self.attack = 45
		self.goldgain = 180
	@property
	def expgain(self):
		expgain = int(1.5 * (3500 / (PlayerIG.level / 2)))
		return expgain
LeviathanIG = Leviathan("Leviathan")

class Scylla:
	def __init__(self, name):
		self.name = "Scylla"
		self.maxhealth = 900
		self.health = self.maxhealth
		self.attack = 55
		self.goldgain = 400
	@property
	def expgain(self):
		expgain = int(1.5 * (3700 / (PlayerIG.level / 2)))
		return expgain
ScyllaIG = Scylla("Scylla")

# VLOKYRRYN
class Vlokyrryn:
	def __init__(self, name):
		self.name = "Vlokyrryn"
		self.maxhealth = 5000
		self.health = self.maxhealth
		self.attack = 80
		self.goldgain = 0
	@property
	def expgain(self):
		expgain = int(1.5 * (10000 / (PlayerIG.level / 2)))
		return expgain
VlokyrrynIG = Vlokyrryn("Vlokyrryn")


def acceptquest():
	os.system('cls')
	print " "
	print "Here are the list of available quests:"
	print " "
	print " Level 1-5 Quests"
	print "------------------"
	print "1.) Kill 7 Goblins      Reward: 100g"
	print "2.) Kill 7 Dire Wolves  Reward: 250g"
	print "3.) Kill 7 Gnolls       Reward: 500g"
	print ""
	print "Level 6-10 Quests"
	print "-----------------"
	print "4.) Kill 7 Cave Trolls      Reward: 600g"
	print "5.) Kill 7 Stone Serpeants  Reward: 800g"
	print "6.) Kill 7 Golems		   Reward: 1000g"         
	print "7.) Kill 5 Savage Orcs      Reward: 2000g"
	print " "
	print "Level 11-15 Quests"
	print "-------------------"
	print "8.)  Kill 10 Griffins  Reward: 1000g"
	print "9.)  Kill 10 Behemoths Reward: 1500g"
	print "10.) Kill 10 Dragons   Reward: 2500g"
	print " "
	print "Level 16-20 Quests"
	print "11.) Kill 10 Demons    Reward: 2000g"
	print "12.) Kill 10 Chimeras  Reward: 2500g"
	print "13.) Kill 7 Cerebruses Reward: 2500g"
	print "14.) Kill 5 Hydras     Reward: 3000g"
	print " "
	print "Level 21-24 Quests"
	print "------------------"
	print "15.) Kill 15 Phoenixes      Reward: 2500g"
	print "16.) Kill 15 Leviathans     Reward: 3000g"
	print "17.) Kill Scylla 10 times   Reward: 5000g"
	print "18.) Kill Cthulhu 10 times  Reward: 10000g"
	print " "
	print "Level 25 Quests"
	print "---------------"
	print "19.) Kill Vlokyrryn"
	print " "
	print "Press 'b' to go back."
	print " "
	option = raw_input("> ")
		
	
	if option == "1":
		if PlayerIG.QuestActive == False:
			if PlayerIG.q1c == False:
				PlayerIG.QuestActive = True
				PlayerIG.qenemy = 'Goblin'
				PlayerIG.kamount = 7
				PlayerIG.reward = 100
				PlayerIG.qenemykillcount = 0
				PlayerIG.q1 = True
				PlayerIG.qtitle = "\"Kill 7 Goblins\""
				print "\nYou have accepted \"Kill 7 Goblins\".\n"
				option = raw_input(" ")
				start()
			else:
				print "You have already completed this quest"
				option = raw_input(" ")
				acceptquest()
		else:
			print "\nYou have already accepted a quest.\n"
			option = raw_input(" ")
			questboard()

	elif option == "2":
		if PlayerIG.QuestActive == False:
			if PlayerIG.q2c == False:
				PlayerIG.QuestActive = True
				PlayerIG.qenemy = 'Dire Wolf'
				PlayerIG.kamount = 7
				PlayerIG.reward = 150
				PlayerIG.qenemykillcount = 0
				PlayerIG.q2 = True
				PlayerIG.qtitle = "\"Kill 7 Dire Wolves\""
				print "\nYou have accepted \"Kill 7 Dire Wolves\".\n"
				option = raw_input(" ")
				start()
			else:
				print "You have already completed this quest"
				option = raw_input(" ")
				acceptquest()
		else:
			print "\nYou have already accepted a quest.\n"
			option = raw_input(" ")
			questboard()

	elif option == "3":
		if PlayerIG.QuestActive == False:
			if PlayerIG.q3c == False:
				PlayerIG.QuestActive = True
				PlayerIG.qenemy = 'Gnoll'
				PlayerIG.kamount = 7
				PlayerIG.reward = 200
				PlayerIG.qenemykillcount = 0
				PlayerIG.q3 = True
				PlayerIG.qtitle = "\"Kill 7 Gnolls\""
				print "\nYou have accepted \"Kill 7 Gnolls\".\n"
				option = raw_input(" ")
				start()
			else:
				print "You have already completed this quest"
				option = raw_input(" ")
				acceptquest()
		else:
			print "\nYou have already accepted a quest.\n"
			option = raw_input(" ")
			questboard()
#### LEVEL 6-10
	elif option == "4":
		if PlayerIG.QuestActive == False:
			if PlayerIG.q4c == False:
				PlayerIG.QuestActive = True
				PlayerIG.qenemy = 'Cave Troll'
				PlayerIG.kamount = 7
				PlayerIG.reward = 600
				PlayerIG.qenemykillcount = 0
				PlayerIG.q4 = True
				PlayerIG.qtitle = "\"Kill 7 Cave Trolls\""
				print "\nYou have accepted \"Kill 7 Cave Trolls\".\n"
				option = raw_input(" ")
				start()
			else:
				print "You have already completed this quest"
				option = raw_input(" ")
				acceptquest()
		else:
			print "\nYou have already accepted a quest.\n"
			option = raw_input(" ")
			questboard()

	elif option == "5":
		if PlayerIG.QuestActive == False:
			if PlayerIG.q5c == False:
				PlayerIG.QuestActive = True
				PlayerIG.qenemy = 'Stone Serpeant'
				PlayerIG.kamount = 7
				PlayerIG.reward = 800
				PlayerIG.qenemykillcount = 0
				PlayerIG.q5 = True
				PlayerIG.qtitle = "\"Kill 7 Stone Serpeants\""
				print "\nYou have accepted \"Kill 7 Stone Serpeants\".\n"
				option = raw_input(" ")
				start()
			else:
				print "You have already completed this quest"
				option = raw_input(" ")
				acceptquest()
		else:
			print "\nYou have already accepted a quest.\n"
			option = raw_input(" ")
			questboard()

	elif option == "6":
		if PlayerIG.QuestActive == False:
			if PlayerIG.q6c == False:
				PlayerIG.QuestActive = True
				PlayerIG.qenemy = 'Golem'
				PlayerIG.kamount = 7
				PlayerIG.reward = 1000
				PlayerIG.qenemykillcount = 0
				PlayerIG.q6 = True
				PlayerIG.qtitle = "\"Kill 7 Golems\""
				print "\nYou have accepted \"Kill 7 Golems\".\n"
				option = raw_input(" ")
				start()
			else:
				print "You have already completed this quest"
				option = raw_input(" ")
				acceptquest()
		else:
			print "\nYou have already accepted a quest.\n"
			option = raw_input(" ")
			questboard()
		
	elif option == "7":
		if PlayerIG.QuestActive == False:
			if PlayerIG.q7c == False:
				PlayerIG.QuestActive = True
				PlayerIG.qenemy = 'Savage Orc'
				PlayerIG.kamount = 5
				PlayerIG.reward = 2000
				PlayerIG.qenemykillcount = 0
				PlayerIG.q7 = True
				PlayerIG.qtitle = "\"Kill 5 Savage Orcs\""
				print "\nYou have accepted \"Kill 5 Savage Orcs\".\n"
				option = raw_input(" ")
				start()
			else:
				print "You have already completed this quest"
				option = raw_input(" ")
				acceptquest()
		else:
			print "\nYou have already accepted a quest.\n"
			option = raw_input(" ")
			questboard()
#### LEVEL 11-15 QUESTS
	elif option == "8":
		if PlayerIG.QuestActive == False:
			if PlayerIG.q8c == False:
				PlayerIG.QuestActive = True
				PlayerIG.qenemy = 'Griffin'
				PlayerIG.kamount = 10
				PlayerIG.reward = 1000
				PlayerIG.qenemykillcount = 0
				PlayerIG.q8 = True
				PlayerIG.qtitle = "\"Kill 10 Griffins\""
				print "\nYou have accepted \"Kill 7 Griffins\".\n"
				option = raw_input(" ")
				start()
			else:
				print "You have already completed this quest"
				option = raw_input(" ")
				acceptquest()
		else:
			print "\nYou have already accepted a quest.\n"
			option = raw_input(" ")
			questboard()

	elif option == "9":
		if PlayerIG.QuestActive == False:
			if PlayerIG.q9c == False:
				PlayerIG.QuestActive = True
				PlayerIG.qenemy = 'Behemoth'
				PlayerIG.kamount = 10
				PlayerIG.reward = 1500
				PlayerIG.qenemykillcount = 0
				PlayerIG.q9 = True
				PlayerIG.qtitle = "\"Kill 7 Behemoths\""
				print "\nYou have accepted \"Kill 7 Behemoths\".\n"
				option = raw_input(" ")
				start()
			else:
				print "You have already completed this quest"
				option = raw_input(" ")
				acceptquest()
		else:
			print "\nYou have already accepted a quest.\n"
			option = raw_input(" ")
			questboard()

	elif option == "10":
		if PlayerIG.QuestActive == False:
			if PlayerIG.q10c == False:
				PlayerIG.QuestActive = True
				PlayerIG.qenemy = 'Dragon'
				PlayerIG.kamount = 10
				PlayerIG.reward = 2500
				PlayerIG.qenemykillcount = 0
				PlayerIG.q10 = True
				PlayerIG.qtitle = "\"Kill 10 Dragons\""
				print "\nYou have accepted \"Kill 10 Dragons\".\n"
				option = raw_input(" ")
				start()
			else:
				print "You have already completed this quest"
				option = raw_input(" ")
				acceptquest()
		else:
			print "\nYou have already accepted a quest.\n"
			option = raw_input(" ")
			questboard()
### QUESTS LEVEL 16-20
	elif option == "11":
		if PlayerIG.QuestActive == False:
			if PlayerIG.q11c == False:
				PlayerIG.QuestActive = True
				PlayerIG.qenemy = 'Demon'
				PlayerIG.kamount = 10
				PlayerIG.reward = 2000
				PlayerIG.qenemykillcount = 0
				PlayerIG.q11 = True
				PlayerIG.qtitle = "\"Kill 10 Demons\""
				print "\nYou have accepted \"Kill 7 Demons\".\n"
				option = raw_input(" ")
				start()
			else:
				print "You have already completed this quest"
				option = raw_input(" ")
				acceptquest()
		else:
			print "\nYou have already accepted a quest.\n"
			option = raw_input(" ")
			questboard()

	elif option == "12":
		if PlayerIG.QuestActive == False:
			if PlayerIG.q12c == False:
				PlayerIG.QuestActive = True
				PlayerIG.qenemy = 'Chimera'
				PlayerIG.kamount = 10
				PlayerIG.reward = 2500
				PlayerIG.qenemykillcount = 0
				PlayerIG.q12 = True
				PlayerIG.qtitle = "\"Kill 10 Chimeras\""
				print "\nYou have accepted \"Kill 10 Chimeras\".\n"
				option = raw_input(" ")
				start()
			else:
				print "You have already completed this quest"
				option = raw_input(" ")
				acceptquest()
		else:
			print "\nYou have already accepted a quest.\n"
			option = raw_input(" ")
			questboard()

	elif option == "13":
		if PlayerIG.QuestActive == False:
			if PlayerIG.q13c == False:
				PlayerIG.QuestActive = True
				PlayerIG.qenemy = 'Cerebrus'
				PlayerIG.kamount = 7
				PlayerIG.reward = 2500
				PlayerIG.qenemykillcount = 0
				PlayerIG.q13 = True
				PlayerIG.qtitle = "\"Kill 7 Cerebruses\""
				print "\nYou have accepted \"Kill 7 Cerebruses\".\n"
				option = raw_input(" ")
				start()
			else:
				print "You have already completed this quest"
				option = raw_input(" ")
				acceptquest()
		else:
			print "\nYou have already accepted a quest.\n"
			option = raw_input(" ")
			questboard()
		
	elif option == "14":
		if PlayerIG.QuestActive == False:
			if PlayerIG.q14c == False:
				PlayerIG.QuestActive = True
				PlayerIG.qenemy = 'Hydra'
				PlayerIG.kamount = 5
				PlayerIG.reward = 3000
				PlayerIG.qenemykillcount = 0
				PlayerIG.q14 = True
				PlayerIG.qtitle = "\"Kill 5 Hydras\""
				print "\nYou have accepted \"Kill 5 Hydras\".\n"
				option = raw_input(" ")
				start()
			else:
				print "You have already completed this quest"
				option = raw_input(" ")
				acceptquest()
		else:
			print "\nYou have already accepted a quest.\n"
			option = raw_input(" ")
			questboard()
#### QUESTS LEVEL 21-24
	elif option == "15":
		if PlayerIG.QuestActive == False:
			if PlayerIG.q15c == False:
				PlayerIG.QuestActive = True
				PlayerIG.qenemy = 'Phoenix'
				PlayerIG.kamount = 15
				PlayerIG.reward = 2500
				PlayerIG.qenemykillcount = 0
				PlayerIG.q15 = True
				PlayerIG.qtitle = "\"Kill 15 Phoenixes\""
				print "\nYou have accepted \"Kill 15 Phoenixes\".\n"
				option = raw_input(" ")
				start()
			else:
				print "You have already completed this quest"
				option = raw_input(" ")
				acceptquest()
		else:
			print "\nYou have already accepted a quest.\n"
			option = raw_input(" ")
			questboard()

	elif option == "16":
		if PlayerIG.QuestActive == False:
			if PlayerIG.q16c == False:
				PlayerIG.QuestActive = True
				PlayerIG.qenemy = 'Leviathan'
				PlayerIG.kamount = 15
				PlayerIG.reward = 2500
				PlayerIG.qenemykillcount = 0
				PlayerIG.q16 = True
				PlayerIG.qtitle = "\"Kill 15 Leviathans\""
				print "\nYou have accepted \"Kill 15 Leviathans\".\n"
				option = raw_input(" ")
				start()
			else:
				print "You have already completed this quest"
				option = raw_input(" ")
				acceptquest()
		else:
			print "\nYou have already accepted a quest.\n"
			option = raw_input(" ")
			questboard()

	elif option == "17":
		if PlayerIG.QuestActive == False:
			if PlayerIG.q17c == False:
				PlayerIG.QuestActive = True
				PlayerIG.qenemy = 'Scylla'
				PlayerIG.kamount = 10
				PlayerIG.reward = 5000
				PlayerIG.qenemykillcount = 0
				PlayerIG.q17 = True
				PlayerIG.qtitle = "\"Kill Scylla 10 times\""
				print "\nYou have accepted \"Kill Scylla 10 times\".\n"
				option = raw_input(" ")
				start()
			else:
				print "You have already completed this quest"
				option = raw_input(" ")
				acceptquest()
		else:
			print "\nYou have already accepted a quest.\n"
			option = raw_input(" ")
			questboard()
		
	elif option == "18":
		if PlayerIG.QuestActive == False:
			if PlayerIG.q18c == False:
				PlayerIG.QuestActive = True
				PlayerIG.qenemy = 'Cthulhu'
				PlayerIG.kamount = 10
				PlayerIG.reward = 10000
				PlayerIG.qenemykillcount = 0
				PlayerIG.q18 = True
				PlayerIG.qtitle = "\"Kill Cthulhu 10 times\""
				print "\nYou have accepted \"Kill Cthulhu 10 times\".\n"
				option = raw_input(" ")
				start()
			else:
				print "You have already completed this quest"
				option = raw_input(" ")
				acceptquest()
			
	elif option == "19":
		if PlayerIG.QuestActive == False:
			if PlayerIG.q19c == False:
				PlayerIG.QuestActive = True
				PlayerIG.qenemy = 'Vlokyrryn'
				PlayerIG.kamount = 1
				PlayerIG.reward = 100000
				PlayerIG.qenemykillcount = 0
				PlayerIG.q19 = True
				PlayerIG.qtitle = "\"Kill Vlokyrryn\""
				print "\nYou have accepted \"Kill Vlokyrryn\".\n"
				option = raw_input(" ")
				start()
			else:
				print "You have already completed this quest"
				option = raw_input(" ")
				acceptquest()
						
		else:
			print "\nYou have already accepted a quest.\n"
			option = raw_input(" ")
			questboard()
			
			
	elif option == "b":
		questboard()	


def questboard():
	os.system('cls')
	print "\n"
	print "==------------------------------=="
	print "==       Quest Room             =="
	print "==------------------------------=="
	print "\n Hello what can I do for you?\n"
	print "1.) Accept Quest"
	print "2.) Turn in Quest"
	print "3.) Reject Current Quest"
	print "4.) Back"
	print " "
	option = raw_input("> ")
	if option == "1":
		acceptquest()
	elif option == "2":
		turnquest()
	elif option == '3':
		
		if PlayerIG.QuestActive == False:
			"\nYou haven't accepted any quests\n"
			option = raw_input(" ")
			acceptquest()
		else:
			print "Are you sure you want to reject %s?" % PlayerIG.qtitle
			print 'Type \'yes\' or \'no\''
			option = raw_input(" ")
			if option == 'yes':
				PlayerIG.QuestActive = False
				if PlayerIG.q1 == True:
					print "You have rejected %s" % PlayerIG.qtitle
					PlayerIG.q1 = False
				elif PlayerIG.q2 == True:
					print "You have rejected %s" % PlayerIG.qtitle
					PlayerIG.q2 = False
				elif PlayerIG.q3 == True:
					print "You have rejected %s" % PlayerIG.qtitle
					PlayerIG.q3 = False
				elif PlayerIG.q4 == True:
					print "You have rejected %s" % PlayerIG.qtitle
					PlayerIG.q4 = False
				elif PlayerIG.q5 == True:
					print "You have rejected %s" % PlayerIG.qtitle
					PlayerIG.q5 = False
				elif PlayerIG.q6 == True:
					print "You have rejected %s" % PlayerIG.qtitle
					PlayerIG.q6 = False
				elif PlayerIG.q7 == True:
					print "You have rejected %s" % PlayerIG.qtitle
					PlayerIG.q7 = False
				elif PlayerIG.q8 == True:
					print "You have rejected %s" % PlayerIG.qtitle
					PlayerIG.q8 = False
				elif PlayerIG.q9 == True:
					print "You have rejected %s" % PlayerIG.qtitle
					PlayerIG.q9 = False
				elif PlayerIG.q10 == True:
					print "You have rejected %s" % PlayerIG.qtitle
					PlayerIG.q10 = False
				elif PlayerIG.q11 == True:
					print "You have rejected %s" % PlayerIG.qtitle
					PlayerIG.q11 = False
				elif PlayerIG.q12 == True:
					print "You have rejected %s" % PlayerIG.qtitle
					PlayerIG.q12 = False
				elif PlayerIG.q13 == True:
					print "You have rejected %s" % PlayerIG.qtitle
					PlayerIG.q13 = False
				elif PlayerIG.q14 == True:
					print "You have rejected %s" % PlayerIG.qtitle
					PlayerIG.q14 = False
				elif PlayerIG.q15 == True:
					print "You have rejected %s" % PlayerIG.qtitle
					PlayerIG.q15 = False
				elif PlayerIG.q16 == True:
					print "You have rejected %s" % PlayerIG.qtitle
					PlayerIG.q16 = False
				elif PlayerIG.q17 == True:
					print "You have rejected %s" % PlayerIG.qtitle
					PlayerIG.q17 = False
				elif PlayerIG.q18 == True:
					print "You have rejected %s" % PlayerIG.qtitle
					PlayerIG.q18 = False
				elif PlayerIG.q19 == True:
					print "You have rejected %s" % PlayerIG.qtitle
					PlayerIG.q19 = False
				option = raw_input(" ")
				questboard()
			else: 
				questboard()
			
	elif option == "4":
		start()
	else:
		questboard()

def turnquest():
	if PlayerIG.QuestActive == False:
		print "\nYou haven't accepted any quests.\n"
		option = raw_input(" ")
		questboard()
	else:
		if PlayerIG.qenemykillcount >= PlayerIG.kamount:
			if PlayerIG.q1 == True:
				PlayerIG.q1c = True
				PlayerIG.q1 = False
			if PlayerIG.q2 == True:
				PlayerIG.q2c = True
				PlayerIG.q2 = False
			if PlayerIG.q3 == True:
				PlayerIG.q3c = True
				PlayerIG.q3 = False
			if PlayerIG.q4 == True:
				PlayerIG.q4c = True
				PlayerIG.q4 = False
			if PlayerIG.q5 == True:
				PlayerIG.q5c = True
				PlayerIG.q5 = False
			if PlayerIG.q6 == True:
				PlayerIG.q6c = True
				PlayerIG.q6 = False
			if PlayerIG.q7 == True:
				PlayerIG.q7c = True
				PlayerIG.q7 = False
			if PlayerIG.q8 == True:
				PlayerIG.q8c = True
				PlayerIG.q8 = False
			if PlayerIG.q9 == True:
				PlayerIG.q9c = True
				PlayerIG.q9 = False
			if PlayerIG.q10 == True:
				PlayerIG.q10c = True
				PlayerIG.q10 = False
			if PlayerIG.q11 == True:
				PlayerIG.q11c = True
				PlayerIG.q11 = False
			if PlayerIG.q12 == True:
				PlayerIG.q12c = True
				PlayerIG.q12 = False
			if PlayerIG.q13 == True:
				PlayerIG.q13c = True
				PlayerIG.q13 = False
			if PlayerIG.q14 == True:
				PlayerIG.q14c = True
				PlayerIG.q14 = False
			if PlayerIG.q15 == True:
				PlayerIG.q15c = True
				PlayerIG.q15 = False
			if PlayerIG.q16 == True:
				PlayerIG.q16c = True
				PlayerIG.q16 = False
			if PlayerIG.q17 == True:
				PlayerIG.q17c = True
				PlayerIG.q17 = False
			if PlayerIG.q18 == True:
				PlayerIG.q18c = True
				PlayerIG.q18 = False
			if PlayerIG.q19 == True:
				PlayerIG.q19c = True
				PlayerIG.q19 = False
			print "You have turned in %s and earned %s gold." % (PlayerIG.qtitle, PlayerIG.reward)
			PlayerIG.gold += PlayerIG.reward
			PlayerIG.QuestActive = False
			option = raw_input(" ")
			questboard()
		else:
			print "\nYou haven't met the requirement yet."
			print "You have only killed %s/%s %s's\n" % (PlayerIG.qenemykillcount, PlayerIG.kamount, PlayerIG.qenemy)
			option = raw_input(" ")
			questboard()
	
	
def archmage():
	os.system('cls')
	print "Arch Mage: \"What can I do for you?\""
	print " "
	print "1.) Teach Spell"
	print "2.) Restore Mana"
	print "3.) Back"
	option = raw_input("> ")
	
	if option == "1":
		learnspell()
	elif option == "2":
		print "\nThere, I have restored your mana."
		PlayerIG.mana = PlayerIG.maxmana
		option = raw_input(" ")
		archmage()
	elif option == "3":
		start()
	else:
		print "There is no option for that."
		archmage()

def learnspell():
	os.system('cls')
	print "========="
	print "Spells: "
	print "========="
	print "1.) Fireball (Deals up to +10 your Magic Attack) [costs 10 mana]  cost:[100g]"
	print " "
	print "2.) Lightning Strike (Deals up to +25 your Magic Attack) [costs 15 mana] cost:[500g]"
	print " "
	print "3.) Magic Missile (Deals up to +50 your Magic Attack) [costs 30 mana] cost:[1000g]"
	print " "
	print "4.) Hellish Scald (Burns enemy for 10% of their health each turn)  [costs 60 mana] cost:[1000g]"
	print " "
	print "5.) Rejuvination  (Heals 100 health) [costs 50 mana] cost:[2000g]" 
	print " "
	print "6.) Tsunami (Deals up to +500 your Magic Attack) [costs 180 mana] cost:[5000g]"
	print " "
	print "7.) Gates of the Underworld (Deals up to +1000 your Magic Attack) [costs 225 mana]  cost:[10000g]"
	print " "
	print "8.) Wrath of God  (Deals a substantial amount of damage and sets your health to 1.) [costs 275 mana]  cost:[12000g]"
	print "----------------------------------------------------"
	print " "
	print "Press 'b' to go back.\n"
	option = raw_input("> ")
	
	if option == "1":
		if "Fireball" in PlayerIG.spells:
			print "You have already learned this spell."
			option = raw_input(" ")
			learnspell()
		else:
			if PlayerIG.gold >= 100:
				print "\nYou have learned the \'Fireball\' spell for 100 gold.\n"
				PlayerIG.gold -= 100
				PlayerIG.spells.append("Fireball")
				option = raw_input(" ")
			else:
				print "\nYou don't have enough gold.\n"
				option = raw_input(" ")
				learnspell()
			learnspell()
		
	elif option == "2":
		if "Lightning Strike" in PlayerIG.spells:
			print "You have already learned this spell."
			option = raw_input(" ")
			learnspell()
		else:
			if PlayerIG.gold >= 500:
				print "\nYou have learned the \'Lightning Strik\' spell for 500 gold.\n"
				PlayerIG.gold -= 500
				PlayerIG.spells.append("Lightning Strike")
				option = raw_input(" ")
			else:
				print "\nYou don't have enough gold.\n"
				option = raw_input(" ")
				learnspell()
			learnspell()
		
	elif option == "3":
		if "Magic Missile" in PlayerIG.spells:
			print "You have already learned this spell."
			option = raw_input(" ")
			learnspell()
		else:
			if PlayerIG.gold >= 1000:
				print "\nYou have learned the \'Magic Missile spell\' for 1000 gold.\n"
				PlayerIG.gold -= 1000
				PlayerIG.spells.append("Magic Missile")
				option = raw_input(" ")
			else:
				print "\nYou don't have enough gold.\n"
				option = raw_input(" ")
				learnspell()
			learnspell()
		
	elif option == "4":
		if "Hellish Scald" in PlayerIG.spells:
			print "You have already learned this spell."
			option = raw_input(" ")
			learnspell()
		else:
			if PlayerIG.gold >= 1000:
				print "\nYou have learned the \'Hellish Scald\' spell for 1000 gold.\n"
				PlayerIG.gold -= 1000
				PlayerIG.spells.append("Hellish Scald")
				option = raw_input(" ")
			else:
				print "\nYou don't have enough gold.\n"
				option = raw_input(" ")
				learnspell()
			learnspell()
		
	elif option == "5":
		if "Rejuvination" in PlayerIG.spells:
			print "You have already learned this spell."
			option = raw_input(" ")
			learnspell()
		else:
			if PlayerIG.gold >= 2000:
				print "\nYou have learned the \'Rejuvination spell\' for 2000 gold.\n"
				PlayerIG.gold -= 2000
				PlayerIG.spells.append("Rejuvination")
				option = raw_input(" ")
			else:
				print "\nYou don't have enough gold.\n"
				option = raw_input(" ")
				learnspell()
			learnspell()
		
	elif option == "6":
		if "Tsunami" in PlayerIG.spells:
			print "You have already learned this spell."
			option = raw_input(" ")
			learnspell()
		else:
			if PlayerIG.gold >= 5000:
				print "\nYou have learned the \'Tsunami spell\' for 5000 gold.\n"
				PlayerIG.gold -= 5000
				PlayerIG.spells.append("Tsunami")
				option = raw_input(" ")
			else:
				print "\nYou don't have enough gold.\n"
				option = raw_input(" ")
				learnspell()
			learnspell()
		
	elif option == "7":
		if "Gates of the Underworld" in PlayerIG.spells:
			print "You have already learned this spell."
			option = raw_input(" ")
			learnspell()
		else:
			if PlayerIG.gold >= 10000:
				print "\nYou have learned the \'Gates of the Underworld\' spell for 10000 gold.\n"
				PlayerIG.gold -= 10000
				PlayerIG.spells.append("Gates of the Underworld")
				option = raw_input(" ")
			else:
				print "\nYou don't have enough gold.\n"
				option = raw_input(" ")
				learnspell()
			learnspell()
		
	elif option == "8":
		if "Wrath of God" in PlayerIG.spells:
			print "You have already learned this spell."
			option = raw_input(" ")
			learnspell()
		else:
			if PlayerIG.gold >= 12000:
				print "\nYou have learned the \'Wrath of God\' spell for 12000 gold.\n"
				PlayerIG.gold -= 12000
				PlayerIG.spells.append("Wrath of God")
				option = raw_input(" ")
			else:
				print "\nYou don't have enough gold.\n"
				option = raw_input(" ")
				learnspell()
			learnspell()
	
	elif option == "b":
			archmage()
	
	else:
			print "I'm sorry I can't teach you that."
			option = raw_input(" ")
			learnspell()
	

def inventory():
	os.system('cls')
	print " \n"
	print "=======---------------------------======="
	print "~       What would you like to do?      ~"
	print "=======---------------------------======="
	print "1.) Equip "
	print "2.) Back "
	print "\n_________"
	print "Inventory:"
	print "----------"
	for item in PlayerIG.inventory:
		print "* %s" % item
	print "==============="
	print " "
	option = raw_input("> ")
	if option == "1":
		equip()
	if option == "2":
		start()
	else:
		inventory() 

def trader():
	os.system('cls')
	print "\nHello what can I do for you?\n"
	print " "
	print "1.)Sell"
	print "2.)Back"
	print ' '
	option = raw_input("> ")
	if option == "1":
		trade()
	elif option == "2":
		start()

def trade():
	os.system('cls')
	print "\nWhat would you like to sell?"
	print " "
	for item in PlayerIG.inventory:
		print "* %s" % item
	print" "
	print "Type 'b' to go back.\n"
	option1 = raw_input("> ")
	if option1 in PlayerIG.inventory:
		if option1 in PlayerIG.weap or option1 in PlayerIG.wbow or option1 in PlayerIG.armA or option1 in PlayerIG.armH or option1 in PlayerIG.armL or option1 in PlayerIG.armB or option1 in PlayerIG.armF:
			print "You cannot sell items that are equipped."
		
		else:
			if option1 in Weapons:
				price = int(Weapons[option1] / 2)
				print "\nYou are going to get %s gold. Are you sure you would like to sell %s?" % (price, option1)
				print '"type \'yes\' or \'no\'"'
				option = raw_input(" ")
				if option == "yes":
					PlayerIG.weaps.remove(option1)
					PlayerIG.inventory.remove(option1)
					PlayerIG.gold += price
					print "\nYou have sold %s for %s gold." % (option1, price)
				else:
					trade()
								
			elif option1 in Bows:
				price = int(Bows[option1] / 2)
				print "\nYou are going to get %s gold. Are you sure you would like to sell %s?" % (price, option1)
				print '"type \'yes\' or \'no\'"'
				print " "
				option = raw_input(" ")
				if option == "yes":
					PlayerIG.bows.remove(option1)
					PlayerIG.inventory.remove(option1)
					PlayerIG.gold += price
					print "\nYou have sold %s for %s gold." % (option1, price)
				else:
					trade()
			
			elif option1 in armH:
				price = int(armH[option1] / 2)
				print "\nYou are going to get %s gold. Are you sure you would like to sell %s?" % (price, option1)
				print '"type \'yes\' or \'no\'"'
				print " "
				option = raw_input(" ")
				if option == "yes":
					PlayerIG.armsH.remove(option1)
					PlayerIG.inventory.remove(option1)
					PlayerIG.gold += price
					print "\nYou have sold %s for %s gold." % (option1, price)
				else:
					trade()
			
			elif option1 in armB:
				price = int(armB[option1] / 2)
				print "\nYou are going to get %s gold. Are you sure you would like to sell %s?" % (price, option1)
				print '"type \'yes\' or \'no\'"'
				print " "
				option = raw_input(" ")
				if option == "yes":
					PlayerIG.armsB.remove(option1)
					PlayerIG.inventory.remove(option1)
					PlayerIG.gold += price
					print "\nYou have sold %s for %s gold." % (option1, price)
				else:
					trade()
					
			
			elif option1 in armL:
				price = int(armL[option1] / 2)
				print "\nYou are going to get %s gold. Are you sure you would like to sell %s?" % (price, option1)
				print '"type \'yes\' or \'no\'"'
				print " "
				option = raw_input(" ")
				if option == "yes":
					PlayerIG.armsL.remove(option1)
					PlayerIG.inventory.remove(option1)
					PlayerIG.gold += price
					print "\nYou have sold %s for %s gold." % (option1, price)
				else:
					trade()
					
			elif option1 in armF:
				price = int(armF[option1] / 2)
				print "\nYou are going to get %s gold. Are you sure you would like to sell %s?" % (price, option1)
				print '"type \'yes\' or \'no\'"'
				print " "
				option = raw_input(" ")
				if option == "yes":
					PlayerIG.armsF.remove(option1)
					PlayerIG.inventory.remove(option1)
					PlayerIG.gold += price
					print "\nYou have sold %s for %s gold." % (option1, price)
				else:
					trade()
	
	elif option1 == "b":
		trader()
			
	else:
		print "You don't have that item."	
	option = raw_input(" ")
	trade()
				

				
			
def shop():
	os.system('cls')
	print "\n"
	print " "
	print "====-----------------------------------===="
	print "	     OTHENDRA SHOP                 "
	print "====-----------------------------------===="
	print "     Hello what would you like to buy?"
	print " "
	print "~  Items for Gathering:  ~"
	print "=========================="
	print "1g.) Woodcutter's Axe  [100g]"
	print "2g.) Pickaxe           [100g]"
	print " "
	print "========="
	print "Weapons: "
	print "========="
	print "1.) Arrows(x5): (Ammo for bows)    cost:[10g] "
	print "2.) Arrows(x25): (Ammo for bows)   cost:[50g]"
	print "3.) Arrows(x50): (Ammo for bows)   cost:[100g]"
	print " "
	print "[Level 0 Weapon]:"
	print "* Rusty Sword (+10 Attack Power)  cost:[30g]"
	print " "
	print "[Level 1-5 Weapons]:"
	print "* Battleaxe (+15 Attack Power)  cost:[100g]"
	print "* Wooden Bow (+20 Range Power)  cost:[100g]"
	print "* Wooden Staff (+15 Magic Power and +10 Attack Power) cost:[130g]"
	print " "
	print "[Level 6-10 Weapons]:"
	print "* Dark Saber (+25 Attack Power) cost:[700g]"
	print "* Steel Bow  (+30 Range Power)  cost:[700g]"
	print "* Jade Staff (+25 Magic Power and + 20 Attack Power) cost:[750g]"
	print " "
	print "[Level 11-15 Weapons]:"
	print "* Sword of Dawn (+40 Attack Power) cost:[1500g]"
	print "* Lightning Bow (+45 Range Power)  cost:[1500g]"
	print "* Holy Staff (+40 Magic Power and + 30 Attack Power) cost:[1700g]"
	print " "
	print "[Level 16-20 Weapons]:"
	print "* Demon Blade (+60 Attack Power)    cost:[3000g]"
	print "* Bow of Hellfire (+70 Range Power) cost:[3000g]"
	print "* Phoenix Staff (+60 Magic Power and +45 Attack Power) cost:[3500g]"
	print " "
	print "[Level 21-24 Weapons]:"
	print "* Death's Blade (+80 Attack Power)  cost:[6000g]"
	print "* Phantom Bow (+90 Range Power)     cost:[6000g]"
	print "* Staff of Fallen Ashes (+80 magic Power and +60 Attack Power) cost:[7000g]"
	print " "
	print "[Level 25 Weapons]:"
	print "* Excalibur (+100 Atack Power)  cost:[10000g]"
	print "* Dragon Bow (+120 Range Power) cost:[11000g]"
	print "* Grandmaster Staff (+100 Magic Power and +80 Attack Power) cost:[15000g]"
	print " "
	print "=========="
	print "  Armor:"
	print "=========="
	print "[Level 1-5 Armor]"
	print "* Leather Tunic     (+10 Defense) cost:[100g]"
	print "* Leather Greaves   (+5 Defense)  cost:[70g]"   
	print "* Leather Gauntlets (+3 Defense)  cost:[30g]"  
	print "* Leather Boots     (+3 Defense)  cost:[30g]"
	print "* Leather Helmet    (+4 Defense)  cost:[50g]"
	print " "
	print "* Mage Robe    (+5 Defense +5 Mana) cost:[100g]"
	print "* Mage Pants   (+3 Defense +3 Mana)  cost:[70g]"   
	print "* Mage Gloves  (+2 Defense +2 Mana)  cost:[30g]"  
	print "* Mage Boots   (+2 Defense +2 Mana)  cost:[30g]"
	print "* Mage Hood    (+3 Defense +3 Mana)  cost:[50g]"		
	print " " 
	print "[Level 6-10 Armor]"
	print "* Steel Armor     (+25 Defense) cost:[200g]"
	print "* Steel Greaves   (+8 Defense)  cost:[100g]"   
	print "* Steel Gauntlets (+5 Defense)  cost:[50g]"  
	print "* Steel Boots     (+5 Defense)  cost:[50g]"
	print "* Steel Helmet    (+7 Defense)  cost:[100g]"	
	print " "
	print "* Priest Robe   (+12 Defense +12 Mana) cost:[200g]"
	print "* Priest Pants  (+4 Defense  +4 Mana)  cost:[100g]"   
	print "* Priest Gloves (+3 Defense  +3 Mana)  cost:[50g]"  
	print "* Priest Boots  (+3 Defense  +3 Mana)  cost:[50g]"
	print "* Priest Hood   (+4 Defense  +4 Mana)  cost:[100g]"	
	print " " 
	print "[Level 11-15 Armor]"
	print "* Plasma Armor     (+40 Defense) cost:[400g]"
	print "* Plasma Greaves   (+20 Defense) cost:[200g]"   
	print "* Plasma Gauntlets (+10 Defense) cost:[100g]"  
	print "* Plasma Boots     (+10 Defense) cost:[100g]"
	print "* Plasma Helmet    (+20 Defense) cost:[200g]"
	print " "
	print "* Phoenix Robe   (+20 Defense +20 Mana) cost:[400g]"
	print "* Phoenix Pants  (+10 Defense +10 Mana) cost:[200g]"   
	print "* Phoenix Gloves (+5 Defense  +5 Mana)  cost:[100g]"  
	print "* Phoenix Boots  (+5 Defense  +5 Mana)  cost:[100g]"
	print "* Phoenix Hood   (+10 Defense +10 Mana) cost:[200g]"	
	print " " 
	print "[Level 16-20 Armor]"
	print "* Demon Armor     (+60 Defense)  cost:[750g]"
	print "* Demon Greaves   (+30 Defense)  cost:[400g]"   
	print "* Demon Gauntlets (+15 Defense)  cost:[225g]"  
	print "* Demon Boots     (+15 Defense)  cost:[225g]"
	print "* Demon Helmet    (+30 Defense)  cost:[400g]"
	print " "
	print "* Necromancer Robe   (+30 Defense +30 Mana) cost:[750g]"
	print "* Necromancer Pants  (+15 Defense +15 Mana) cost:[400g]"   
	print "* Necromancer Gloves (+8 Defense  +8 Mana)  cost:[225g]"  
	print "* Necromancer Boots  (+8 Defense  +8 Mana)  cost:[225g]"
	print "* Necromancer Hood   (+15 Defense +15 Mana) cost:[400g]"	
	print " " 
	print "[Level 21-24 Armor]"
	print "* Phantom Armor     (+80 Defense) cost:[2000g]"
	print "* Phantom Greaves   (+40 Defense) cost:[700g]"   
	print "* Phantom Gauntlets (+20 Defense) cost:[300g]"  
	print "* Phantom Boots     (+20 Defense) cost:[300g]"
	print "* Phantom Helmet    (+40 Defense) cost:[700g]"	
	print " "
	print "* Death's Robe    (+40 Defense +40 Mana) cost:[2000g]"
	print "* Death's Greaves (+20 Defense +20 Mana) cost:[700g]"   
	print "* Death's Gloves  (+10 Defense +10 Mana) cost:[300g]"  
	print "* Death's Boots   (+10 Defense +10 Mana) cost:[300g]"
	print "* Death's Hood    (+20 Defense +20 Mana) cost:[700g]"	
	print " " 
	print "[Level 25 Armor]"
	print "* Champion Armor     (+100 Defense) cost:[5000g]"
	print "* Champion Greaves   (+50 Defense)  cost:[1750g]"   
	print "* Champion Gauntlets (+25 Defense)  cost:[750g]"  
	print "* Champion Boots     (+25 Defense)  cost:[750g]"
	print "* Champion Helmet    (+50 Defense)  cost:[1750g]"	
	print " "
	print "* Arch Mage Robe   (+50 Defense +50 Mana)  cost:[5000g]"
	print "* Arch Mage Pants  (+25 Defense +25 Mana)  cost:[1750g]"   
	print "* Arch Mage Gloves (+15 Defense +15 Mana)  cost:[750g]"  
	print "* Arch Mage Boots  (+15 Defense +15 Mana)  cost:[750g]"
	print "* Arch Mage Hood   (+25 Defense +25 Mana)  cost:[1750g]"
	print " " 
	print "-----------------------------------------------------"
	print "\n"
	print "Press 'b' to go back.\n"
	option = raw_input("> ")
	
## Buying Weapons
	if option == "1":
		if PlayerIG.gold >= 10:
			print "\nYou have bought 5 Arrows for 10 gold.\n"
			PlayerIG.gold -= 10
			PlayerIG.arrows += 5
			option = raw_input("")
			shop()
		else:
			print "\nYou don't have enough gold.\n"
			option = raw_input(" ")
			shop()
	
	if option == "2":
		if PlayerIG.gold >= 50:
			print "\nYou have bought 25 Arrows for 50 gold.\n"
			PlayerIG.gold -= 50
			PlayerIG.arrows += 25
			option = raw_input("")
			shop()
		else:
			print "\nYou don't have enough gold.\n"
			option = raw_input(" ")
			shop()
			
	if option == "3":
		if PlayerIG.gold >= 100:
			print "\nYou have bought 50 Arrows for 100 gold.\n"
			PlayerIG.gold -= 100
			PlayerIG.arrows += 50
			option = raw_input("")
			shop()
		else:
			print "\nYou don't have enough gold.\n"
			option = raw_input(" ")
			shop()
			
	if option in Weapons:
		if PlayerIG.gold >= Weapons[option]:
			PlayerIG.gold -= Weapons[option]
			PlayerIG.weaps.append(option)
			PlayerIG.inventory.append(option)
			print "You bought %s" % option
		else:
			print "You don't have enough gold"
	
	elif option in Bows:
		if PlayerIG.gold >= Bows[option]:
			PlayerIG.gold -= Bows[option]
			PlayerIG.bows.append(option)
			PlayerIG.inventory.append(option)
			print "You bought %s" % option
		else:
			print "You don't have enough gold"
		
	elif option in armH:
		if PlayerIG.gold >= armH[option]:
			PlayerIG.gold -= armH[option]
			PlayerIG.armsH.append(option)
			PlayerIG.inventory.append(option)
			print "You bought %s" % option
		else:
			print "You don't have enough gold"
	
	elif option in armB:
		if PlayerIG.gold >= armB[option]:
			PlayerIG.gold -= armB[option]
			PlayerIG.armsB.append(option)
			PlayerIG.inventory.append(option)
			print "You bought %s" % option
		else:
			print "You don't have enough gold"
	
	elif option in armA:
		if PlayerIG.gold >= armA[option]:
			PlayerIG.gold -= armA[option]
			PlayerIG.armsA.append(option)
			PlayerIG.inventory.append(option)
			print "You bought %s" % option
		else:
			print "You don't have enough gold"
	
	elif option in armL:
		if PlayerIG.gold >= armL[option]:
			PlayerIG.gold -= armL[option]
			PlayerIG.armsL.append(option)
			PlayerIG.inventory.append(option)
			print "You bought %s" % option
		else:
			print "You don't have enough gold"
	
	elif option in armF:
		if PlayerIG.gold >= armF[option]:
			PlayerIG.gold -= armF[option]
			PlayerIG.armsF.append(option)
			PlayerIG.inventory.append(option)
			print "You bought %s" % option
		else:
			print "You don't have enough gold"
	
	
	elif option == "b":
		start()
	
	else:
		print "This item doesn't exist"
	option = raw_input(" ")
	shop()


def stats():
	os.system('cls')
	print "==========================="
	print "=======Statistics:========="
	print "==========================="
	print " "
	print "Name: %s  Gold: %d  Health: %d" % (PlayerIG.name, PlayerIG.gold, PlayerIG.health)
	print "Exp: %d/%d   Potions: %d  Arrows: %d" % (PlayerIG.exp, PlayerIG.maxexp, PlayerIG.pots, PlayerIG.arrows) 
	print " "
	print "Attack Power: %s" % PlayerIG.stre
	print "Range Power: %s" % PlayerIG.rang
	print "Magic Power: %s" % PlayerIG.magi
	print "Defense: %s" % PlayerIG.defe
	print "Mana increase %s" % PlayerIG.mdefe
	print " "
	print "Equipped Weapon: %s" % PlayerIG.weap
	print " "
	print "Equipped Bow: %s" % PlayerIG.wbow
	print " "
	print "Armor: "
	print "Head: %s" % PlayerIG.armH
	print "Body: %s" % PlayerIG.armB
	print "Arms: %s" % PlayerIG.armA
	print "Legs: %s" % PlayerIG.armL
	print "Feet: %s" % PlayerIG.armF
	print " "
	print "Known spells:"
	for item in PlayerIG.spells:
		print item
	print " "
	print "Press any button to continue..."
	option = raw_input("> ")
	if option == "1":
		PlayerIG.weap = "None"
		start()
	else:
		start()

def fightmap():
	os.system('cls')
	print "\n"
	print "Where would you like to go?"
	print " "
	print "1.) Forest        (Level 1-5)"
	print "2.) Cave          (Level 6-10)" 
	print "3.) Mountains     (Level 11-15)"
	print "4.) Underworld    (Level 16-20)"
	print "5.) Realm of Zero (Level 21-24)"
	print "6.) Realm of Zero [~Vlokyrryn's Lair~] (Level 25)"
	print " "
	print "7.) Back"
	option = raw_input("> ")
	if option == "1":
		Forestprep()
	
	elif option == "2":
		if PlayerIG.level >= 6:
			Caveprep()
		else:
			print "\nYour level is not high enough to go here.\n"
			option = raw_input(" ")
			fightmap()
			
	elif option == "3":
		if PlayerIG.level >= 11:
			Mountprep()
		else:
			print "\nYour level is not high enough to go here.\n"
			option = raw_input(" ")
			fightmap()
	
	elif option == "4":
		if PlayerIG.level >= 16:
			UnderWprep()
		else:
			print "\nYour level is not high enough to go here.\n"
			option = raw_input(" ")
			fightmap()
	
	elif option == "5":
		if PlayerIG.level >= 21:
			RealmXeroprep()
		else:
			print "\nYour level is not high enough to go here.\n"
			option = raw_input(" ")
			fightmap()
	
	elif option == "6":
		if PlayerIG.level >= 25:
			Vlokyrrynprep()
		else:
			print "\nYour level is not high enough to go here.\n"
			option = raw_input(" ")
			fightmap()
	
	elif option == "7":
		start()
	
	else:
		print "There is no option for %s." % option
		option = raw_input(" ")
		fightmap()
		
def Caveprep():
	os.system('cls')
	enemynum = random.randint(1,6)
	global enemy
	if enemynum == 1 or enemynum == 3:
		enemy = TrollIG
	elif enemynum == 2 or enemynum == 4:
		enemy = StoneSerpeantIG
	elif enemynum == 5:
		enemy = GolemIG
	else:
		enemy = OrcIG
	
	print "\nAs you venture into the cave you encounter a %s\n" % enemy.name
	option = raw_input("Press any button to continue...")
	battle()
	
def UnderWprep():
	os.system('cls')
	enemynum = random.randint(1,8)
	global enemy
	if enemynum == 1 or enemynum == 3 or enemynum == 7:
		enemy = DemonIG
	elif enemynum == 2 or enemynum == 4:
		enemy = ChimeraIG
	elif enemynum == 5 or enemynum == 8:
		enemy = CerebrusIG
	else:
		enemy = HydraIG
	
	print "\nAs you venture through the depths of the Underworld, you encounter a %s\n" % enemy.name
	option = raw_input("Press any button to continue...")
	battle()
	
def RealmXeroprep():
	os.system('cls')
	enemynum = random.randint(1,8)
	global enemy
	if enemynum == 1 or enemynum == 3 or enemynum == 7:
		enemy = PhoenixIG
	elif enemynum == 2 or enemynum == 4:
		enemy = LeviathanIG
	elif enemynum == 5 or enemynum == 8:
		enemy = ScyllaIG
	else:
		enemy = CthuluIG
	
	print "\nAs you venture through the Realm of Xero you encounter a %s\n" % enemy.name
	option = raw_input("Press any button to continue...")
	battle()
	
def Vlokyrrynprep():
	os.system('cls')
	if PlayerIG.q19 == False:
		print "You must accept the quest 'Kill Vlokyrryn' before you can continue."
		option = raw_input(' ')
		fightmap()
	else:
		global enemy
		enemy = VlokyrrynIG
		print "\nYou finally find it, \'The Lair of %s\'" % enemy.name
		print "You stand there in awe until Vlokyrryn turns around and"
		print "launches at you for an attack."
		print " "
		option = raw_input("Press any button to continue...")
		battle()

def Mountprep():
	os.system('cls')
	enemynum = random.randint(1,6)
	global enemy
	if enemynum == 1 or enemynum == 3 or enemynum == 4:
		enemy = GriffonIG
	elif enemynum == 2 or enemynum == 5:
		enemy = BehemothIG
	else:
		enemy = DragonIG

	
	print "\nAs you venture into the cave you encounter a %s\n" % enemy.name
	option = raw_input("Press any button to continue...")
	battle()

def Forestprep():
	os.system('cls')
	enemynum = random.randint(1,7)
	global enemy
	if enemynum == 1 or enemynum == 2 or enemynum == 3 or enemynum == 4:
		enemy = GoblinIG
	elif enemynum == 5 or enemynum == 6:
		enemy = WolfIG
	else:
		enemy = GnollIG

	print "\nAs you are walking through the forest you encounter a %s.\n" % enemy.name
	option = raw_input("Press any button to continue...")
	battle()

# Combat System
def battle():
	os.system('cls')
	if MBurn == True:
		MBurnD = int(enemy.health * 0.1)
		print ("%s takes %s burn damage.") % (enemy.name, MBurnD)
		enemy.health -= MBurnD
		option = raw_input(" ")
	os.system('cls')
	magic = PlayerIG.magi
	if PlayerIG.health <= 0:
		dead()
	if PlayerIG.health > PlayerIG.maxhealth:
		PlayerIG.health = PlayerIG.maxhealth
	print "==========================="
	print "%s  vs  %s" % (PlayerIG.name, enemy.name)
	print "==========================="
	print " "
	print "Health:%d/%d  %s's Health:%d/%d" % (PlayerIG.health, PlayerIG.maxhealth, enemy.name, enemy.health, enemy.maxhealth)
	print "Mana:%d/%d   Potions:%d   Arrows:%d" % (PlayerIG.mana, PlayerIG.maxmana, PlayerIG.pots, PlayerIG.arrows)
	print " "
	print "1.) Melee Attack"
	print "2.) Ranged Attack"
	print "3.) Magic Attack"
	print "4.) Spells"
	print "5.) Drink Potion"
	print "6.) Run"
	option = raw_input("> ")

### Melee Attack ---------------------------------------------
	if option == "1":
		PAttack = random.randint(PlayerIG.stre-15, PlayerIG.stre) 
		EAttack = random.randint(0, enemy.attack) 
		
		if PAttack == PlayerIG.stre-15 or PAttack == 0:
			PAttack = 0
			print ("\nYou miss.\n")
			
		elif PAttack != PlayerIG.stre-15 and PAttack < 0:
			PAttack = 2
			enemy.health -= PAttack
			print ("\n%s takes %s melee damage.\n") % (enemy.name, PAttack)
			if enemy.health <= 0:
				option = raw_input(" ")
				win()
		else:
			print ("\n%s takes %s melee damage.\n") % (enemy.name, PAttack)
			enemy.health -= PAttack
			if enemy.health <= 0:
				option = raw_input(" ")
				win()
		
		if EAttack == 0:
			print ("%s misses.\n") % (enemy.name)
			
		else:
			print ("%s deals %d damage to %s.\n") % (enemy.name, EAttack, PlayerIG.name)
			PlayerIG.health -= EAttack
		option = raw_input("Press any button to continue...\n")
		battle()
		
### Range Attack ----------------------------------
	elif option == "2":
		if PlayerIG.wbow == "None":
			print "\nYou don't have a bow equipped.\n"
			option = raw_input(" ")
			battle()
		elif PlayerIG.arrows == 0:
			print "\nYou don't have any arrows.\n"
			option = raw_input(" ")
			battle()		
		else:
			PRange = random.randint(PlayerIG.rang-15, PlayerIG.rang) 
			EAttack = random.randint(0, enemy.attack) 
		
			if PRange == PlayerIG.rang-15 or PRange == 0:
				PlayerIG.arrows -= 1
				PRange = 0
				print ("\nYou miss.\n")
			
			else:
				print ("\nYou shoot an arrow at %s and takes %s ranged damage.\n") % (enemy.name, PRange)
				enemy.health -= PRange
				PlayerIG.arrows -= 1
				if enemy.health <= 0:
					option = raw_input(" ")
					win()
		
			if EAttack == 0:
				print ("%s misses.\n") % (enemy.name)
			
			else:
				print ("%s deals %d damage to %s.\n") % (enemy.name, EAttack, PlayerIG.name)
				PlayerIG.health -= EAttack
			option = raw_input("Press any button to continue...\n")
			battle()
		
## Magic Attack ---------------------------------------------
	elif option == "3":
		PAttack = random.randint(PlayerIG.magi-15, PlayerIG.magi)
		PAttack = int(PAttack * 0.7) 
		PMGain = int(PlayerIG.mana * 0.2)
		EAttack = random.randint(0, enemy.attack) 
		
		if PAttack == PlayerIG.magi-15 or PAttack == 0:
			PAttack = 0
			print ("\nYou miss.\n")
		
		elif PAttack != PlayerIG.magi-15 and PAttack < 0:
			if PlayerIG.mana == PlayerIG.maxmana:
				PMGain = 0
			if PlayerIG.mana > (PlayerIG.maxmana-20):
				PMGain = int(PlayerIG.maxmana - PlayerIG.mana) 
			PAttack = 1
			enemy.health -= PAttack
			print ("\n%s takes %s magic damage.") % (enemy.name, PAttack)
			print ("You have gained %s mana back.\n") % PMGain
			PlayerIG.mana += PMGain
			if enemy.health <= 0:
				option = raw_input(" ")
				win()
		
		else:
			if PlayerIG.mana == PlayerIG.maxmana:
				PMGain = 0
			if PlayerIG.mana > (PlayerIG.maxmana-20):
				PMGain = int(PlayerIG.maxmana - PlayerIG.mana) 
			print ("\n%s takes %s magic damage.") % (enemy.name, PAttack)
			print ("You have gained %s mana back.\n") % PMGain
			enemy.health -= PAttack
			PlayerIG.mana += PMGain
			if enemy.health <= 0:
				option = raw_input(" ")
				win()
		
		if EAttack == 0:
			print ("%s misses.\n") % (enemy.name)
			
		else:
			print ("%s deals %d damage to %s.\n") % (enemy.name, EAttack, PlayerIG.name)
			PlayerIG.health -= EAttack
		option = raw_input("Press any button to continue...\n")
		battle()

## Spells -------------------------------------
	
	elif option == "4":
		EAttack = random.randint(0, enemy.attack) 
		if PlayerIG.spells == []:
			print "You don't know any spells."
			option = raw_input("Press any button to continue...")
			battle()
		else:
			print "\nWhat spell do you wish to use?"
			print "(Type in the name of the spell you want to use.)\n"
			print "Known spells:"
			for item in PlayerIG.spells:
				print item
			print " "
			print "Press 'b' to go back."
			print " "
			option = raw_input("> ")
			
			# Spells #
			##### FIREBALL
			if option == "Fireball":
				if "Fireball" in PlayerIG.spells:
					if PlayerIG.mana >= 10:
						MagiAttack = random.randint(magic-15, magic+10)
						if MagiAttack < 0:
							MagiAttack = 1
						enemy.health -= MagiAttack
						print ("\nYou shoot the %s with a fiery missle dealing %s magic damage.\n") % (enemy.name, MagiAttack)
						PlayerIG.mana -= 10
					else:
						print "\nYou don't have enough mana.\n"
						option = raw_input(" ")
						battle()
					
					if enemy.health <= 0:
						option = raw_input(" ")
						win()
					else:
						if EAttack == 0:
							print ("%s misses.\n") % (enemy.name)
						else:
							print ("%s deals %d damage to %s.\n") % (enemy.name, EAttack, PlayerIG.name)
							PlayerIG.health -= EAttack
					option = raw_input("Press any button to continue...\n")
					battle()
				else:
					print "You don't know the spell \'Fireball\'."
					option = raw_input(" ")
					battle()
				##### LIGHTNING STRIKE
			if option == "Lightning Strike":
				if "Lightning Strike" in PlayerIG.spells:
					if PlayerIG.mana >= 20:
						MagiAttack = random.randint(magic-15, magic+25)
						if MagiAttack < 0:
							MagiAttack = 1
						enemy.health -= MagiAttack
						print ("\nYou summon a bolt of lightning that strikes %s dealing %s magic damage.\n") % (enemy.name, MagiAttack)
						PlayerIG.mana -= 10
					else:
						print "\nYou don't have enough mana.\n"
						option = raw_input(" ")
						battle()
					
					if enemy.health <= 0:
						option = raw_input(" ")
						win()
					else:
						if EAttack == 0:
							print ("%s misses.\n") % (enemy.name)
						else:
							print ("%s deals %d damage to %s.\n") % (enemy.name, EAttack, PlayerIG.name)
							PlayerIG.health -= EAttack
					option = raw_input("Press any button to continue...\n")
					battle()
				else:
					print "You don't know the spell \'Lightning Strike\'."
					option = raw_input(" ")
					battle()
					#### MAGIC MISSILE
			if option == "Magic Missile":
				if "Magic Missile" in PlayerIG.spells:
					if PlayerIG.mana >= 40:
						MagiAttack = random.randint(magic-15, magic+50)
						if MagiAttack < 0:
							MagiAttack = 1
						enemy.health -= MagiAttack
						print ("\nYou point your finger at %s, shooting a missile that deals %s magic damage.\n") % (enemy.name, MagiAttack)
						PlayerIG.mana -= 40
					else:
						print "\nYou don't have enough mana.\n"
						option = raw_input(" ")
						battle()
					
					if enemy.health <= 0:
						option = raw_input(" ")
						win()
					else:
						if EAttack == 0:
							print ("%s misses.\n") % (enemy.name)
						else:
							print ("%s deals %d damage to %s.\n") % (enemy.name, EAttack, PlayerIG.name)
							PlayerIG.health -= EAttack
					option = raw_input("Press any button to continue...\n")
					battle()
				else:
					print "You don't know the spell \'Magic Missile\'."
					option = raw_input(" ")
					battle()
					#### HELLISH SCALD
			if option == "Hellish Scald":
				if "Hellish Scald" in PlayerIG.spells:
					if PlayerIG.mana >= 60:
						MagiAttack = random.randint(magic-15, magic)
						MagiAttack *= 0.6
						if MagiAttack < 0:
							MagiAttack = 1
						enemy.health -= MagiAttack
						print "\nYou open your mouth breathing the steam from hell towards %s, burning %s's skin" % (enemy.name, enemy.name)
						print "and dealing %s magic damage.\n" % MagiAttack
						PlayerIG.mana -= 40
						global MBurn
						MBurn = True
					else:
						print "\nYou don't have enough mana.\n"
						option = raw_input(" ")
						battle()
					
					if enemy.health <= 0:
						option = raw_input(" ")
						win()
					else:
						if EAttack == 0:
							print ("%s misses.\n") % (enemy.name)
						else:
							print ("%s deals %d damage to %s.\n") % (enemy.name, EAttack, PlayerIG.name)
							PlayerIG.health -= EAttack
					option = raw_input("Press any button to continue...\n")
					battle()
				else:
					print "You don't know the spell \'Hellish Scald\'."
					option = raw_input(" ")
					battle()
				#### REJUVINATION
			if option == "Rejuvination":
				if "Rejuvination" in PlayerIG.spells:
					if PlayerIG.mana >= 50:
						MagiAttack = random.randint(magic-15, magic+50)
						print "You fill your hands with magic energy then touch your chest to heal your wounds.\n"
						PlayerIG.health += 100
						if PlayerIG.health > PlayerIG.maxhealth:
							PlayerIG.health = PlayerIG.maxhealth
						PlayerIG.mana -= 50
					else:
						print "\nYou don't have enough mana.\n"
						option = raw_input(" ")
						battle()
					if enemy.health <= 0:
						option = raw_input(" ")
						win()
					else:
						if EAttack == 0:
							print ("%s misses.\n") % (enemy.name)
						else:
							print ("%s deals %d damage to %s.\n") % (enemy.name, EAttack, PlayerIG.name)
							PlayerIG.health -= EAttack
					option = raw_input("Press any button to continue...\n")
					battle()
				else:
					print "You don't know the spell \'Rejuvination\'."
					option = raw_input(" ")
					battle()
				#### TSUANAMi
			if option == "Tsunami":
				if "Tsunami" in PlayerIG.spells:
					if PlayerIG.mana >= 180:
						MagiAttack = random.randint(magic+15, magic+500)
						if MagiAttack < 0:
							MagiAttack = 1
						enemy.health -= MagiAttack
						print "\nYou unfold a scroll and set it on the ground. Filling your hands with magic energy"
						print "you set your hands on the scroll unleasing a massive tsunami that crushes %s." % enemy.name
						print "and deals %s magic damage\n" % MagiAttack
						PlayerIG.mana -= 180
					else:
						print "\nYou don't have enough mana.\n"
						option = raw_input(" ")
						battle()
					
					if enemy.health <= 0:
						option = raw_input(" ")
						win()
					else:
						if EAttack == 0:
							print ("%s misses.\n") % (enemy.name)
						else:
							print ("%s deals %d damage to %s.\n") % (enemy.name, EAttack, PlayerIG.name)
							PlayerIG.health -= EAttack
					option = raw_input("Press any button to continue...\n")
					battle()
				else:
					print "You don't know the spell \'Tsunami\'."
					option = raw_input(" ")
					battle()
					#### GATES OF THE UNDERWORLD
			if option == "Gates of the Underworld":
				if "Gates of the Underworld" in PlayerIG.spells:
					if PlayerIG.mana >= 225:
						MagiAttack = random.randint(magic+15, magic+1000)
						if MagiAttack < 0:
							MagiAttack = 1
						enemy.health -= MagiAttack
						print "\nYou unfold a scroll and set it on the ground. Filling your hands with magic energy"
						print "you set your hands on the scroll  summoning  \'The Gates of the Underworld\'"
						print "out of the ground. As the ground starts to shake violently you looks at the gates"
						print "slowly start to open and then releases \'The Gate Guardian of the Underworld\' which attacks"
						print "%s and deals %s magic damage\n" % (enemy.name, MagiAttack)
						PlayerIG.mana -= 180
					else:
						print "\nYou don't have enough mana.\n"
						option = raw_input(" ")
						battle()
					
					if enemy.health <= 0:
						option = raw_input(" ")
						win()
					else:
						if EAttack == 0:
							print ("%s misses.\n") % (enemy.name)
						else:
							print ("%s deals %d damage to %s.\n") % (enemy.name, EAttack, PlayerIG.name)
							PlayerIG.health -= EAttack
					option = raw_input("Press any button to continue...\n")
					battle()
				else:
					print "You don't know the spell \'Gates of the Underworld\'."
					option = raw_input(" ")
					battle()
					#### WRATH OF GOD
			if option == "Wrath of God":
				if "Wrath of God" in PlayerIG.spells:
					if PlayerIG.mana >= 275:
						MagiAttack = 2000
						if MagiAttack < 0:
							MagiAttack = 1
						enemy.health -= MagiAttack
						print "You rip off the clothing covering your torso to reveal your chest"
						print "and then cast a rune on yourself. As %s starts to charge at you," % enemy.name
						print "you activate the rune turning yourself into a seemingly immortal monster."
						print "Using what magic power you can muster you rise up and smack down on %s" % enemy.name
						print "using the power of a god and deal %s magic damage. You lie on the ground" % MagiAttack
						print "feeling like you are about to die and look next to you at %s not sure if" % enemy.name
						print "%s is dead or alive. You then look at your body as you slowly start turning into ash\n" % enemy.name 
						PlayerIG.mana -= 180
						PlayerIG.health = 1
						if enemy.health <= 0:
							option = raw_input(" ")
							win()
						else:
							option = raw_input(' ')
							battle()
					else:
						print "\nYou don't have enough mana.\n"
						option = raw_input(" ")
						battle()
					
					if enemy.health <= 0:
						option = raw_input(" ")
						win()

				else:
					print "You don't know the spell \'Wrath of God\'."
					option = raw_input(" ")
					battle()
			
			
			elif option == 'b':
				battle()
			
			else:
				print "That spell doesn't exist"
				option = raw_input(" ")
				battle()
	
## Drink Potion
	elif option == "5":
		if PlayerIG.pots > 0:
			print "\nYou pull out and drink one of your potions "
			print "which heals you for up to 50 health.\n"
			option = raw_input("Press any button to continue...\n")
			PlayerIG.pots -= 1
			PlayerIG.health += 50
			battle()
		else:
			print "\nYou don't have any potion.\n"
			option = raw_input("Press any button to continue...\n")
			battle()
		
## Run Away
	elif option == "6":
		EAttack = random.randint(0, enemy.attack) 
		run = random.randint(1, 5)
		if run == 2:
			print "\nYou have successfully run away from %s!\n" % enemy.name
			option = raw_input("Press any button to continue...\n")
			enemy.health = enemy.maxhealth
			start()
		else:
			print "\nYou weren't able to get away from the %s." % enemy.name
			if EAttack == 0:
				print ("%s misses.\n") % (enemy.name)
			else:
				print ("%s deals %d damage to %s.\n") % (enemy.name, EAttack, PlayerIG.name)
				PlayerIG.health -= EAttack
			option = raw_input("Press any button to continue... \n")
			battle()
		enemy.health = enemy.maxhealth
	
	else:
		battle()


def endstory():
	print "--------================----------"
	print "        Congratulations!"
	print "--------================----------"
	print " "
	print """You have defeated Vlokyrryn and now Valkria may lay at ease
knowing that now monsters are no longer a threat to the kingdom. The king
grants you the \'Merit of Bravery\' to honor the defeat of Vlokyrryn and
promotes you to Jarl of Othendra and Captain of the Othendra guard. This
victory will lead you down the road of success in Kingdom Valkria. """
	print " "
	option = raw_input('Press any button to continue... ')
	start()



# Runs back to start() after the player defeats a monster in combat.
def win():
	os.system('cls')
	global MBurn
	MBurn = False
	if enemy == VlokyrrynIG:
		PlayerIG.qenemykillcount += 1
		endstory()
	else:
		print "\nCongratulations you killed the %s." % enemy.name
		print "You found %d gold." % enemy.goldgain
		print "You gain %d exp.\n" % enemy.expgain
		if enemy == OrcIG:
			specitem = random.randint(1, 3)
			if specitem == 2:
				PlayerIG.orichalcum += 1
				print "You have found orichalcum ore."
				print " "
			else:
				print "The Orc didn't have any orichalcum ore."
				print " "
		option = raw_input("Press any button to continue...\n")
		if enemy.name == PlayerIG.qenemy:
			PlayerIG.qenemykillcount += 1
		PlayerIG.gold += enemy.goldgain
		PlayerIG.exp += enemy.expgain
		enemy.health = enemy.maxhealth
		start()

# Runs when the player levels up
def levelup():
	os.system('cls')
	PlayerIG.level += 1
	PlayerIG.exp = 0
	PlayerIG.maxexp = PlayerIG.maxexp + PlayerIG.expdiff
	PlayerIG.expdiff += 50
	print "\nCongratulations you have leveled up!"
	print "You are now level %d.\n" % PlayerIG.level
	print "Your stats have improved"
	print " "
	option = raw_input(" ")
	levelup2()

def levelup2():
	print "Choose an attribute to increase:"
	print "1.) Health"
	print "2.) Mana"
	option = raw_input("> ")
	if option == "1":
		PlayerIG.maxhealth += 5
		print "\nYour Health has increased."
		levelup3()
	if option == "2":
		PlayerIG.base_mdefe += 5
		print "\nYour Mana has increased."
		levelup3()
	else:
		levelup2()

def levelup3():
	print " "
	print "Choose another attribute to increase:"
	print "1.) Attack Power"
	print "2.) Range Power"
	print "3.) Magic Power"
	option = raw_input("> ")
	if option == "1":
		PlayerIG.base_stre += 2
		print "\nYour Attack Power has increased."
	elif option == "2":
		PlayerIG.base_rang += 2
		print "\nYour Range Power has increased."
	elif option == "3":
		PlayerIG.base_magi += 2
		print "\nYour Magic Power has increased."
	else:
		levelup3()
	print " "
	option = raw_input("Press any button to continue...\n")
	start()

def healer():
	os.system('cls')
	print "\n"
	print "Healer: \"Hello what can I do for you?\""
	print " "
	print "Gold:%d" % PlayerIG.gold
	print " "
	print "1.) Heal my wounds"
	print "2.) Buy Potion (Gives user 50 health) costs 30 gold. "
	print "3.) Back"
	print "\n"
	option = raw_input("> ")
	
	if option == "1":
		print "\nYou have been healed.\n"
		PlayerIG.health = PlayerIG.maxhealth
		option = raw_input("Press any button to contine...\n")
		healer()
	elif option == "2":
		if PlayerIG.gold >= 30:
			print "\nBought potion with 30 gold.\n"
			PlayerIG.gold -= 30
			PlayerIG.pots += 1
			option = raw_input("Press any button to continue...\n")
			healer()
		else:
			print "\nYou don't have enough gold.\n"
			option = raw_input(" ")
			healer()
	elif option == "3":
		start()
	else:
		print ("\nThere was no option for %s.\n") % option
		option = raw_input("Press any button to continue...\n")
		healer()
		
		
def equip():
	os.system('cls')
	print "\nWhat would you like to equip?"
	print " "
	for item in PlayerIG.inventory:
		print item
	print " "
	print "Press 'b' to go back."
	print " "
	option = raw_input("> ")
	
	if option == 'b':
		inventory()
	
	if option == PlayerIG.weap or option == PlayerIG.wbow or option == PlayerIG.armH or option == PlayerIG.armB or option == PlayerIG.armL or option == PlayerIG.armA or option == PlayerIG.armF:
		print "%s is already equipped." % option
		
	elif option in PlayerIG.weaps:
		PlayerIG.weap = option
		print "You have equipped %s" % option

	elif option in PlayerIG.bows:
		PlayerIG.wbow = option
		print "You have equipped %s" % option

	elif option in PlayerIG.armsH:
		PlayerIG.armH = option
		print "You have equipped %s" % option
	
	elif option in PlayerIG.armsB:
		PlayerIG.armB = option 
		print "You have equipped %s" % option
	
	elif option in PlayerIG.armsL:
		PlayerIG.armL = option 
		print "You have equipped %s" % option
	
	elif option in PlayerIG.armsA:
		PlayerIG.armA = option 
		print "You have equipped %s" % option
	
	elif option in PlayerIG.armsF:
		PlayerIG.armF = option 
		print "You have equipped %s" % option

	else:
		print "\nYou don't have a %s.\n" % option
	option = raw_input(" " )
	equip()

def dead():
	 os.system('cls')
	 print "\nThe monsters have slain you..."
	 print "You lost half your gold, and are rushed to the healer."
	 print "Healer: \"You're lucky I was able to revive you.\"\n"
	 option = raw_input("Press any button to contine...")
	 PlayerIG.health = 1
	 PlayerIG.gold = int(PlayerIG.gold / 2)
	 enemy.health = enemy.maxhealth
	 start()


if __name__ == '__main__':
	start()




