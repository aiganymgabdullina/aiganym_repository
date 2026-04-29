my_list = ["task1", "task2", "task3", "task4"]
def show_list():
    if not my_list:
        print("Список пуст")
        return
    print("\nТекущий список:")
    for i, item in enumerate(my_list):
        print(f"{i}: {item}")

def delete_by_index():
    show_list()
    if not my_list:
        return
    try:
        index = int(input("Choose the index to delete : "))
        removed = my_list.pop(index)
        print(f"Удалён элемент: {removed}")
    except ValueError:
        print("Error: введи число")
    except IndexError:
        print("Ошибка: такого индекса нет")

while True:
    print("1 — show the list")
    print("2 — delete the task")
    print("0 — Выход")

    choice = input("Choose: ")

    if choice == "1":
        show_list()
    elif choice == "2":
        delete_by_index()
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Error")