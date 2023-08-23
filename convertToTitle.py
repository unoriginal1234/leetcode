columnNumber = 701

# A should be zero
# Z should be 25

list = []
x = columnNumber

while x >= 1:
    y = x%26
    if y == 0:
        y = 26
    list.append(y)
    x = int((x - y)/26)

# char(65) = A
# So I need to add 64 to each int

ans = ""
while list:
    z = list.pop()
    ans = ans + chr(z + 64)

print(ans)
