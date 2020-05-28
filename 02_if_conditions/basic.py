age = 34
inner_color = outer_color = color = "red" 

# basic
if age < 18:
    print("You are in school")


# another example
if age >= 65:
    print("Congrats man! You are risk for COVID-19")


# notice how I check equality.
if color == "green":
    print("You are a frog")


# complex conditions
if outer_color == "green" and inner_color == "red":
    print("you are a water melon")
    print ("Or maybe just a man painted in green")


# I can add parantheses for complex conditions to be clear
if (color == "green") or (color == "brown"):
    print("You might be a tree")
