
# check length of string
from_user = input("Please enter a string")
while len(from_user) < 6 or len(from_user) > 12:
    
    if len(from_user) < 6:
        print("String to short. Should be at least 6 characters")
    if len(from_user) > 12: # can this be 'else'?
        print("String to long. Should be no longer than 12 characters")

    from_user = input("Please enter a string")

print("your password is", from_user)


# count H or h  in string
from_user = input("Please enter a string: ")
count = 0
i = 0  # index
while (i < len(from_user)):
    if from_user[i] == 'h' or from_user[i] == 'H':
        count = count + 1

    i = i + 1

print("found", count, "times the letter H")


# check is H or h are in string
from_user = input("Please enter a string: ")
found = False
i = 0 # index
while i < len(from_user):
    if from_user[i] == 'h' or from_user[i] == 'H':
        found = True
    i = i + 1

if found:
    print("Found H")
else:
    print("didn't found H")

# check is H or h are in string with flag
from_user = input("Please enter a string: ")
found = False
i = 0  # index
while i < len(from_user) and not found:
    if from_user[i] == 'h' or from_user[i] == 'H':
        found = True
    i = i + 1

if found:
    print("Found H")
else:
    print("didn't found H")

# check is H or h are in string with break
from_user = input("Please enter a string: ")
found = False
i = 0  # index
while i < len(from_user):
    if from_user[i] == 'h' or from_user[i] == 'H':
        found = True
        break
    i = i + 1

if found:
    print("Found H")
else:
    print("didn't found H")

# check is H or h are in string with in
from_user = input("Please enter a string: ")
if 'h' in from_user or 'H' in from_user:
    print("Found H")
else:
    print("didn't found H")
