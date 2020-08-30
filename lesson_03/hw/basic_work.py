
def is_prime(num):
    if num <= 1:
        return False

    c = 2
    while c < num:
        if num % c == 0:
            return False

        c += 1
    
    return True
    

def print_prime_elements(num):
    if num < 2:
        print("There are no prime elements")
        return

    if is_prime(num):
        print(num, "is prime")
        return

    while not is_prime(num):
        
        e = 2
        while True:
            if num % e == 0 and is_prime(e):
                break
            e = e + 1

        print("element is", e)
        num = num // e

    print("last element is", num)


def max_number(a, b):
    if a > b:
        return a
    else:
        return b


def small_common_denominator(a, b):
    number = max_number(a, b)
    while number % a != 0 or number % b != 0:
        number = number + 1

    return number