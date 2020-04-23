import random

print("\tNUMBER GUESSING GAME\n")
while True:
	print("LEVELS")
	print("1. Easy")
	print("2. Medium")
	print("3. Hard")
	level = input("Enter a level: ")
	
	if level == "1":
		guess = " "
		print("\nEasy level\nChoose a number between 1 - 10")
		win = False
	if level == "2":
		guess = " "
		print("\nMedium level\nChoose a number between 1 - 20")
		win = False
	if level == "3":
		guess = " "
		print("\nHard level\nChoose a number between 1 - 50")
		win = False
			
	while True:
		if level == "1":
			guesses = 6
			number = random.randint(1,10)
		if level == "2":
			guesses = 4
			number = random.randint(1,20)
		if level == "3":
			guesses = 3
			number = random.randint(1,50)
		
		for i in range(guesses):
			guess = int(input("\nGuess the number, what is the number?\n"))
			if  guesses > 1:
				guesses -= 1
				if guess != number:
					print("That was wrong")
					print(guesses, "chances remaining")
				else:
					print("You got it right")
					print("Congratulation")
					break
			else:
				if guess != number:
					print("That was wrong")
					print("Sorry you didn't guess the number correctly, the number is", number)
					print("\nGAME OVER\n")
					break
				else:
					print("You got it right")
					print("Congratulation")
					break
		
		end = input("Do you want to continue playing this level? (y/n)\n")
		if end == "y":
			continue
		if end == "n":
			break
	print("\n\tNUMBER GUESSING GAME")
	quit = input("Do you wish to continue playing this game? (y/n)\n")
	if quit == "y":
		continue
	if quit == "n":
		print("\nThanks")
		break
			
