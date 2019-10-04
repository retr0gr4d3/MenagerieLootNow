from os import system, name
import time

# SO FAR, WHOLE COMPLETED SEGMENTS ARE: SUB MGs, SNIPERS, ROCKET LAUNCHERS AND HEAVY MGs.

# DEFINED EXTRAS - CLEARING OUTPUT AND ERROR MESSAGE

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

def invalidAnswer():
	print('Invalid answer. Please try again.')
	time.sleep(1)
	clear()

# HEAVY MACHINE GUNS

def heavyMGs():
	heavyCAT01 = input("Heavy Machine Guns:\n1 - Fixed Odds\n99 - Return to Weapon Menu\nPlease pick a number from 1 / 99: ")
	if heavyCAT01 == '1':
		clear()
		fixedOdds()
	elif heavyCAT01 == '99':
		clear()
		lootWeapons()
	else:
		clear()
		invalidAnswer()
		heavyMGs()

def fixedOdds():
	returnToMenu = input("Rune combination...\nSlot 1 (Red): Ambition\nSlot 2 (Blue): Any\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		heavyMGs()
	else:
		clear()
		invalidAnswer()
		fixedOdds()

# ROCKET LAUNCHERS

def rocketLaunchers():
	rocketCAT01 = input("Rocket Launchers:\n1 - Bad Omens\n2 - Zenobia-D\n3 - Sleepless\n99 - Return to Weapon Menu\nPlease pick a number from 1-3 / 99: ")
	if rocketCAT01 == '1':
		clear()
		badOmens()
	if rocketCAT01 == '2':
		clear()
		zenobiaD()
	if rocketCAT01 == '3':
		clear()
		Sleepless()
	if rocketCAT01 == '4':
		clear()
		dreadedVenture()
	elif rocketCAT01 == '99':
		clear()
		lootWeapons()
	else:
		clear()
		invalidAnswer()
		rocketLaunchers()

def badOmens():
	returnToMenu = input("Rune combination...\nSlot 1 (Red): Ambition\nSlot 2 (Purple): Any\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		rocketLaunchers()
	else:
		clear()
		invalidAnswer()
		badOmens()

def zenobiaD():
	returnToMenu = input("Rune combination...\nSlot 1 (Red): Ambition\nSlot 2 (Red): Any\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		rocketLaunchers()
	else:
		clear()
		invalidAnswer()
		zenobiaD()

def Sleepless():
	returnToMenu = input("Rune combination...\nSlot 1 (Red): Ambition\nSlot 2 (Green): Any\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		rocketLaunchers()
	else:
		clear()
		invalidAnswer()
		Sleepless()

# SNIPERS

def snipers():
	snipersCAT01 = input("Snipers:\n1 - Twilight Oath\n2 - Beloved\n3 - Fate Cries Fowl\n4 - Dreaded Venture\n99 - Return to Weapon Menu\nPlease pick a number from 1-4 / 99: ")
	if snipersCAT01 == '1':
		clear()
		twilightOath()
	if snipersCAT01 == '2':
		clear()
		beloved()
	if snipersCAT01 == '3':
		clear()
		fateCriesFowl()
	if snipersCAT01 == '4':
		clear()
		dreadedVenture()
	elif snipersCAT01 == '99':
		clear()
		lootWeapons()
	else:
		clear()
		invalidAnswer()
		snipers()

def twilightOath():
	returnToMenu = input("Rune combination...\nSlot 1 (Purple): Jubilation\nSlot 2 (Purple): Any\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		snipers()
	else:
		clear()
		invalidAnswer()
		twilightOath()

def beloved():
	returnToMenu = input("Rune combination...\nSlot 1 (Purple): Jubilation\nSlot 2 (Red): Any\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		snipers()
	else:
		clear()
		invalidAnswer()
		beloved()

def fateCriesFowl():
	returnToMenu = input("Rune combination...\nSlot 1 (Purple): Jubilation\nSlot 2 (Green): Any\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		snipers()
	else:
		clear()
		invalidAnswer()
		fateCriesFowl()

def dreadedVenture():
	returnToMenu = input("Rune combination...\nSlot 1 (Purple): Jubilation\nSlot 2 (Purple): Any\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		snipers()
	else:
		clear()
		invalidAnswer()
		dreadedVenture()

# SUB MACHINE GUNS

def subMGs():
	smgCAT01 = input("Sub Machine Guns:\n1 - CalusMiniTool\n2 - TracklessWaste\n3 - HardTruths\n4 - BadReputation\n99 - Return to Weapon Menu\nPlease pick a number from 1-4 / 99: ")
	if smgCAT01 == '1':
		clear()
		calusMiniTool()
	if smgCAT01 == '2':
		clear()
		tracklessWaste()
	if smgCAT01 == '3':
		clear()
		hardTruths()
	if smgCAT01 == '4':
		clear()
		badReputation()
	elif smgCAT01 == '99':
		clear()
		lootWeapons()
	else:
		clear()
		invalidAnswer()
		subMGs()

def calusMiniTool():
	returnToMenu = input("Rune combination...\nSlot 1 (Purple): Beast\nSlot 2 (Purple): Any\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		subMGs()
	else:
		clear()
		invalidAnswer()
		calusMiniTool()

def tracklessWaste():
	returnToMenu = input("Rune combination...\nSlot 1 (Purple): Beast\nSlot 2 (Red): Any\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		subMGs()
	else:
		clear()
		invalidAnswer()
		tracklessWaste()

def hardTruths():
	returnToMenu = input("Rune combination...\nSlot 1 (Purple): Beast\nSlot 2 (Green): Any\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		subMGs()
	else:
		clear()
		invalidAnswer()
		hardTruths()

def badReputation():
	returnToMenu = input("Rune combination...\nSlot 1 (Purple): Beast\nSlot 2 (Purple): Any\nPress 99 to return to subsection selection: ")
	if returnToMenu == '99':
		clear()
		subMGs()
	else:
		clear()
		invalidAnswer()
		badReputation()

# THE MAIN MENUS

def lootWeapons():
	clear()
	cat01 = input("Chalice of Opulence weapon loot pool:\n1 - Sub MGs\n2 - Snipers\n3 - Rocket Launchers\n3.1 - Heavy MGs\n4 - Hand Cannons\n5 - Sidearms\n6 - Fusion Rifles\n7 - Shotguns\n99 - Return to Menu\nPlease pick a number from 1-7 / 99: ")
	if cat01 == '1':
		clear()
		subMGs()
	elif cat01 == '2':
		clear()
		snipers()
	elif cat01 == '3':
		clear()
		rocketLaunchers()
	elif cat01 == '3.1':
		clear()
		heavyMGs()
	elif cat01 == '4':
		clear()
		handCannons()
	elif cat01 == '5':
		clear()
		sidearms()
	elif cat01 == '6':
		clear()
		fusionRifles()
	elif cat01 == '7':
		clear()
		shotguns()
	elif cat01 == '99':
		clear()
		mainMenu()
	else:
		clear()
		invalidAnswer()
		lootWeapons()

def mainMenu():
	clear()
	cat01 = input("Hi User. Welcome to MenagerieLootNow. Please select one of the following.\n1 - Weapons\n2 - Armour\nChoice: ")
	if cat01 == '1':
		clear()
		lootWeapons()
	elif cat01 == '2':
		clear()
		lootArmour()
	else:
		clear()
		invalidAnswer()
		mainMenu()

mainMenu()