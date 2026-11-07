import logging
from pathlib import Path
from utils.statistics import calculate_average, find_min, find_max, validate_numbers
from utils.reader import read_numbers

def setup_logging(log_file):
    """Настраивает запись сообщений в файл с датой, уровнем и текстом."""
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S", encoding="utf-8", force=True)

def main():
    input_file = Path("data") / "measurements.txt"

    # Каталог logs создаём до настройки логирования
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    log_file = logs_dir / "app.log"
    setup_logging(log_file)

    logging.info("Запуск программы")

    print(f"Текущий рабочий каталог: {Path.cwd()}")

    if not input_file.exists():
        logging.error("Файл не найден: %s", input_file)
        print(f"Файл не найден: {input_file}")
        logging.info("Завершение программы")
        return

    numbers = read_numbers(input_file)

    # read_numbers() вернул None — сработала обработка FileNotFoundError
    if numbers is None:
        logging.error("Не удалось прочитать файл: %s", input_file)
        print("Обработка прервана: не удалось прочитать файл.")
        logging.info("Завершение программы")
        return

    logging.info("Файл успешно прочитан: %s", input_file)
    logging.info("Количество прочитанных значений: %d", len(numbers))

    try:
        validate_numbers(numbers)
    except ValueError as error:
        logging.error("Ошибка валидации: %s", error)
        print(f"Ошибка валидации: {error}")
        logging.info("Завершение программы")
        return

    srznach=calculate_average(numbers)
    minim=find_min(numbers)
    maxim=find_max(numbers)

    print(srznach)
    print(minim)
    print(maxim)

    logging.info("Среднее: %.2f, минимум: %.2f, максимум: %.2f",
                 srznach, minim, maxim)
    logging.info("Завершение программы")

if __name__ == "__main__":
    main()
