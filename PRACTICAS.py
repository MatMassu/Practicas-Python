
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# name = input("Please enter the name: ")
# age = int(input("Please enter the age: "))

# import datetime
# now = datetime.datetime.now()

# year = 100 - age + now.year

# print(name, 'will turn 100 years old in the year', year)


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

# num = int(input('Please enter a number: '))

# if num % 2 == 0 and num % 4 != 0:
#     print ('The number', num, 'is even.')
# elif num % 2 == 0 and num % 4 == 0:
#     print ('The number', num, 'is even and also a multiple of 4.') 
# else: 
#     print ('The number', num, 'is odd.')


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Take a list and write a program that prints out all the elements of the list that are less than a chosen number.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# num = int(input('Please enter a number: '))
# print ([x for x in a if x < num]) 


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

# num = int(input('Please enter a number: '))
 
# listRange = list(range(1, num + 1))

# divList = []

# for x in listRange:
#     if num % x == 0:
#         divList.append(x)

# print('The divisors for', num, 'are:', divList)


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Take two randomly generated lists of different sizes and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 

# import random 

# randList1 = random.sample(range(0, 20), 15)
# randList2 = random.sample(range(0, 20), 12)

# sameNum = []

# for a in randList1:
#     if a in randList2 and a not in sameNum:
#         sameNum.append(a)

# print(sameNum)


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Write one line of Python that takes this list a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] and makes a new list that has only the even elements of this list in it.

# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# evenList = [x for x in a if x % 2 == 0]

# print(evenList)


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Make a two-player Rock-Paper-Scissors game. Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players 
# want to start a new game.

# p1 = input('Welcome to Rock-Paper-Scissors! Player 1, please type your name: ')
# p2 = input('Player 2, please type your name: ')

# def p1Endgame():
#     p1Answer = input(p1, 'wins! Do you want to play again? (y/n): ')
#     if p1Answer == 'y':
#         game = 1
#     else: break

# def p2Endgame():
#     p2Answer = input(p2, 'wins! Do you want to play again? (y/n): ')
#     if p2Answer == 'y':
#         game = 1
#     else: break

# def drawEndgame():
#     p1Answer = input("It's a draw! Do you want to play again? (y/n): ")
#     if p1Answer == 'y':
#         game = 1
#     else: break

# game = 1
# while game == 1:

#     p1Select = input(p1, ', please enter your play: ') = p1Select.lower
#     p2Select = input(p2, ', please enter your play: ') = p2Select.lower
 
#     if p1Select == 'rock' and p2Select == 'scissors':
#         p1Endgame()
#     elif p1Select == 'scissors' and p2Select == 'paper':
#         p1Endgame()
#     elif p1Select == 'paper' and p2Select == 'rock':
#         p1Endgame()
#     elif p2Select == 'rock' and p1Select == 'scissors':
#         p2Endgame()
#     elif p2Select == 'scissors' and p1Select == 'paper':
#         p2Endgame()
#     elif p2Select == 'paper' and p1Select == 'scissors':
#         p2Endgame()
#     else: drawEndgame()
# else:
#     print('Game over!')


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

# import random

# num = random.randint(1,9)

# # (VALIDATION)
# # while True:
# #     try:
# #         guess = int(input('Guess a number between 1 and 9: '))
# #     except ValueError:
# #         print("This is not a whole number. Try again!")
# #         continue
# #     else: break 

# guess = 0
# att = 0

# while guess != num and guess != 'q':
#     guess = input('Guess a number between 1 and 9: ')

#     if guess == 'q':
#         print('Goodbye!')
#         break

#     guess = int(guess)
#     att += 1

#     if guess < num and range(num-10):
#         print('You guessed too low! Try again: ')
#     elif guess > num:
#         print('You guessed too high! Try again: ')
#     else:
#         print('You got it! It took you', att, 'tries.')


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

