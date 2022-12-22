#сортировка вставками. Insertion sort. w - O(n^2) best - O(n)
# максимальное время если отсортированы в обратном порядке. Минимум - отсортированы.

def insertSort(array):
    for i in range(1, len(array)):
        key = array[i]
        # Все элементы до i-1 которые больше ключа передвигаем на 1 позицию от их текущей
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j + 1] = key


array = [-4, 2, 15, 0, 2, 8, 102, 55]
insertSort(array)
print(array)