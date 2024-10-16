def get_number():
    for num in range(30):
        if num % 2 != 0:  # Проверяем, является ли число нечетным
            yield num  # Возвращаем нечетное число

# Создаем генератор
odd_numbers = get_number()

# Сохраняем нечетные числа в список для удобства
odd_numbers_list = list(odd_numbers)

# Находим первое, пятое и последнее значение
first_value = odd_numbers_list[0] if len(odd_numbers_list) > 0 else None
fifth_value = odd_numbers_list[4] if len(odd_numbers_list) > 4 else None
last_value = odd_numbers_list[-1] if len(odd_numbers_list) > 0 else None

# Выводим результаты
print("Первое нечетное число:", first_value)
print("Пятое нечетное число:", fifth_value)
print("Последнее нечетное число:", last_value)
