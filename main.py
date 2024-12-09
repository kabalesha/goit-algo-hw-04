from pathlib import Path


def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                total += int(salary)
                count += 1

        average = total / count if count > 0 else 0

        return total, average

    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0, 0
    except ValueError:
        print("Помилка в даних файлу. Переконайтеся, що зарплата є числом.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0

total, average = total_salary("Temp/salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")