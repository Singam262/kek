def menu():
    print("Menu:")
    print(" 0.Вернуть в меню")
    print(" 1.Первое задание")
    print(" 2.Второе задание")
    print(" 3.Третье задание")
    print(" 4.Четвертое задание")
    return int(input("Выберите пункт: "))
def task_1():
    print("Предлагает ввести строку. "
          "Подсчитать самую длинную последовательность подряд идущих букв а. "
          "Решить данную задачу двумя способами – без использования стандартных процедур и "
          "функций для работы со строками и с их использованием.")
    print('Введите строку')
    s = input()
    c = [0, 0]
    l = [s[0], s[0]]
    for i in s:
        if i == l[1]:
            c[1] += 1
            if c[1] > c[0]:
                c[0] = c[1]
                l[0] = l[1]
        else:
            c[1] = 1
            l[1] = i
    print(c[0], l[0])
def task_2():
    print("Считывает дату в формате 07/21/55 и выводит в формате July 21, 1955."
          " Названия месяцев задать как кортеж.")
    from datetime import datetime
    date_input = input('Enter a date(mm/dd/yy): ')

    date_object = datetime.strptime(date_input, '%m/%d/%y')
    print(date_object.strftime('%B %d, %Y'))
def task_3():
    print("Преобразует целые значения температуры в шкале Фаренгейта в диапазоне от 20 до 40 градусов "
          "в значения температуры с плавающей точкой "
          "в шкале Цельсия с точностью 3 цифры. "
          "Для вычисления использовать формулу: celcius = 5.0 / 9.0 * ( fahrenheit – 32 ). "
          "Результат должен быть напечатан в два столбца шириной 10 символов с выравниванием по правому краю. "
          "Перед значением температуры в шкале Цельсия должен выводиться знак, "
          "как для отрицательных значений, так и для положительных.")
    print("farenheit        celasius")
    for i in range(20,41):
        celsius=5.0/9.0*(i-32)
        print(i,"                   ","%.2f"% celsius)
def task_4():
line=input("Stroku")
counter=0
mostcommon=0
for letter in line:
  if letter == 'a':
    counter+=1
  else:
      if mostcommon<counter:
         mostcommon=counter
      counter=0;
print(mostcommon)
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
