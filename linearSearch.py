from sort_functions import fillArray, mergeSort

arr = []
fillArray(arr, 20)
mergeSort(arr)


num = 9
print(f"Массив: {arr}")
for i in arr:
    if i == num:
        print(f"Искомый элемент находится под индексом {arr[i]}. {num, i}")
        break
    else:
        print("Элемента в массиве нет.")
