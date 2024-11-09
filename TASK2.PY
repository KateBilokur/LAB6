def quick_sort(array):
    # Базовий випадок: масив з 1 елемента або порожній уже відсортований
    if len(array) <= 1:
        return array
    else:
        # Вибір опорного елемента
        pivot = array[0]

        # Поділ на підмасиви менших та більших елементів відносно опорного
        less_than_pivot = [x for x in array[1:] if x <= pivot]
        greater_than_pivot = [x for x in array[1:] if x > pivot]

        # Рекурсивне сортування підмасивів та об'єднання з опорним елементом
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Функція для введення списку з клавіатури
def get_list_from_input():
    user_input = input("Введіть елементи списку через пробіл: ")
    return user_input.split()

# Основна частина для запуску функцій
print("\n\t\t<*> Швидке сортування списку <*>")
user_list = get_list_from_input()

# Перетворення елементів на числа, якщо це можливо
try:
    user_list = [int(x) if x.isdigit() else x for x in user_list]
except ValueError:
    print("> Помилка: список містить елементи, які не є числами.")
    user_list = [str(x) for x in user_list]  # Конвертуємо всі елементи у строки у випадку помилки

# Викликаємо функцію швидкого сортування та виводимо результат
sorted_list = quick_sort(user_list)
print("\n> Відсортований список:")
print(sorted_list)
