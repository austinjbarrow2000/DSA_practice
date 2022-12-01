def merge(arr_one, arr_two):
    arr_result = []

    while len(arr_one) > 0 and len(arr_two) > 0:
        if arr_one[0] < arr_two[0]:
            arr_result.append(arr_one.pop(0))

        else:
            arr_result.append(arr_two.pop(0))

    while len(arr_one) > 0:
        arr_result.append(arr_one.pop(0))

    while len(arr_two) > 0:
        arr_result.append(arr_two.pop(0))

    return arr_result


def mergesort(arr):
    if len(arr) < 2:
        return arr
    else:
        mid = len(arr) // 2
        arr_one = arr[:mid]
        arr_two = arr[mid:]

        arr_one = mergesort(arr_one)
        arr_two = mergesort(arr_two)
        return merge(arr_one, arr_two)


print(mergesort([1, 5, 2, 0, 3, 9, 8]))
