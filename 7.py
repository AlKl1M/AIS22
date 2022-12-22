#Shell sort. w - O(n^2) best - O(nlog(n))

def shellSort(array):
    n = len(array)
    gap = n // 2

    while gap > 0:
        j = gap
        while j < n:
            i = j - gap
            while i >= 0:
                if array[i + gap] > array[i]:
                    break
                else:
                    array[i+gap], array[i] = array[i], array[i+gap]
                i = i - gap
            j+=1
        gap = gap // 2

array = [-4, 2, 15, 0, 2, 8, 102, 55]
shellSort(array)
print(array)