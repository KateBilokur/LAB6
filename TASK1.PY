def insert_after_element(user_list):
    try:
        element = input("Введіть елемент, після якого потрібно вставити новий: ")
        new_element = input("Введіть новий елемент для вставки: ")

        if element not in user_list:
            print("> Помилка: вказаного елемента немає в списку.")
            return user_list

        index = user_list.index(element)
        user_list.insert(index + 1, new_element)

        print("\n> Оновлений список після вставки:")
        print(user_list)
        return user_list
    except Exception as e:
        print(f"> Помилка: {e}")
        return user_list

# Функція для введення списку з клавіатури
def get_list_from_input():
    user_input = input("Введіть елементи списку через пробіл: ")
    return user_input.split()

# Основна частина для запуску функцій
print("\n\t\t<*> Операції над списками <*>")
user_list = get_list_from_input()
print("\n> Поточний список:")
print(user_list)

# Викликаємо функцію вставки
user_list = insert_after_element(user_list)
