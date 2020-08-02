long_string = input("please enter the long string: ")
short_string = input("please enter the short string to search in it: ")

if len(short_string) > len(long_string):
    print("Your short string is longer than the long string. Exiting")
    exit()

i = 0
starts_with = True
while i < len(short_string):
    
    if short_string[i] != long_string[i]:
        starts_with = False

    i = i + 1

if starts_with:
    print("YES!!!", long_string, "starts with", short_string)
else:
    print("NOOOOOOOOOOOOOOO!!!", long_string, "does not start with", short_string)
