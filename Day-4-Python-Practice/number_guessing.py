# Day 4 - Number Guessing Game

secret_number = 7

guess = int(input("Guess the number between 1 and 10: "))

if guess == secret_number:
    print("Congratulations! You guessed correctly.")
elif guess < secret_number:
    print("Too low!")
else:
    print("Too high!")

print("The secret number was:", secret_number)
