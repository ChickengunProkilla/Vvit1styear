numbers = [-10, 3, -2, 8, -5]
snumbers=sorted(numbers)
s2numbers=sorted(numbers, key=lambda x: abs(x))
print(snumbers)
print(s2numbers)