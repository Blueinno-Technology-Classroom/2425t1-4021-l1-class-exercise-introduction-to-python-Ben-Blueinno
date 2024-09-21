import random

# print(random.randint(1, 100))
ans = random.randint(1, 100)
# print(ans)

res = input("guess a number from 1 to 100: ")
res = int(res)

max = 100
min = 1

while ans != res:
    if res >= 1 and res <= 100:
        if res > ans:
            max = res
            res = int(input(f'guess a number from {min} to {max}: '))
        elif res < ans:
            min = res
            res = int(input(f'guess a number from {min} to {max}: '))
    else:
        print('your respone is out of limit')
        
print('you got it')