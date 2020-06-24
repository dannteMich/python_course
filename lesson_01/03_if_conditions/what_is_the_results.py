x = -4

if x < 0:           # true
    x = x * 2       # x is -8
    x = x - 3       # x is -11
else:
    x = x + 1       # not hapenning
x = x * 10          # x is 110

print(x)

num1 = -34
num2 = 22

if num1 <= 0 and num2 <=0:  # false
    num1 = num1 * num2
else:
    num2 = num2 * 2         # num2 is 44

if num1 < 0:                # true
    num1 = num1 * -1        # num1 is 34
if num1 > num2:             # false
    num1 = num1 - num2
    num2 = num1
else:                       
    num1 = num1 + num2      # num1 is 78

if num2 < 0 or num1 > num2: # true
    num2 = num1 - 1         # num2 is 77
    num1 = 2 * num1         # num1 is 156
else:
    num1 = num2 - 1

print(num1)                 # 77
print(num2)                 # 156



