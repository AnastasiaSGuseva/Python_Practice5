"""
1. Напишите программу, удаляющую из текста все слова, содержащие "абв". <- filter

"""

with open('text.txt', 'w', encoding='UTF-8') as file:
    file.write('абв лрлкедп лпрлабв плущщпь абв еее')

with open('text.txt', 'r', encoding='UTF-8') as text:
    text1 = text.readline().split()


list_text2 = list(filter(lambda x: 'абв' not in x, text1))
text2 = ' '.join(list_text2)


with open('text.txt', 'w', encoding='UTF-8') as file:
    file.writelines(text2)
