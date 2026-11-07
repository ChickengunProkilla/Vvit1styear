import json
import logging
from pathlib import Path
from utils.statistics import calculate_average, find_min, find_max, validate_numbers
from utils.reader import read_numbers

from utils.statistics import (
    calculate_average,
    find_min,
    find_max,
    validate_numbers,
)
from utils.reader import read_numbers

CONFIG_PATH = Path("config.json")


def load_config(config_path):
    try:
        with open(config_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("файл конфигурации не найден", config_path)
        return None
    except json.JSONDecodeError as error:
        print("некорректный JSON", config_path, error)
        return None


def setup_logging(log_file):
    log_file.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        encoding="utf-8",
        force=True,
    )


def main():
    config = load_config(CONFIG_PATH)
    if config is None:
        return

    try:
        input_file = Path(config["input_file"])
        log_file = Path(config["log_file"])
    except KeyError as error:
        print("Ошибка конфигурации: отсутствует ключ", error)
        return

    setup_logging(log_file)
    logging.info("Запуск программы")

    print("Текущий рабочий каталог", Path.cwd())
    print(f"Входной файл", input_file)

    if not input_file.exists():
        logging.error("Файл не найден: %s", input_file)
        print("Файл не найден", input_file)
        logging.info("Завершение программы")
        return

    numbers = read_numbers(input_file)

    if numbers is None:
        logging.error("Не удалось прочитать файл: %s", input_file)
        print("Обработка прервана: не удалось прочитать файл.")
        logging.info("Завершение программы")
        return

    logging.info("Файл прочитан: %s", input_file)
    logging.info("Количество прочитанных значений: %d", len(numbers))

    try:
        validate_numbers(numbers)
    except ValueError as error:
        logging.error("Ошибка валидации: %s", error)
        print("Ошибка валидации", error)
        logging.info()
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
