basic_string = "hello world"
basic_string2 = 'hello world'

single_char = "h"

empty_s = ""

if 'h' == 'H':
    print("case insensitive")
else:
    print("case sensitive")

string_length = len(basic_string)  # 11

# concatination
first_s = "I am first"
second_s = "I am second"

final = first_s + second_s
print(final) # "I am firstI am Second"
fix_final = first_s + " " + second_s
print(fix_final) # "I am first I am Second"

# the in operator
sentence = "This is the end of the world as we know it" 
if 'n' in sentence:
    print("n in in the sentence")

if 'N' in sentence:
    print("n is also here")
else:
    print("N is in this sentence")

if "now" in sentence:   # True
    print("The sentence contains the now")

if "Now" in sentence:   # False
    print("Now is here")