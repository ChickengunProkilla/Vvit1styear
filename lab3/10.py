numbers = [2, 6, 43, 16, 4, 8, 5]
def analyze(numbers):
    minim=100
    maxim=0
    for i in range(len(numbers)):
        if numbers[i]<minim:
            minim=numbers[i]
        if numbers[i]>maxim:
            maxim=numbers[i]
    srznach=(sum(numbers)/len(numbers))
    return minim, maxim, srznach
mn, mx, srz=analyze(numbers)
print(analyze(numbers))
print(mn, mx, srz)