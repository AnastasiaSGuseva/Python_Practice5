"""
4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

"""


with open('4_input.txt', 'r') as file:
    str1 = file.read()


str2 = ''
i = 0


while i != len(str1):
    k = str1.count(str1[i])
    if k < 9:
        str2 += str(k) + str1[i]
    else:
        str2 += '9' + str1[i]
        while k > 9:
            k = k - 9
            if k < 9:
                str2 += str(k) + str1[i]
            else:
                str2 += '9' + str1[i]
    i += str1.count(str1[i])


with open('4_output1.txt', 'w') as file2:
    file2.write(str2)


str3 = ''


for i in range(0, len(str2), 2):
    str3 += (int(str2[i]) * str2[i+1])


with open('4_output2.txt', 'w') as file3:
    file3.write(str3)








