# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count("а"))

# Вывести количество гласных букв в слове
word_one = 'Архангельск'
glasniye = ["а", "я", "у", "ю", "о", "е", "ё", "э", "и", "ы"]
i = 0
for letter in word_one.lower():
    if letter in glasniye:
        i += 1
        print(f'{i} "раз"')

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
lenght = 0
for word in sentence.split():
    lenght += len(word)
else:
    print(f'Средняя длина слова в предложении {lenght // len(sentence.split())}')
