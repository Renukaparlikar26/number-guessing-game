import random
com = random.randint(1, 100)
tries = 0

while True:
    hum = int(input("Guess a number between 1 and 100: "))
    tries = tries + 1
    if hum == com:
        print(f"Congratulations! You guessed the correct number in {tries} tries.")
        break
    elif hum > com:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.") 