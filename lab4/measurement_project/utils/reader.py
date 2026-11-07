def read_numbers(file_path):
    numbers = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue
                try:
                    numbers.append(float(line))
                except ValueError:
                    print(line_number,"строка пропущена")
    except FileNotFoundError:
        print("файл не найден")
        return None
    return numbers
