def menu():
    print("Menu:")
    print(" 0.Вернуть в меню")
    print(" 1.Первое задание")
    print(" 2.Второе задание")
    print(" 3.Третье задание")
    print(" 4.Четвертое задание")

    return int(input("Выберите пункт: "))
def task_1():
    print("""Предлагает ввести три целых числа; 
             Считывает введенные числа; 
             Подсчитывает и выводит значения суммы, произведения, минималь¬ного из этих чисел; \n""")
    print('Первое число: ')
    a = input()
    print('Второе число: ')
    b = input()
    print("Третье число")
    c = input()
    summa = (int(a) + int(b) + int(c))
    product = (int(a) * int(b) * int(c))
    if a < b < c:
        print("Минимальное число  ", a)
    elif b < a < c:
        print("Минимальное число ", b)
    else:
        print("Минимальное число ", c)

    print('Сумма: ', summa)
    print('Произведение: ', product)
def task_2():
    print("""Суммирует последовательность целых чисел. 
    Первое, считываемое целое число, определяет количество значений, которое будут введены и просуммированы (первое число не суммируется). 
    Программа должна считывать только одно зна¬чение при каждом выполнении функции ввода. 
    Использовать оператор цикла for:\n""")

    print('Сумма:', sum([int(input('Число ' + str(i + 1) + ': ')) for i in range(int(input('Сколько чисел: ')))]))
def task_3():
    print("""Считывает последовательность символов (0 – конец последовательности). Подсчитать количества вхождений в последовательность: цифр 3, 7, букв К или к. Нарисовать частотную гистограмму с помощью звездочек. Для рисования гистограмм использовать оператор цикла while. Гистограмму представить в виде:\n""")
    amount = []
    symbols = []
    mustbeSafedSymbols = ['3', '7', 'K', 'k']

    # сахраняет нужные введённые символы
    symbol = input("введите любой символ")
    while symbol != '0':
        if symbol == '0':
            break
        elif symbol == mustbeSafedSymbols[0] or symbol == mustbeSafedSymbols[1] or symbol == mustbeSafedSymbols[
            2] or symbol == mustbeSafedSymbols[3]:
            symbols.append(symbol)
        symbol = input("введите любой символ")

    # подсчитывает символы
    for index in mustbeSafedSymbols:
        amount.append(symbols.count(index))
    amount[2] = amount[2] + amount[3]
    amount.pop(3)

    # ресует гистограмму
    for index in range(len(amount)):
        counter = 0
        if mustbeSafedSymbols[index] == 'K':
            print("K,   k", end='')
        else:
            print(mustbeSafedSymbols[index], "  ", amount[index], end='')
        if amount[index] > 9:
            print("   ", end='')
        else:
            print("    ", end='')
        while counter != amount[index]:
            print('*', end='')
            counter += 1
        print('\n')
def task_4():
    print("Выводит на экран последовательность чисел (в последовательности отсутствуют числа 5 и 8): \n")
    for number in range(1, 11):
        if number != 5 and number != 8:
            print(number)
while True:
    access = menu()
    if access == 1:
        task_1();
    elif access == 2:
        task_2();
    elif access == 3:
        task_3();
    elif access == 4:
        task_4();
    elif access == 0:
        menu()
    else:
        break
