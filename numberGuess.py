import random

print("Hello, Let's play a number guessing game. \n You got 7 chances to guess the number.  Let's go")

guessNumber = random.randrange(100)

userChances = 7

guesses = 0

while guesses < userChances:

    guesses += 1
    userGuess = int(input('Guess a number : '))

    if userGuess == guessNumber:
        print(f'The number is {guessNumber} You found it!! in the {guesses} attempt')
        break

    elif guesses >= userChances and guesses != guessNumber:
        print(f'Oops sorry, The number is {guessNumber} better luck next time')

    elif userGuess >= guessNumber:
        print('Your guess is too high')

    elif userChances <= guessNumber:
        print('Your guess is too low')


