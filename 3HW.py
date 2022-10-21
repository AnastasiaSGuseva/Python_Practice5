"""
3. Создайте программу для игры в ""Крестики-нолики"".

"""


matrix = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]


def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end='\t')
        print()
        print()


print_matrix(matrix)


def matrix_to_string(m):
    mtr_string = ''
    for i in range(len(m)):
        for j in range(len(m[i])):
            mtr_string += ''.join(m[i][j])
    return mtr_string


def win_in_main_diagonal(m, sign):
    status = []
    for i in range(len(m)):
        if m[i][i] == sign:
            status.append(True)
        else:
            status.append(False)
    if status == [True, True, True]:
        return True
    else:
        return False


def win_in_side_diagonal(m, sign):
    if m[0][2] == sign and m[1][1] == sign and m[2][0] == sign:
        return True


def win_in_row(m, sign):
    for i in range(len(m)):
        if m[i] == [sign, sign, sign]:
            return True


def win_in_columns(m, sign):
    for i in range(len(m)):
        status = []
        for j in range(len(m[i])):
            if m[j][i] == sign:
                status.append(True)
            else:
                status.append(False)
        if status == [True, True, True]:
            return True
            break


while not matrix_to_string(matrix).isalpha():
    pl1i = int(input('Укажите строку для х: '))
    pl1j = int(input('Укажите столбец для х: '))
    matrix[pl1i-1][pl1j-1] = 'x'
    print_matrix(matrix)
    if win_in_main_diagonal(matrix, 'x'):
        print('Победа Х!')
        break
    if win_in_side_diagonal(matrix, 'x'):
        print('Победа Х!')
        break
    if win_in_row(matrix, 'x'):
        print('Победа Х!')
        break
    if win_in_columns(matrix, 'x'):
        print('Победа Х!')
        break
    if matrix_to_string(matrix).isalpha():
        print('Ничья!')
        break
    pl2i = int(input('Укажите строку для o: '))
    pl2j = int(input('Укажите столбец для o: '))
    matrix[pl2i-1][pl2j-1] = 'o'
    print_matrix(matrix)
    if win_in_main_diagonal(matrix, 'o'):
        print('Победа O!')
        break
    if win_in_side_diagonal(matrix, 'o'):
        print('Победа O!')
        break
    if win_in_row(matrix, 'o'):
        print('Победа O!')
        break
    if win_in_columns(matrix, 'o'):
        print('Победа O!')
        break
    if matrix_to_string(matrix).isalpha():
        print('Ничья!')
        break
