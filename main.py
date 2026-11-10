import math

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Факториал отрицательного числа не существует.")
    return math.factorial(n)

def main() -> None:
    user_input = input("Введите положительное целое число: ")

    # Проверка на то, что пользователь ввел целое число
    try:
        number = int(user_input)
    except ValueError:
        print("Ошибка: введите целое число без дробной части и посторонних символов.")
        return

    # Проверка, что число положительное
    if number < 0:
        print("Ошибка: число должно быть положительным.")
        return

    # Вычисление факториала
    try:
        result = factorial(number)
    except ValueError as error:
        print(f"Ошибка: {error}")
        return

    # Вывод результата
    print(f"Факториал числа {number}! равен: {result}")

if __name__ == "__main__":
    main()