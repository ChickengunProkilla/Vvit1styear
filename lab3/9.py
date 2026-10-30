numbers = [2, 6, 43, 16, 4, 8, 5]
def find_element(numbers, target):

    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1
print(find_element(numbers, 8), find_element(numbers, 55))