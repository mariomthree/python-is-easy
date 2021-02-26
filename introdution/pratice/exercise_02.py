from random import randint

guessesTaken = 0
myName = input('Hello! What is your name?\n')
number = randint(1, 20)
print('Well {}, I am thinking of a number between 1 and 20.'.format(myName))
while guessesTaken < 6:
    guess = int(input('Take a guess.\n'))
    guessesTaken += 1
    if guess < number:
        print('Your guess is too low.') # There are eight spaces in front of print.
    elif guess > number:
        print('Your guess is too high.')
    else:
        print('Good job, {}! You guessed my number in {} guesses!'.format(myName, guessesTaken))
        break