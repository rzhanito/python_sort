from sort_functions import shellSort, fillArray
import time

arr = []
fillArray(arr, 10000)
print(f"Исходный массив: {arr}")
startTime = time.time()
equation, swap = shellSort(arr)
print(f"Итоговый массив: {arr}")
print(f"Количество сравнений: {equation} Количество перестановок: {swap}")
endTime = time.time()
totalTime = float("{:.9f}".format(endTime - startTime))
print(f"Время выполнения функции: {totalTime}")
