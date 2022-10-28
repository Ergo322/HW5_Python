# 38. Напишите программу, удаляющую из текста
# все слова, содержащие ""абв"".
text = input()
text = text.split()
new_text = ''
for i in text:
    if 'abc' not in i:
        new_text += i + ''
print(new_text)

text = input()
text = text.split()
new_text = list(filter(lambda x: 'abc' not in x, text))
print(new_text)

# 42. Реализуйте RLE алгоритм: реализуйте модуль
# сжатия и восстановления данных.

# a a a a b b b b c c c c d d d d = 4a 4b 4c 4d

text = (input('Введите текст: '))
text = text.split()
new_text = []
count = 0
i = 0
while (i+1) < len(text):

    if text[i] == text[i+1]:
        count += 1
        i += 1
    else:
        i += 1
        new_text.append(count + 1)
        new_text.append(text[i - 1])
        count = 0
new_text.append(count + 1)
new_text.append(text[i])
ready_text = (''.join(map(str, new_text)))
print(ready_text)


