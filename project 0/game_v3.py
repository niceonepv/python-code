"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
При этом мы хотим минимизировать количество попыток до 20
"""

import numpy as np


def smart_predict(number, left : int = 0, right: int = 100) -> int:
    """Начинаем с середины и действуем методом деления пополам, узнавая с какой стороны число от текущего

    Args:
        predict_number (int, optional): Предполагаемое число. Defaults to 50.

    Returns:
        int: Число попыток
    """
    count = 0
    while right-left >=1:
        predict_num = (right + left) // 2
        
        if predict_num > number:
            right = predict_num
            count += 1
        
        if predict_num < number:
            left = predict_num
            count += 1
        
        if predict_num == number:
            return count 


def score_game(smart_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(200))  # загадали список чисел

    for number in random_array:
        count_ls.append(smart_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(smart_predict)
