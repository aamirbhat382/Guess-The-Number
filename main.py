Number_of_guesses = 1

while(Number_of_guesses <= 10):
    guess = int(input("Enter a number\n"))
    if guess < 10:
        print("You Enter A Less  Number")
    elif guess > 10:
        print("You Enter a big Number")
    else:
        print("You Won\n")
        break
    Number_of_guesses += 1

if Number_of_guesses > 10:
    print("Game Over")

