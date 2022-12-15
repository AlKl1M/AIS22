#quick sort

def quickSort(array):
    if len(array) < 2: # если длина меньше 2, то мы не можем взять pivot
        return array
    else:
        pivot = array[0] #произвольный элемент для начала отсчета
        # делим на подмассивы, где больше и меньше числа
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        # делим на подмассивы обьединяем через рекурсию и возвращаем.
        return quickSort(less) + [pivot] + quickSort(greater)

#тест
array = [4, 2, 15, 0, 2, 8, 102, 55]
print(quickSort(array))