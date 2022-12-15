#Поразрядная сортировка

def countingSort(array, exp):
    n = len(array) # длинна массива
    # out - дубликат массива. count - массив для хранения совпадений
    out = [0] * (n) # массив, который будет хранить отсортированный массив
    count = [0] * (10) # массив счетчик
    # храним число "появлений" в count[]
    for i in range(0, n):
        index = array[i] // exp
        count[index % 10] += 1
    # Меняем count[i] на текущий, где у нас индекс
    # позиция этого числа в out
    for i in range(1, 10):
        count[i] += count[i - 1]
    # строим массив на вывод
    i = n - 1
    while (i >= 0):
        index = array[i] // exp
        out[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1
    # копируем массив out array
    # теперь имеет отсортированные числа
    i = 0
    for i in range(0, len(array)):
        array[i] = out[i]

# сама поразрядная сортировка
def radixSort(array):
    # максимальное число чтобы знать число чисел для проверки
    max1 = max(array)
    # делаем countingsort для каждого чиста. Вместо каждого числа передаем
    # exp, которая 10^i, где i - текущее число
    exp = 1
    while max1 / exp >= 1:
        countingSort(array, exp)
        exp *= 10

#тест
array = [234, 2122, 15, 0, 21, 8, 102, 55]
radixSort(array)
print(array)