# Задача на списки и словари: "Статистика по тексту"
# Напишите программу, которая:
# Принимает от пользователя текст (можно многострочный).

# Считает:
# Количество уникальных слов (без учёта регистра).
# Самое длинное слово.
# Частоту каждой буквы (сколько раз встречается а, б и т.д.).

# Пример:
# Ввод:
# "Солнце светит, солнце греет, солнце всех нас веселит!"  

# Вывод:
# Уникальных слов: 7  
# Самое длинное слово: "греет"  
# Частота букв: {'с': 7, 'о': 3, 'л': 3, ...}  


line = input("Введите строку: ")

# Количепство уникальных слов

line = line.lower() #сделает все буквы одного размера
words = line.split() # поделит текст на слова

un_words = {} #словарь для уникальных слов

for word in words:
    un_words[word] = True #доб слово в словарь

count_un_words = len(un_words) #считает кол уникальных слов

print(f"Количество уникальных слов: {count_un_words}")

#  Самое длинное слово
word_len = {} 
max_len = 0
longest_word = ""

for word in words:
    word_len[word] = len(word) #длина слова

for word in word_len: #перебирает все слова в созданном словаре
    if word_len[word] > max_len:
        max_len = word_len[word]
        longest_word = word

print(f"Самое длиное слово: {longest_word} (длина: {max_len})")


#Частоста букв

letter_count = {} #пустой словарь

for i in line:
    i_lower = i.lower() # каждый символ в строчную букву
    if i_lower in letter_count:
        letter_count[i_lower] += 1
    else:
        letter_count[i_lower] = 1

print("Частота букв:", letter_count)