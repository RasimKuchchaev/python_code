# Сначала импортируйте модуль ввода файлов Python.
import fileinput

# Повторите содержимое файла данных.
for line in fileinput.input("okrug_full.txt", encoding="utf8"):
    # Распечатать каждую строку текста.
    print(line)