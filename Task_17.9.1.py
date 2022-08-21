"""Hа вход подается последовательность чисел через пробел,
   а также запрашивается у пользователя любое число.
   В результате работы программы устанавливается номер позиции элемента,
   который меньше введенного пользователем числа,
   а следующий за ним больше или равен этому числу"""

def entering_values():  # Функция принимает последовательость чисел и любое число
    global list_number, number
    try:  # Конструкция исключает ввод любых символов, кроме целых чисел
        chain = input("Введите числа через пробел: \n")
        number = int(input("Введите любое число в диапазоне: \n"))
        list_number = list(map(int, chain.split()))  # Последовательность чисел преобразуем в список
    except ValueError as e:
        print("Вы ввели неверное число. Введите числа повторно.")
        entering_values()
    else:  # Отсекаются значения числа вне введенной последовательности
        sort_list()
        if number <= list_number[0] or number > list_number[-1]:
            print('Число не входит в допустимый диапазон. Решения нет')
            entering_values()
        return()

def sort_list():  #Фунция сортировки списка
    list_number.sort()
    return

def search_number(list_number, number, left, right):  # Функция поиска нужного элемента
    if left > right:
        return 'Введенное число не соответствует заданному условию'
    middle = (left+right) // 2
    if number > list_number[middle-1] and number <= list_number[middle]:
        return middle-1
    # Это условие на случай повторяющихся элементов: (ниже)
    elif number == list_number[middle-1] and number <= list_number[middle]:
        return search_number(list_number, number, left, right-1)
    elif number < list_number[middle]:
        return search_number(list_number, number, left, middle-1)
    else:
        return search_number(list_number, number, middle+1, right)

entering_values()  # Вызов функции ввода значений
left, right = 0, len(list_number)-1  # Находим крайние значения индексов

#print(list_number, number) #Эта строка для проверки работы функций
#print(left, right)         #Эта строка для проверки работы функций
# Вызов функции поиска:
print(f"Первое число меньшее {number} в последовательности {list_number} находится на {search_number(list_number, number, left, right)} позиции")