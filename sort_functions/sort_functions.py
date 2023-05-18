import random


def fillArray(arr, length):
    for i in range(length):
        arr.append(random.randint(1, length))
    return arr


def bubbleSort(array):
    count = 0
    swaps = 0
    for i in range(len(array)):
        for j in range(len(array)-1):
            count += 1
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                swaps += 1
    return [count, swaps]


def selectionSort(array):
    comparing = 0
    swap = 0
    for i in range(len(array)):
        minIndex = i
        for j in range(i+1, len(array)):
            comparing += 1
            if array[j] < array[minIndex]:
                minIndex = j
        swap += 1
        (array[i], array[minIndex]) = (array[minIndex], array[i])
    return comparing, swap


def shellSort(array):
    distance = len(array) // 2
    swap = 0
    comp = 0
    while distance > 0:
        for i in range(distance, len(array)):
            temp = array[i]
            j = i
            comp += 1
            while j >= distance and array[j-distance] > temp:
                array[j] = array[j - distance]
                swap += 1
                j -= distance
            array[j] = temp
            swap += 1
        distance //= 2
    return [comp,swap]


def binarySearch(array, toFind, start, end):
    while start <= end:
        middle = (start + end) // 2
        if array[middle] > toFind:
            end = middle - 1
        elif array[middle] < toFind:
            start = middle + 1
        else:
            return middle
    return start


def binaryInsertionSort(array):
    comp = swap = 0
    for i in range(1, len(array)):
        toInsert = array[i]
        pos = binarySearch(array,  toInsert, 0, i)
        for k in range(i, pos, -1):
            swap += 1
            array[k] = array[k-1]
        array[pos] = toInsert
        swap += 1
    return [comp, swap]


def cocktailSort(arr):
    n = len(arr)
    start = 0
    end = n - 1
    comp = swap = 0
    while True:
        # Перемещение наименьшего элемента в конец массива
        for i in range(start, end):
            comp += 1
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap += 1

        # Движение справа налево, чтобы поместить наибольший элемент в начало массива
        for i in range(end-1, start-1, -1):
            comp += 1
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap += 1

        # Перемещение левого края вправо, чтобы избавиться от уже отсортированных элементов
        start += 1
        end -= 1

        # Если нет перемещений, то сортировка завершена
        if start >= end:
            break
    return [comp, swap]


def mergeSort(arr):
    equation = swap = 0
    if len(arr) > 1:
        mid = len(arr)//2
        sub_array1 = arr[:mid]
        sub_array2 = arr[mid:]
        mergeSort(sub_array1)
        mergeSort(sub_array2)
        i = j = k = 0
        while i < len(sub_array1) and j < len(sub_array2):
            equation += 1
            if sub_array1[i] < sub_array2[j]:
                arr[k] = sub_array1[i]
                swap += 1
                i += 1
            else:
                arr[k] = sub_array2[j]
                swap += 1
                j += 1
            k += 1
        equation += 1
        while i < len(sub_array1):
            arr[k] = sub_array1[i]
            swap += 1
            i += 1
            k += 1
        equation += 1
        while j < len(sub_array2):
            arr[k] = sub_array2[j]
            swap += 1
            j += 1
            k += 1
    return [equation, swap]
