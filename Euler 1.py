result = 0

for n in range (0,1000):
    if n % 3 == 0:
        result += n
    elif n % 5== 0:
        result += n

print(result)
