from pathlib import Path
from utils.statistics import calculate_average, find_min, find_max
from utils.reader import read_numbers

def main():
    input_file = Path("data") / "measurements.txt"

    print(Path.cwd())

    if not input_file.exists():
        print("не правильный путь", input_file)
        return

    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    numbers = read_numbers(input_file)

    if numbers is None:
        print("не удалось прочитать файл.")
        return

    if not numbers:
        print("числа отсутствуют")
        return

    srznach=calculate_average(numbers)
    minim=find_min(numbers)
    maxim=find_max(numbers)

    print(srznach)
    print(minim)
    print(maxim)

if __name__ == "__main__":
    main()
