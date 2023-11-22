import random, time, math

settings = {
	"min": 0, # Default minimu
	"max": 10, # Default maximum
	"tries": 5, # Default maximum tries
	"caracters": 150 # Change this to adapt the maximal length of displayed messages
}

def displayMessage(message, returnToTheLine = False):
	if message:
		message = " " + message + " "
	if returnToTheLine:
		print('')
	numberOfStars = math.floor((settings["caracters"] - len(message)) / 2)
	for i in range(numberOfStars):
		print("*", end="")
	if message:
		print(message,end="")
	for i in range(numberOfStars):
		print("*", end="")
	print('')

displayMessage('', True)
displayMessage('randomNumberGame')
displayMessage('')

def showMenu(preChoice = 0, showMenuV = True):
	choice = 0
	if preChoice == 0:
		if showMenuV:
			displayMessage('MENU', True)
		displayMessage('')
		displayMessage('1 - Play | 2 - Settings | 3 - Credits | 4 - Exit')
		choice = displayInput()
		if isNumber(choice): choice = int(choice)
		else :
			print("⚠ [WARNING] - The number must be 1 or 2\n")
			return showMenu(0, False)
	if not preChoice == 2 and choice == 1:
		secretNumberGame(settings["min"],settings["max"])
	if choice == 2 or preChoice == 2:
		displayMessage("SETTINGS", True)
		displayMessage('1 - Minimum | 2 - Maximum | | 3 - Tries | 4 - Go Back')
		choice1 = displayInput()
		if choice1 == "1":
			newMin = input("New minimum: ")
			if isNumber(newMin): newMin = int(newMin)
			else:
				print("⚠ [WARNING] - Minimal value must be a number !\n")
				showMenu(2)
			if newMin < settings["max"]:	
				settings["min"] = newMin
			else:
				print("The minimum can't be bigger than the maximum !")
				showMenu(2)
				return
			showMenu()
		if choice1 == "2":
			newMax = input("New maximum: ")
			if isNumber(newMax): newMax = int(newMax)
			else:
				print("⚠ [WARNING] - Maximal value must be a number !\n")
				showMenu(2)
			if newMax > settings["min"]:
				settings["max"] = newMax
			else: 
				print("The maximum can't be smaller than the minimum !")
				showMenu(2)
				return
			showMenu()
		if choice1 == "3":
			newTriesMax = input("New tries maximum: ")
			if isNumber(newTriesMax): newTriesMax = int(newTriesMax)
			else:
				print("⚠ [WARNING] - Maximal tries value must be a number !\n")
				showMenu(2)
			if newTriesMax < 0:
				return print("⚠ [WARNING] - Maximal tries value can't be negative !\n")
			else:
				settings["tries"] = newTriesMax
				return showMenu()
		if choice1 == "4":
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
		if totalTries == settings["tries"]:
			print("\nYou used all your tries !...")
			return showMenu()

		n = input("\nYour choice: ")
		if n == "000":
			print("You gave up..")
			return showMenu()
		if isNumber(n): n = int(n)
		else:
			print("You choice wasn't a number !")
			return tryToGetTheNumber(totalTries)
		totalTries += 1
		if n == numberToFind:
			print("You won in",totalTries,"tries !")
			showMenu()
		else:
			print("You failed... try again (attempt",str(totalTries)+"/",str(settings["tries"])+") ! | Write '000' to give up...")
			if numberToFind > n: print("Tip: The number is bigger :)")
			elif numberToFind < n: print("Tip: The number is smaller :D")
			tryToGetTheNumber(totalTries)
	tryToGetTheNumber(totalTries)

def writeSlowly(message):
	for i in message:
		print(i, end = "")
		time.sleep(0.001)
	time.sleep(1)

def isNumber(string):
	if string[0] == '-':
		string = str(string).replace('-', '')
	return(string.isnumeric() == True)

def displayInput():
	return input('---> ')

showMenu()
