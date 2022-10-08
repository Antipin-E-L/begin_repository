import numpy as np
min_number = 1 # Нижний предел чисел для загадывания
# Можно изменить с сохранностью работоспособности кода
max_number = 100 # Верхний предел чисел для загадывания
# Можно изменить с сохранностью работоспособности кода

def random_predict(number:int=1) -> int:
    """Угадываем число используя бинарный поиск

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    global min_number, max_number 
    # Взять глобальные значения пределов для угадывания числа
    loc_min_num, loc_max_num = min_number - 1, max_number 
    # Определить локальные пределы для угадывания конкретного числа
    while True:
        count += 1
        predict_num = round((loc_min_num + loc_max_num) / 2)
        # Определить среднее число между двумя пределами
        if number == predict_num:
            break # Выход из цикла, если угадали
        elif number > predict_num:
            loc_min_num = predict_num
        elif number < predict_num:
            loc_max_num = predict_num
    return(count)

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов 
    угадывает наш алгоритм

    Args:
        random_predict ([type]): Функция угадывания

    Returns:
        int: Среднее количество попыток
    """
    global min_number, max_number 
    # Взять глобальные пределы для загадыния числа

    count_ls = [] # Список для сохранения количества попыток
    np.random.seed(1) # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(min_number, max_number + 1, size=(1000)) 
    # Загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # Находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)