def is_fibonacci(n):
    # Функція, щоб перевірити, чи є число n числом Фібоначчі
    if n < 1:
        return False
    a, b = 0, 1
    while b <= n:
        if b == n:
            return True
        a, b = b, a + b
    return False

def count_fibonacci_in_set(num_set):
    # Створюємо список чисел Фібоначчі до максимального значення в num_set
    fibonacci_numbers = set()
    a, b = 0, 1
    while b <= max(num_set):
        if b in num_set:
            fibonacci_numbers.add(b)
        a, b = b, a + b

    print("\n> Числа Фібоначчі у множині:")
    print(fibonacci_numbers)
    print(f"> Кількість чисел Фібоначчі: {len(fibonacci_numbers)}")
    return fibonacci_numbers

# Створюємо множину чисел від 1 до 50
num_set = set(range(1, 51))

# Викликаємо функцію для визначення чисел Фібоначчі
fibonacci_in_set = count_fibonacci_in_set(num_set)
