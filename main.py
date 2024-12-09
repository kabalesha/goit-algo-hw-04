from pathlib import Path

# Task 1
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

# Task 2
def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cat_dict = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }
                cats_info.append(cat_dict)

        return cats_info

    except FileNotFoundError:
        print("Файл не знайдено.")
        return []
    except ValueError:
        print("Помилка в даних файлу. Переконайтеся, що кожен рядок містить id, name та age.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []


cats_info = get_cats_info("Temp/cats.txt")
print(cats_info)