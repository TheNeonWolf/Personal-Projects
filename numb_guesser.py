import random

guesses = 0

number = random.randint(1,100)



while True:
    guess = input("Guess a number between 1 and 100: ")
    guess = int(guess)
    if guess < number:
        print("Too low")
        guesses +=1

    if guess > number:
        print("Too high")
        guesses +=1

    if guess == number:
        print(f"Correct! You took {guesses} guesses")
        break




