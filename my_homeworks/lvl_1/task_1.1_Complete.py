# Задача 1.1.

# Есть строка с перечислением песен

# my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
string_length = len(my_favorite_songs)
print(len(my_favorite_songs))
print(my_favorite_songs[:14])
print(my_favorite_songs[64:77])
print(my_favorite_songs[16:30])
print(my_favorite_songs[51:60])
