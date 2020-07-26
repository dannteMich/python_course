# first and last string
to_search = input("Please enter a string")

to_search_length = len(to_search)
if to_search[0] == to_search[to_search_length-1]:
    print("First and last characters are equal")
else:
    print("First and last characters are not the same")

# with negative indices
if to_search[0] == to_search[-1]:
    print("First and last characters are equal")
else:
    print("First and last characters are not the same")


#first 2 and last 2 with begative indices
to_search = input("Please enter a string")
if (to_search[0] == to_search[-1]) and (to_search[1] == to_search[-2]):
    print("Equal")
else:
    print("Not Equal")