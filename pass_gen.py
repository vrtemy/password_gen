import random

flag = True
classic = [
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g',
    'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R',
    'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
    'Z', 'X', 'C', 'V', 'B', 'N', 'M'
]
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] * 2
symbols = ['-', '#', '$', '&', '%'] * 5
password = ''

while flag == True:
    how_long = int(input('Длина пароля: '))

    if how_long > 50:
        print('Слишком длинный пароль!')
        continue

    use_numbers = input(
        'Использовать цифры? [Y/N]: ').upper() == 'Y'  # True / False
    use_symbols = input('Использовать символы? (-/#/$/&/%) [Y/N]: ').upper(
    ) == 'Y'  # True / False

    if use_numbers == True and use_symbols == True:
        passgen_lib = random.sample(classic + numbers + symbols, how_long)
    elif use_symbols == True and use_numbers != True:
        passgen_lib = random.sample(classic + symbols, how_long)
    elif use_numbers == True and use_symbols != True:
        passgen_lib = random.sample(classic + numbers, how_long)
    else:
        passgen_lib = random.sample(classic, how_long)

    for i in passgen_lib:
        password += i

    print(f'\nПароль: {password}')
    print('_' * 8 + '_' * how_long + '\n')

    passgen_lib = None
    password = ''

    flag = input('Еще раз? [Y/N]: ').upper() == 'Y'
