import random # This is used to generate psudo-random numbers

print("Let's play a game. I'll pick a random number and you guess it! Don't worr,y I'll tell you if it's higher or lower to help youfind the answer. I'll pick a number between 1 and 100.")
number = random.randrange(1,100) # This is the generated number we need to guess.
guess = 0 # This is where we store the users guesses
attempts = 0 # This is the number of attempts before the answer was found

while guess != number:
    guess = int(input("Guess the number: ")) # We place the question here as it is in the loop, creating this above would prevent the user guessing again. Having it in both places will generate twice on the first run which looks bad and is redundant as it won't capture the attempt number if they guess it right.
    if guess > number:
        print("The number is lower than " + f'{guess}')
    elif guess < number: #else if (elif) is used instead of else to prevent this condition triggering when the correct number is guessed.
        print("The number is higher than " + f'{guess}') #f'{guess} is used to pass this number across.
    attempts = attempts + 1 # Increment the attempt counter by 1
print("Congrats! You guessed the correct number " + f'{number}' + " in " + f'{attempts}' + " attempts!")