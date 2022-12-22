# Сортировка прочесыванием. Comb sort. w - o(n^2) b - o(nlogn) mem - o(1)

def getNextGap(gap):
    gap = (gap * 10) // 13

    if (gap < 1):
        return 1
    return gap

def combSort(array):
    n = len(array)
    gap = n
    swapped = True
    while gap != 1 or swapped == 1:
        gap = getNextGap(gap)
        swapped = False

        for i in range(0, n-gap):
            if array[i] > array[i+gap]:
                array[i], array[i+gap] = array[i + gap], array[i]
                swapped = True

array = [-4, 2, 15, 0, 2, 8, 102, 55]
combSort(array)
print(array)

