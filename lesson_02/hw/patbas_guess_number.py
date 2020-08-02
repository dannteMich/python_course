
print("Casino user - you're up: What is the target number?")
target_number = int(input())

print("Player - time to play. What is you'r guess?")
guess = int(input())

while guess != target_number:
    if guess < target_number:
        print("The target number is bigger. ")
    else:
        print("The target number is smaller. ")

    guess = int(input("what is your next guess"))

print("Correct! the number is", target_number)