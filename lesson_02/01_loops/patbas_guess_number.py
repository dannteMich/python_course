chosen_number_as_string = input("Please select a number for the Player to guess: ")
chosen_number = int(chosen_number_as_string)

guess = int(input("Player, what is your guess? "))
while guess != chosen_number:
    if guess < chosen_number:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
    guess = int(input("Player, what is your guess? "))

print("Correct. It was", chosen_number)
