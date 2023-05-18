from sort_functions import fillArray, cocktailSort
import time

arr = []
fillArray(arr, 10000)
print(f"Исходный массив: {arr}")
startTime = time.time()
comparison, swaps = cocktailSort(arr)
print(f"Итоговый массив: {arr}")
endTime = time.time()
totalTime = float("{:.9f}".format(endTime - startTime))
print(f"Время выполнения алгоритма составило: {totalTime}")
print(f"Количество перестановок: {swaps}. Количество сравнений: {comparison}")
