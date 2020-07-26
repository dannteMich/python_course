# first and last string
to_search = input("Please enter a string: ")

to_search_length = len(to_search)
if len(to_search) < 1:
    print("this string is too shiort. Exiting")
    exit();

if to_search[0] == to_search[to_search_length-1]:
    print("First and last characters are equal")
else:
    print("First and last characters are not the same")

# with negative indices
if to_search[0] == to_search[-1]:
    print("First and last characters are equal")
else:
    print("First and last characters are not the same")


#first 2 and last 2 with negative indices
to_search = input("Please enter a string: ")
if len(to_search) < 3:
    print("this string is too shiort. Exiting")
    exit();

if (to_search[0] == to_search[-1]) and (to_search[1] == to_search[-2]):
    print("Equal")
else:
    print("Not Equal")


#is Polyndrom
to_search = input("Please enter a string to check if polyndrom: ")
is_polyndrom = True
str_length = len(to_search)
i = 0

while i < str_length:
    if to_search[i] != to_search[str_length-i-1]:
        is_polyndrom = False
    i = i + 1

if is_polyndrom:
    print("This is polyndrom!!!")
else:
    print("This is not a polyndrom")
