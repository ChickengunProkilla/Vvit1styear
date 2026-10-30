
def greet(name):
    return("Здравствуйте,", name)
def square(number):
    return(number**2)
def max_of_two(a,b):
    if a>b:
        return a
    else:
        return b
print(greet('Ванек Толкократ'), greet('Святослав Староэуб'))
print(square(12), square(9))
print(max_of_two(19,91), max_of_two(59,25))
