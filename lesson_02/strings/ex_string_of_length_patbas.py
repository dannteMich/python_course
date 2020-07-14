
from_user = input("Please enter a string")
while len(from_user) < 6 or len(from_user) > 12:
    
    if len(from_user) < 6:
        print("String to short. Should be at least 6 characters")
    if len(from_user) > 12: # can this be 'else'?
        print("String to long. Should be no longer than 12 characters")

    from_user = input("Please enter a string")

print("your password is", from_user)
