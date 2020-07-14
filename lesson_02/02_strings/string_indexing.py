s = "BAD ASS string"

some_letter = s[0]  # 'B'
a_letter = s[2]     # 'D'
print(s[0], s[1])   # print BA
space_char = s[3]   # ' '

s[3] = 'F'          # type error!

print(s[15])        # index error!

last_char = s[-1]   # g
next_to_last = s[-2] # n
x = s[-20]          # index error!
