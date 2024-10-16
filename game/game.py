def get_computer_choice():
    choices = ['камень', 'ножницы', 'бумага']
    return choices[(hash("computer") % 3)]

def get_user_choice():
    while True:
        user_input = input("Введите 'камень', 'ножницы' или 'бумага': ").lower()
        if user_input in ['камень', 'ножницы', 'бумага']:
            return user_input
        print("Неверный ввод. Попробуйте снова.")

def decide_winner(user_choice, computer_choice):
    outcomes = {
        ('камень', 'ножницы'): "Вы выиграли!",
        ('ножницы', 'бумага'): "Вы выиграли!",
        ('бумага', 'камень'): "Вы выиграли!",
    }
    
    if user_choice == computer_choice:
        return "Ничья!"
    elif (user_choice, computer_choice) in outcomes:
        return outcomes[(user_choice, computer_choice)]
    else:
        return "Компьютер выиграл!"

def play_game():
    print("Добро пожаловать в игру 'Камень-Ножницы-Бумага'!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"Вы выбрали: {user_choice}")
    print(f"Компьютер выбрал: {computer_choice}")

    result = decide_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
