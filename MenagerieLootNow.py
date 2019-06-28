1. --Sub MGs--
CalusMiniTool
TracklessWaste
HardTruths
BadReputation

2. --Snipers--
TwilightOath
Beloved
FateCriesFoul
DreadedVenture

3. --Rocket Launchers--
BadOmens
ZenobiaD
Sleepless

3.1 --Heavy MGs--
FixedOdds

4. --Hand Cannons--
Trust
Austringer
WakingVigil
PribinaD

5. --Sidearms--
DrangBaroque
TheLastDance
AnonymousAutumn
SmugglersWord

6. --Fusion Rifles--
ProeliumFR3
MainIngredient
TheEpicurean
ErentilFR4

7. --Shotguns--
Badlander
ParcelOfStardust
ImperialDecree
DustRockBlues



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
        subMGs()
    elif cat01 == '2':
        snipers()
    elif cat01 == '3':
        rocketLaunchers()
    elif cat01 == '3.1':
        heavyMGs()
    elif cat01 == '4':
        handCannons()
    elif cat01 == '5':
        sidearms()
    elif cat01 == '6':
        fusionRifles()
    elif cat01 == '7':
        shotguns()
    elif cat01 == '99':
        mainMenu()

    else:
        print('Invalid answer. Please try again.')
        lootWeapons()
