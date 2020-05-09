import os
import sys, traceback

if name == 'nt':
	print("User is on Windows.")
else:
	if os.getuid() != 0:
	print('''You are running in an unprivileged
userspace. This is good.''')
	elif os.getuid() == 0:
		print('''\033[1;91mDo not run this application with
sudo privileges. This is to
protect you, the end user, from
any possible damage caused by
tampered code.\033[1;m''')
		sys.exit()

def main():
	try:
		print('''
\033[1;36m __  __      _          _   _   
|  \/  |    | |        | \ | |  
| |\/| |    | |        |  \| |  
| |  | | _  | |___  _  | |\  | _ 
| |  |_|(_) |_____|(_) |_| | |(_)
\_|                        |_/
\033[1;m
+-------------------------------+
|    Menagerie   Loot   Now     |
+-------------------------------+
\033[1;32m
+ -- -- +=[Author: Retr0gr4d3]
[Built, tested and ran on Python]
\033[1;m \033[1;91m
[INFO] This is still in early
development. If you encounter a
bug, please open up an issue on
GitHub.
\033[1;m
			''')
		def decision1():
			while True:
				print('''
1) Menagerie Weapons
2) Menagerie Armor
					''')
				option0 = input("\033[1;36mM. L. N. > \033[1;m")
				while option0 == "1":
					print('''
1) Machine Guns
2) Sub Machine Guns
3) Sniper Rifles
4) Rocket Launchers
5) Hand Cannons
6) Sidearms
7) Fusion Rifles
8) Shotguns

99) Return to main menu
						''')
					weapon = input("\033[1;32mSelect a category > \033[1;m")
					if weapon == "1":
						print('''
1) Fixed Odds

99) Go back
							''')
						heavyMG = input("\033[1;32mSelect a weapon > \033[1;m")
						if heavyMG == "1":
							print("\033[1;91mRune combination...\nSlot 1 - Rune of Ambition (RED)\nSlot 2 - Any rune (BLUE)")
							end = input("\033[1;32mPress [ENTER] to continue > \033[1;m")
						elif heavyMG == "99":
							decision1()
						else:
							print("\033[1;31mSorry, that was an invalid command!\033[1;m")
					elif weapon == "2":
						print('''
1) RTM
							''')
						subMG = input("Coming soon > ")
						if heavyMG == "1":
							decision1()
						else:
							print("Enter command [1] to continue")
					elif weapon == "3":
						print('''
1) RTM
							''')
						sniper = input("Coming soon > ")
						if sniper == "1":
							decision1()
						else:
							print("Enter command [1] to continue")
					elif weapon == "4":
						print('''
1) RTM
							''')
						rocket = input("Coming soon > ")
						if rocket == "1":
							decision1()
						else:
							print("Enter command [1] to continue")
					elif weapon == "5":
						print('''
1) RTM
							''')
						handCannon = input("Coming soon > ")
						if handCannon == "1":
							decision1()
						else:
							print("Enter command [1] to continue")
					elif weapon == "6":
						print('''
1) RTM
							''')
						sidearm = input("Coming soon > ")
						if sidearm == "1":
							decision1()
						else:
							print("Enter command [1] to continue")
					elif weapon == "7":
						print('''
1) RTM
							''')
						fusion = input("Coming soon > ")
						if fusion == "1":
							decision1()
						else:
							print("Enter command [1] to continue")
					elif weapon == "8":
						print('''
1) RTM
							''')
						shotgun = input("Coming soon > ")
						if shotgun == "1":
							decision1()
						else:
							print("Enter command [1] to continue")
					elif weapon == "99":
						main()
					else:
						print("Sorry! That was an invalid command.")
				while option0 == "2":
					print("Armor coming soon")
					rtm = input("Press [ENTER] to return home. > ")
					main()
		decision1()

	except KeyboardInterrupt:
		print('''

Thanks for using Menagerie Loot Now!
''')

	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

main()
