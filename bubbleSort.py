from sort_functions import fillArray, bubbleSort
import time

arr = []
fillArray(arr, 1000)
print(f"Исходный массив: {arr}")
startTime = time.time()
comparison, swaps = bubbleSort(arr)
print(f"Итоговый массив: {arr}")
endTime = time.time()
totalTime = endTime - startTime
print(f"Время выполнения алгоритма составило: {totalTime}")
print(f"Количество перестановок: {swaps}. Количество сравнений: {comparison}")
