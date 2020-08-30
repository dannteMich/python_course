break_point = int(input("When to break?"))

i = 0
while i < 100:
    
    if i % 7 == 0:
        continue
    
    if '7' in str(i):
        continue

    if i == break_point:
        break

    print(i)
    i += 1