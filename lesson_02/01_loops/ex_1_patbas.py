print("Please enter a 2-digit number")
number = int(input())

while number >= 100 or number < 10:
    print("This was not a 2-digit number. Please enter a 2-digit number")
    number_as_string = input()
    number = int(number_as_string)

print("Congrats dude, It's a 2-digit number!!!")