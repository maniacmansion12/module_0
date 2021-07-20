import numpy as np
count = 0
number = np.random.randint(1, 101)      # загадали число


def game_core_v3(number):

    count = 1
    predict = 50

    if predict < number:
        predict += 25
    else:
        predict -= 25
    if predict < number:
        predict += 12
    else:
        predict -= 12
    if predict < number:
        predict += 6
    else:
        predict -= 6
    if predict < number:
        predict += 3
    else:
        predict -= 3

    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return(count)  # выход из цикла, если угадали


def score_game(game_core):
    # Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


score_game(game_core_v3)   # в среднем за 2 попытки
