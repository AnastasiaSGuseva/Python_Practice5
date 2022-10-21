# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

str1 = 'fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhheee222111111111'
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

print(str2)

str3 = ''
for i in range(0, len(str2), 2):
    str3 += (int(str2[i]) * str2[i+1])

print(str3)

print(str1 == str3)







