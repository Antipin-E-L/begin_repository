import numpy as np
min_number = 1 # нижний предел чисел для загадывания
max_number = 100 # верхний предел чисел для загадывания
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
    local_min_number, local_max_number = min_number, max_number
    # определить локальные пределы для угадывания конкретного числа
    
    while True:
        count += 1
        predict_number = int((np.random.randint(local_min_number, local_max_number + 1)) / 2) 
        # Исходя из локальных пределов выбирается среднее число
        if number == predict_number:
            break # выход из цикла, если угадали
        elif number > predict_number:
            local_min_number = predict_number 
        elif number < predict_number:
            local_max_number = predict_number
    return(count)

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    global min_number, max_number # взять глобальные пределы для загадыния числа

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(min_number, max_number + 1, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

print(score_game(random_predict))
# RUN
if __name__ == '__main__':
    score_game(random_predict)