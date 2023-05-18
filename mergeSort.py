import time
from sort_functions import fillArray, mergeSort


arr = []
fillArray(arr, 1000000)
print(f"Исходный массив: {arr}")
startTime = time.time()
equation, swap = mergeSort(arr)
print(f"Итоговый массив: {arr}")
print(f"Количество сравнений: {equation} Количество перестановок: {swap}")
endTime = time.time()
totalTime = float("{:.9f}".format(endTime - startTime))
print(f"Время выполнения функции: {totalTime}")
