def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]

        smaller = [i for i in arr[1:] if i <= pivot]
        bigger = [i for i in arr[1:] if i > pivot]

        return quicksort(smaller) + [pivot] + quicksort(bigger)


print(quicksort([1, 5, 2, 0, 3, 9, 8]))
