# merge sort. Сортировка слиянием - o(nlogn)


def mergeSort(array):
    if len(array) > 1:

        #  r - gap
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # разделить на 2 части
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

array = [-4, 2, 15, 0, 2, 8, 102, 55]
mergeSort(array)
print(array)