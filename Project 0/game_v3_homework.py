import numpy as np
min_number = 1 # нижний предел чисел для загадывания
# можно изменить с сохранностью работоспособности кода
max_number = 100 # верхний предел чисел для загадывания
# можно изменить с сохранностью работоспособности кода

def random_predict(number:int=1) -> int:
    """Угадываем число используя бинарный поиск

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    global min_number, max_number 
    # взять глобальные значения пределов для угадывания числа
    loc_min_num, loc_max_num = min_number - 1, max_number 
    # определить локальные пределы для угадывания конкретного числа
    while True:
        count += 1
        predict_num = round((loc_min_num + loc_max_num) / 2)
        # Определить среднее число между двумя пределами
        if number == predict_num:
            break # выход из цикла, если угадали
        elif number > predict_num:
            loc_min_num = predict_num
        elif number < predict_num:
            loc_max_num = predict_num
    return(count)

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов 
    угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    global min_number, max_number 
    # взять глобальные пределы для загадыния числа

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(min_number, max_number + 1, size=(1000)) 
    # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)