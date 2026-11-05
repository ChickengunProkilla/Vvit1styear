from utils.statistics import calculate_average, find_min, find_max
def main():
    numbers=[87, 3, 53, 13, 154, 11, 21, 76]
    srznach=calculate_average(numbers)
    minim=find_min(numbers)
    maxim=find_max(numbers)
    print(srznach)
    print(minim)
    print(maxim)


if __name__ == "__main__":
    main()
