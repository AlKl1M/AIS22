import os
import tempfile
import heapq
import sys


# кучу выделил в класс для удобства. filehandler - файл, где числа.
class heapnode:
    def __init__(
            self,
            item,
            fileHandler):
        self.item = item
        self.fileHandler = fileHandler

#  идея в том, что мы разбиваем большой файл на маленькие, сортируем маленькие
#  используя heapq, чтобы соединять разные маленькие отсортированные файлы
#  каждый отсортированный файл загружается как генератор. Память не нагрузит.
class externalMergeSort:
    #конструктор
    def __init__(self):
        self.sortedTempFileHandlerList = []
        self.getCurrentDir()

    def getCurrentDir(self):
        self.cwd = os.getcwd()

    # для прохождения по генератору отсортированного файла
    def iterateSortedData(self, sortedCompleteData):
        for no in sortedCompleteData:
            print(no)

    # сортируем все числа в листе файлов, которые указывают через Filehandlers из sortedTempFileHandlerList
    def mergeSortedTempFiles(self):
        mergedNo = (map(int, tempFileHandler) for tempFileHandler in self.sortedTempFileHandlerList)
        sortedCompleteData = heapq.merge(
            *mergedNo
        )
        return sortedCompleteData

    # из прошлой лабы. Аналогично, но класс.
    def heapify(self, arr, i, n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left].item < arr[i].item:
            smallest = left
        else:
            smallest = i

        if right < n and arr[right].item < arr[smallest].item:
            smallest = right

        if i != smallest:
            (arr[i], arr[smallest]) = (arr[smallest], arr[i])
            self.heapify(arr, smallest, n)

    # конструктор для кучи
    def constuct_heap(self, arr):
        l = len(arr) - 1
        mid = l / 2
        while mid >= 0:
            self.heapify(arr, mid, l)
            mid -= 1

    #   обьединяем k отсортированных маленьких файлов в больший файл. Передвигаем первый
    #   элемент всего файла в minheap. Куча теперь самый маленький элемент.
    #   Передвигаем этот элемент из кучи в файл. Используем filehandler этого
    #   элемента. Читаем следующий используя такой же filehandler. Если следующий
    #   элемент пустой, передвигаем его в кучу. Опять юзаем heapidy. Продолжаем
    #   пока все элементы кучи совпадают с INT_MAX - максимальное число или все меньшие
    #   файлы уже прочитаны.
    def mergeSortedTempFiles_low_level(self):
        list = []
        sorted_output = []
        for tempFileHandler in self.sortedTempFileHandlerList:
            item = int(tempFileHandler.readline().strip())
            list.append(heapnode(item, tempFileHandler))

        self.constuct_heap(list)
        while True:
            min = list[0]
            if min.item == sys.maxsize:
                break
            sorted_output.append(min.item)
            fileHandler = min.fileHandler
            item = fileHandler.readline().strip()
            if not item:
                item = sys.maxsize
            else:
                item = int(item)
            list[0] = heapnode(item, fileHandler)
            self.heapify(list, 0, len(list))
        return sorted_output

    #   разбитие файлов на меньшие "чанки",  сортирует их и хранит в папку temp
    def splitFiles(self, largeFileName, smallFileSize):
        with open(largeFileName, 'rb') as largeFileHandler:
            tempBuffer = []
            size = 0
            while True:
                number = largeFileHandler.readline()
                if not number:
                    break
                tempBuffer.append(number)
                size += 1
                if size % smallFileSize == 0:
                    tempBuffer = sorted(tempBuffer, key=lambda no: int(no.strip()))
                    tempFile = tempfile.NamedTemporaryFile(dir=self.cwd + '\\temp', delete=False)
                    tempFile.writelines(tempBuffer)
                    tempFile.seek(0)
                    self.sortedTempFileHandlerList.append(tempFile)
                    tempBuffer = []


# тест. Вывод в консоль.
if __name__ == "__main__":
    largeFileName = 'largefile'
    smallFileSize = 10
    obj = externalMergeSort()
    obj.splitFiles(largeFileName, smallFileSize)
    sortedCompleteData = obj.mergeSortedTempFiles()
    obj.iterateSortedData(sortedCompleteData)