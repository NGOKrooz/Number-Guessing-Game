import random

secret_number = random.randint(1,14)

guess = None
attempts = 0

while guess != secret_number:
   try:
        guess = int(input("Guess a number from 1-14 ?"))
        attempts += 1

        if guess > secret_number:
            print("Number is too high")
        elif guess < secret_number:
            print("Number is too small")
   except ValueError:
       print("Please enter a valid number")
else :
    print(f"Congratulations, You got it in {attempts} trials. ")