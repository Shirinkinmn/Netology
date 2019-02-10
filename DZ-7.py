math_func = input('Для вычисления введите операцию и два положительных числа через пробел: ', )
math_list = math_func.split()
assert math_list[0] in ['+', '-', '*', '/'], 'Данная математическая операция не может быть выполнена'
assert int(math_list[1]) > 0 and int(math_list[2]) > 0 ,  'Аргументы должны быть положительными числами'
assert len(math_list) == 3, 'Введено неверное количество аргументов'

if math_list[0] == '+':
    try:
        print('Результат сложения равен: ', int(math_list[1]) + int(math_list[2]))
    except ValueError:
        print('Значения аргументов заданы не верно')

elif math_list[0] == '-':
    try:
        print('Результат разности равен: ', int(math_list[1]) - int(math_list[2]))
    except ValueError:
        print('Значения аргументов заданы не верно')

elif math_list[0] == '*':
    try:
        print('Результат умножения равен: ', int(math_list[1]) * int(math_list[2]))
    except ValueError:
        print('Значения аргументов заданы не верно')

elif math_list[0] == '/':
    try:
        print('Результат деления равен: ', int(math_list[1]) / int(math_list[2]))
    except ZeroDivisionError:
        print('Выполнение операции невозможно - деление на ноль')
    except ValueError:
        print('Значения аргументов заданы не верно')
