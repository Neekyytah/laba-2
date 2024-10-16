def calculate_age():
    # Запрос текущей даты у пользователя
    current_date_input = input("Введите сегодняшнюю дату (дд/мм/гггг): ")
    
    # Разделяем введенную строку на день, месяц и год
    try:
        current_day, current_month, current_year = map(int, current_date_input.split('/'))
    except ValueError:
        print("Неверный формат даты. Пожалуйста, используйте формат дд/мм/гггг.")
        return

    # Запрос даты рождения у пользователя
    birth_date_input = input("Введите вашу дату рождения (дд/мм/гггг): ")

    # Разделяем введенную строку на день, месяц и год
    try:
        day, month, year = map(int, birth_date_input.split('/'))
    except ValueError:
        print("Неверный формат даты. Пожалуйста, используйте формат дд/мм/гггг.")
        return

    # Вычисляем возраст
    age = current_year - year

    # Проверяем, был ли день рождения в этом году
    if (current_month, current_day) < (month, day):
        age -= 1

    print(f"Ваш возраст: {age} лет.")

# Вызов функции
calculate_age()
