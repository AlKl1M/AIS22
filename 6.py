# Посредством выбора. Selection sort. o(n^2) - пройтись по массиву и сравнить

import sys

def selectionSort(array):
    for i in range(len(array)):
        ind_min = i
        for j in range(i + 1, len(array)):
            if array[ind_min] > array[j]:
                ind_min = j

        array[i], array[ind_min] = array[ind_min], array[i]

array = [-4, 2, 15, 0, 2, 8, 102, 55]
selectionSort(array)
print(array)