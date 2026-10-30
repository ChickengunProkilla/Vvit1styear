numbers=[32,8,54,16,86,2,7]
def calculate_sum(numbers):
    suma= 0
    for i in range(len(numbers)):
        suma+=numbers[i]
    return suma
def find_min(numbers):
    minim=200
    for j in range(len(numbers)):
        if numbers[j] < minim:
            minim=numbers[j]
    return minim
def find_max(numbers):
    maxim=0
    for w in range(len(numbers)):
        if numbers[w] > maxim:
            maxim=numbers[w]
    return maxim
print(calculate_sum(numbers), find_min(numbers),find_max(numbers))
print(sum(numbers),min(numbers),max(numbers))