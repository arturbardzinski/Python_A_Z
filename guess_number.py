from random import randint

number = randint(1, 10)

guess = None
attempt = 0
while number != guess:
    guess = int(input("Your number: "))
    attempt += 1
    if guess == number:
        print(f"You win!!! Your guess in {attempt} attempt")
    elif guess < number:
        print("To low\n")
    elif guess > number:
        print("To high\n")
