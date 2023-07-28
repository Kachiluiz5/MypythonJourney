guess_number = 4
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Enter Guess: "))
    guess_count += 1
    if guess == guess_number:
        print("You Won")
        break
else:
    print("You loose")

