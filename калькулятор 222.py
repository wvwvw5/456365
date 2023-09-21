import math

# Операции над числами
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль"
    return x / y

# Тригонометрические функции
def calculate_trigonometric(func, x):
    return func(math.radians(x))

def sin(x):
    return calculate_trigonometric(math.sin, x)

def cos(x):
    return calculate_trigonometric(math.cos, x)

def tan(x):
    return calculate_trigonometric(math.tan, x)

# Функция для вычисления площади прямоугольника
def rectangle_area(width, height):
    return width * height

# Функция для определения четности числа
def is_even(number):
    return number % 2 == 0

# Функция для вычисления суммы цифр числа
def sum_digits(number):
    return sum(int(digit) for digit in str(number))

# Главная функция калькулятора
def main():
    while True:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Синус")
        print("6. Косинус")
        print("7. Тангенс")
        print("8. Выход")

        choice = input("Введите номер операции (1/2/3/4/5/6/7/8): ")

        if choice == '8':
            print("До свидания!")
            break

        if choice in ('1', '2', '3', '4', '5', '6', '7'):
            num1 = float(input("Введите первое число: "))
            
            if choice in ('5', '6', '7'):
                result = None
                if choice == '5':
                    result = sin(num1)
                elif choice == '6':
                    result = cos(num1)
                elif choice == '7':
                    result = tan(num1)
                print("Результат:", result)
            else:
                num2 = float(input("Введите второе число: "))
                if choice == '1':
                    print("Результат:", add(num1, num2))
                elif choice == '2':
                    print("Результат:", subtract(num1, num2))
                elif choice == '3':
                    print("Результат:", multiply(num1, num2))
                elif choice == '4':
                    print("Результат:", divide(num1, num2))
        else:
            print("Неверная операция")

if __name__ == "__main__":
    main()
