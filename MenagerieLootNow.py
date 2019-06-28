from os import system, name
gloMasterwork = ''

def clear():
    # for windows
    if name == 'nt': 
        _ = system('cls')
    # for mac and linux
    else: 
        _ = system('clear')

def ninenine():
    

def calusMiniTool():
    global gloMasterwork
    print('''
Rune combination...

Slot 1 (Purple): Beast
Slot 2 (Purple): Any''')
    gloMasterwork = input('''
Would you like to select a specific Masterwork for your weapon?

Please chose 'y' or 'n': ''')
    if gloMasterwork == 'y' or gloMasterwork == 'Y':
        #chose masterwork for slot 3
    elif gloMasterwork == 'n' or gloMasterwork == 'N':
        print('Leave Slot 3 Empty')
        print('*********************')
    else:
        print('Sorry')

def subMGs():
    smgCAT01 = input('''Sub Machine Guns:

1 - CalusMiniTool
2 - TracklessWaste
3 - HardTruths
4 - BadReputation

99 - Return to Weapon Menu

Please pick a number from 1-4 / 99: ''')
    if smgCAT01 == '1':
        clear()
        calusMiniTool()

#1. --Sub MGs--
#CalusMiniTool
#TracklessWaste
#HardTruths
#BadReputation

#2. --Snipers--
#TwilightOath
#Beloved
#FateCriesFoul
#DreadedVenture

#3. --Rocket Launchers--
#BadOmens
#ZenobiaD
#Sleepless

#3.1 --Heavy MGs--
#FixedOdds

#4. --Hand Cannons--
#Trust
#Austringer
#WakingVigil
#PribinaD

#5. --Sidearms--
#DrangBaroque
#TheLastDance
#AnonymousAutumn
#SmugglersWord

#6. --Fusion Rifles--
#ProeliumFR3
#MainIngredient
#TheEpicurean
#ErentilFR4

#7. --Shotguns--
#Badlander
#ParcelOfStardust
#ImperialDecree
#DustRockBlues



def lootWeapons():
    cat01 = input('''Chalice of Opulence weapon loot pool:

1 - Sub MGs
2 - Snipers
3 - Rocket Launchers
3.1 - Heavy MGs
4 - Hand Cannons
5 - Sidearms
6 - Fusion Rifles
7 - Shotguns

99 - Return to Menu

Please pick a number from 1-7 / 99: ''')
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
        print('Invalid answer. Please try again.')
        clear()
        lootWeapons()


lootWeapons()

