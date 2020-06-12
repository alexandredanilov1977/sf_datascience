import numpy as np


# Механизм определения загаданного числа
def game_core_v2(number):
    # Установка стартовых параметров
    lower_limit = 1
    upper_limit = 101    
    count = 1
    predict = int((upper_limit-lower_limit) / 2)

    # Если число не угадали, то сужаем диапазон и далаем новое предсказание
    while number != predict:
        count += 1
        # Cужаем диапазон.
        if number > predict: 
            lower_limit = predict+1            
        elif number < predict: 
            upper_limit = predict-1 

        # Делаем новое предсказание.               
        predict = new_predict(lower_limit, upper_limit)
    
    # Если число угадано, возвращаем количество итераций
    return count


# Определение нового предсказанного значения
# Новое значение - середина нового диапазона     
def new_predict(lower_limit, upper_limit):
    return int((upper_limit+lower_limit) / 2)


# Механизм многоразового запуска программы, для подсчета среднего числа попыток
# Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число
def score_game(game_core):
    count_ls = []
    # Создаем тестовый набора значений
    # Фиксируем ramdom seed, чтобы эксперимент был воспроизводим
    np.random.seed(1)  
    random_array = np.random.randint(1, 101, size=1000)

    # Для каждого значения из набора запускаем игру
    for number in random_array:
        count_ls.append(game_core(number))

    # Расчитываем средний показатель попыток 
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

    # Возвращаем среднее число попыток
    return(score)


score_game(game_core_v2)
