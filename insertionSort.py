# 1.	Сортировка вставками. Место помещения очередного элемента в отсортированную часть определить с помощью двоичного поиска. Двоичный поиск оформить в виде отдельной функции.
from sort_functions import fillArray, binaryInsertionSort
import time


arr = []
fillArray(arr, 10000)
print(f"Исходный массив: {arr}")
startTime = time.time()
comparison, swaps = binaryInsertionSort(arr)
print(f"Итоговый массив: {arr}")
endTime = time.time()
totalTime = float("{:.9f}".format(endTime - startTime))
print(f"Время выполнения алгоритма составило: {totalTime}")
print(f"Количество перестановок: {swaps}. Количество сравнений: {comparison}")
