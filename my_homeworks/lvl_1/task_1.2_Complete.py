# Задача 1.2.

# Пункт A.
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

import random

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
three_random_song_a = random.sample(my_favorite_songs, 3)
print(three_random_song_a)
ttl = three_random_song_a[0][1] + three_random_song_a[1][1] + three_random_song_a[2][1]
print("Пункт A: ", "Три песни звучат", round(ttl), "Минут")

# Пункт B.
# Есть словарь песен
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
 }
my_favorite_songs_lst = list(my_favorite_songs_dict.items())
three_random_song_b = random.sample(my_favorite_songs_lst, 3)
ttl = three_random_song_b[0][1] + three_random_song_b[1][1] + three_random_song_b[2][1]
print(three_random_song_b)
print("Пункт B: ", "Три песни звучат", round(ttl), "минут")

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

ttl_el = len(my_favorite_songs)
random_lst = random.sample(my_favorite_songs, ttl_el)
print("Пункт C: ", random_lst)

# Дополнительно
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime

import datetime

