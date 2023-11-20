import random
import logging

logging.basicConfig(filename='log_file.log', level=logging.DEBUG)

def generate_random_sequence(n):
    """
    Генерирует и возвращает случайную последовательность чисел от 1 до n.
    """
    sequence = list(range(1, n+1))
    random.shuffle(sequence)
    return sequence

def extract_next_barrel(sequence):
    """
    Извлекает следующий бочонок из последовательности.
    После извлечения, удаляет бочонок из последовательности.
    Возвращает извлеченный бочонок.
    """
    barrel = sequence.pop(0)
    logging.info(f'Извлечен бочонок: {barrel}')
    return barrel

def play_game():
    """
    Основная функция, которая запускает игру.
    Пользователь вводит количество бочонков (n).
    Генерируется случайная последовательность чисел от 1 до n.
    Пока есть бочонки в последовательности, пользователь может нажимать кнопку
    для извлечения очередного бочонка.
    """
    n = input("Введите количество бочонков (целое положительное число): ")
    try:
        n = int(n)
        if n <= 0:
            raise ValueError
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите положительное целое число.")
        return

    sequence = generate_random_sequence(n)
    print("Игра началась!")

    while sequence:
        _ = input("Нажмите Enter для извлечения очередного бочонка: ")
        extracted_barrel = extract_next_barrel(sequence)
        print(f"Извлечен бочонок: {extracted_barrel}")

    print("Игра окончена!")

if __name__ == '__main__':
    play_game()
