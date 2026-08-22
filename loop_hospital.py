# FIXED: range() stops before the ending number, so 11 is needed to include 10.
for i in range(1, 11):
    print(i)


# FIXED: n was never changed, causing an infinite loop; subtract 1 each time.
n = 3
while n > 0:
    print(n)
    n = n - 1


# FIXED: total was reset to 0 inside every loop; initialize it before the loop.
total = 0

for i in range(1, 6):
    total = total + i

print(total)
