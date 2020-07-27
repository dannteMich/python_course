print("What is your paragraph or string: ")
corpus = input()

print("What letter would you like me to search in there? ")
letter = input()
while len(letter) != 1:
    print("This is not a letter. please input one letter")
    letter = input()

i = 0
count = 0
while i < len(corpus):
    if corpus[i] == letter:
        count = count + 1
    i = i + 1

print("The letter was found", count, "times in the text.")