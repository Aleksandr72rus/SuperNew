# line1 = "Python"
# line2 = "Programming language"
# line3 = set(line1) & set(line2)    # {'o', 'n', 'P'}
# line_end = set(line1) - set(line3)
#
# print(line_end)

line1 = "Python"
line2 = "Programming language"
# line_end = set(line1) - (set(line1) & set(line2))

print(set(line1) - (set(line1) & set(line2)))
