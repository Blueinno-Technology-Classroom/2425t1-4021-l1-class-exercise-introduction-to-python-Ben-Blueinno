age = int(input("type your age here: "))

# method 2
print(f'you wil be {2+age} years old 2 years later')

if age < 18:
    print("teen")
elif age < 65:
    print("adult")
else:
    print("elderly")
