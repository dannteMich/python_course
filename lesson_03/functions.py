n1 = int(input("Please enter first number: "))
n2 = int(input("Please enter second number: "))

if n1 > n2:
    print("The maximum is", n1)
else:
    print("The maximum is", n2)

def get_max(number1, number2):
    if number1 > number2:
        return number1
    else:
        return number2


