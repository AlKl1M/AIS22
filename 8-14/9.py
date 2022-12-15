#Пирамидальная (heapsort)

# чтобы привести к куче поддерево по индексу i. n - размер
# n - размер кучи
def heapify(arr, n, i):
    largest = i #считается корнем
    left = 2 * i + 1
    right = 2 * i + 2
    # если левый "ребенок" корня существует и он больше, чем корень
    if left < n and arr[i] < arr[left]:
        largest = left
    # если правый "ребенок" корня существует и он больше, чем корень
    if right < n and arr[largest] < arr[right]:
        largest = right
    # поменять корень, если нужно
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])
        # приводим корень к куче
        heapify(arr, n, largest)

#основная функция
def heapSort(arr):
    n = len(arr)
    # строим кучу. Пока последний родитель будет в ((n//2)-1) мы можем начать отсюда
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # один за одним из вытаскиваемых элементов
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i]) # свапаем
        heapify(arr, i, 0)

# тест
array = [-4, 2, 15, 0, 2, 8, 102, 55]
heapSort(array)
print(array)
