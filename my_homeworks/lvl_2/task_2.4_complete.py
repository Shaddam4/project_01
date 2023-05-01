# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

print("Пункт A.")
def remove_exclamation_marks(s):
    s1 = '!'
    output = ""
    for i in s:
        if i == s1:
            continue
        output += i
    return output


print(f'Hi! Hello! -> {remove_exclamation_marks("Hi! Hello")}')
print(f'"" -> {remove_exclamation_marks("")}')
print(f'Oh, no!!! -> {remove_exclamation_marks("Oh, no!!!")}')


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"
print("Пункт B.")
def remove_last_em(s):
    i = 0
    while i < 1 and s[-1] == "!":
        s = s[:-1]
        i += 1
    return s

print(f'Hi! == {remove_last_em("Hi!")}')
print(f'Hi!!! == {remove_last_em("Hi!!!")}')
print(f'!Hi == {remove_last_em("!Hi")}')

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"
print("Пункт C.")
def remove_word_with_one_em(s):
    s = s.split(' ')
    for item in tuple(s):
        ttl_s = item.count('!')
        if ttl_s == 1:
            s.remove(item)
    words = ''.join(s)
    return words


print(f'remove("Hi!") === "{remove_word_with_one_em("Hi!")}"')
print(f'remove("Hi! Hi!") === "{remove_word_with_one_em("Hi! Hi!")}"')
print(f'remove("Hi! Hi! Hi!") === "{remove_word_with_one_em("Hi! Hi! Hi!")}"')
print(f'remove("Hi Hi! Hi!") === "{remove_word_with_one_em("Hi Hi! Hi!")}"')
print(f'remove("Hi! !Hi Hi!") === "{remove_word_with_one_em("Hi! !Hi Hi!")}"')
print(f'remove("Hi! Hi!! Hi!") === "{remove_word_with_one_em("Hi! Hi!! Hi!")}"')
print(f'remove("Hi! !Hi! Hi!") === "{remove_word_with_one_em("Hi! !Hi! Hi!")}"')
print(remove_word_with_one_em("join! !then! for!!"))