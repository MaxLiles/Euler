n1 = 1
n2 = 2
n3 = 0
answer = 2

while n3 < 4000000:
    n3 = n1 + n2
    if n3 % 2 == 0:
        answer += n3
    n1 = n2
    n2 = n3

print(answer)
    
