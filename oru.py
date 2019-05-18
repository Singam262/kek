print("Предлагает ввести строку. "
          "Подсчитать самую длинную последовательность подряд идущих букв а. "
          "Решить данную задачу двумя способами – без использования стандартных процедур и "
          "функций для работы со строками и с их использованием.")
print("vtoroj sposob")
line=(input("vvedite stroku"))
map = str.maketrans('qwertyuiopsdfghjklzxcvbnm', '                      ')
line=line.translate(map)
line2=line.split(' ')
print(max(line2).count('a'))
