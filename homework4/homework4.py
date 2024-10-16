def generate_random_numbers(size):
    numbers = []
    for _ in range(size):
        # Генерируем случайное число от 0 до 200
        number = (hash(str(_)) % 201)  # Используем hash для генерации "случайного" числа
        numbers.append(number)
    return numbers

def find_multiples_of_x():
    # Генерируем список случайных чисел размером не менее 10
    numbers = generate_random_numbers(10)
    print("Сгенерированные числа:", numbers)
    
    # Запрашиваем у пользователя цифру X
    while True:
        try:
            x = int(input("Введите цифру X (от 1 до 9): "))
            if 1 <= x <= 9:
                break
            else:
                print("Пожалуйста, введите цифру от 1 до 9.")
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите целое число.")

    # Используем лямбда-функцию для фильтрации кратных X
    multiples = list(filter(lambda num: num % x == 0, numbers))

    # Выводим найденные числа
    print(f"Числа, кратные {x}: {multiples}")

# Вызов функции
find_multiples_of_x()
