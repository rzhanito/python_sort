from sort_functions import fillArray
import time

# Function to find the partition position


def partition(array, low, high):
    comp = swap = 0

    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        comp += 1
        if array[j] <= pivot:

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
            swap += 1

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    swap += 1

    # Return the position from where partition is done
    return [i + 1, comp, swap]

# function to perform quicksort


def quickSort(array, low, high):
    comp = swap = 0
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi, comp, swap = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)
    return [comp, swap]


arr = []
fillArray(arr, 1000000)
print(f"Исходный массив: {arr}")
startTime = time.time()
equation, swap = quickSort(arr, 0, len(arr)-1)
print(f"Итоговый массив: {arr}")
print(f"Количество сравнений: {equation} Количество перестановок: {swap}")
endTime = time.time()
totalTime = float("{:.9f}".format(endTime - startTime))
print(f"Время выполнения функции: {totalTime}")
