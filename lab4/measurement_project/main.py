from utils.statistics import calculate_average, find_min, find_max
from utils.reader import read_numbers

def main():
    numbers = read_numbers("data/measurements.txt")
    srznach=calculate_average(numbers)
    minim=find_min(numbers)
    maxim=find_max(numbers)

    print(srznach)
    print(minim)
    print(maxim)

if __name__ == "__main__":
    main()
