import random, time

print("\n\n***************************************************************")
print("********************** SecretNumberGame ***********************")
print("***************************************************************")

settings = {
	min: 0,
	max: 10
}

def showMenu(preChoice = 0, showMenuV = True):
	choice = 0
	if preChoice == 0:
		if showMenuV:
			print("\n************************* MENU ********************************")
		print("***************************************************************")
		print("****** 1 - Play | 2 - Settings | 3 - Credits | 4 - Exit *******")
		choice = input("--> ")
		if choice.isnumeric() == True: choice = int(choice)
		else :
			print("⚠ [WARNING] - The number must be 1 or 2\n")
			return showMenu(0, False)
	if not preChoice == 2 and choice == 1:
		secretNumberGame(settings[min],settings[max])
	if choice == 2 or preChoice == 2:
		print("\n************************* SETTINGS ****************************")
		print("********** 1 - Minimum | 2 - Maximum | 3 - Go Back ************")
		choice1 = int(input("--> "))
		if choice1 == 1:
			newMin = input("New minimum: ")
			if newMin.isnumeric() == True: newMin = int(newMin)
			else:
				print("⚠ [WARNING] - Minimal value must be a number !\n")
				showMenu(2)
			if newMin < settings[max]:	
				settings[min] = newMin
			else:
				print("The minimum can't be bigger than the maximum !")
				showMenu(2)
				return
			showMenu()
		if choice1 == 2:
			newMax = input("New maximum: ")
			if newMax.isnumeric() == True: newMax = int(newMax)
			else:
				print("⚠ [WARNING] - Maximal value must be a number !\n")
				showMenu(2)
			if newMax > settings[min]:
				settings[max] = newMax
			else: 
				print("The maximum can't be smaller than the minimum !")
				showMenu(2)
				return
			showMenu()
		if choice1 == 3:
			return showMenu()
		else:
			return showMenu(2)
	if choice == 3:
		message =  "\n***************************************************************\n"
		message +=  "********** Made by Nostlix (https://github.com/Nostlix) *******\n"
		message +=  "*** Repository: https://github.com/Nostlix/randomNumberGame ***\n"
		message +=  "***************************************************************\n"
		writeSlowly(message)
		return showMenu()
	if choice == 4:
		message =  "\n***************************************************************\n"
		message += "***************** Thanks for playing ! ❤  ❤  ❤ ****************\n"
		message +=  "***************************************************************"
		writeSlowly(message)
		exit()
	else:
		showMenu()


def secretNumberGame(min, max):
	numberToFind = random.randint(min , max)
	print("\nThe number is between",min,"and", max, "!")
	totalTries = 0

	def tryToGetTheNumber(totalTries):
		n = input("\nYour choice: ")
		if n == "000":
			print("You gave up..")
			return showMenu()
		if n.isnumeric() == True: n = int(n)
		else:
			print("You choice wasn't a number !")
			return tryToGetTheNumber(totalTries)
		totalTries += 1
		if n == numberToFind:
			print("You won in",totalTries,"tries !")
			showMenu()
		else:
			print("You failed... try again (attempt",str(totalTries)+") ! | Write '000' to give up...")
			if numberToFind > n: print("Tip: The number is bigger :)")
			elif numberToFind < n: print("Tip: The number is smaller :D")
			tryToGetTheNumber(totalTries)
	tryToGetTheNumber(totalTries)

def writeSlowly(message):
	for i in message:
		print(i, end = "")
		time.sleep(0.001)
	time.sleep(1)

showMenu()
