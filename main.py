import math

# Реализована функция вычисления факториала введенного числа
def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Функция с импользованием библитотеки math для работы с факториалами
def factorial_lib(n: int) -> int:
    return math.factorial(n)

def read_positive_integer() -> int:
    while True:
        user_input = input("Введите положительное целое число: ")

        try:
            number = int(user_input)
        except ValueError:
            print("Ошибка: нужно ввести целое число без дробной части и посторонних символов.")
            continue

        if number < 0:
            print("Ошибка: число должно быть положительным.")
            continue

        return number

def main() -> None:
    try:
        number = read_positive_integer()
        # В работе приложения используется оптимизированная функция для работы с факториалами
        result = factorial_lib(number)
        # result = factorial(number)

        print(f"Факториал числа {number} равен: {result}")

    except (KeyboardInterrupt, EOFError):
        print("\nПрограмма завершена пользователем.")

if __name__ == "__main__":
    main()