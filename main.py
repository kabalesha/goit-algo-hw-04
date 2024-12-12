from pathlib import Path

# Task 1
def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                total += float(salary)
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
print(f"Загальна сума заробітної плати: {total:.2f}, Середня заробітна плата: {average:.2f}")

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

# Task 4

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Usage: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Usage: change [name] [new phone]"
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command. Usage: phone [name]"
    name = args[0]
    return contacts.get(name, "Contact not found.")

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()