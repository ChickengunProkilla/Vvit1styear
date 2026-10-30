measurements = [16, 8, 71, 32, 9, 15, 59, 2, 36, 47]
def calculate_average(measurements):
    summ=0
    for i in range(len(measurements)):
        summ+=measurements[i]
    return summ
def find_minimum(measurements):
    minim=100
    for i in range(len(measurements)):
        if measurements[i]<minim:
            minim=measurements[i]
    return minim
def find_maximum(measurements):
    maxim=0
    for i in range(len(measurements)):
        if measurements[i]>maxim:
            maxim=measurements[i]
    return maxim
def count_above_average(measurements):
    srznach=calculate_average(measurements)
    ksz=0   #Kolichestvo Srednih Znacheniy
    for i in range(len(measurements)):
        if measurements[i]>srznach:
            ksz+=1
    return ksz
def find_value(measurements, target):
    for i in range(len(measurements)):
        if measurements[i] == target:
            return i
    return -1
def analyze_measurements(measurements):
    return (find_minimum(measurements), find_maximum(measurements), calculate_average(measurements))


minim, maxim, srznach=analyze_measurements(measurements)
print(calculate_average(measurements))
print(find_minimum(measurements))
print(find_maximum(measurements))
print(count_above_average(measurements))
print(find_value(measurements, 2))
print(analyze_measurements(measurements))
print(minim, maxim, srznach)
