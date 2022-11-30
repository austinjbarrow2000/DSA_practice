def sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr.pop() + sum(arr)


print(sum([1, 2, 3, 4, 5]))


def arr_length(arr):
    if len(arr) == 0:
        return 0
    else:
        arr.pop()
        return 1 + arr_length(arr)


print(arr_length([1, 2, 3, 4, 5]))


def max_arr(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    temp_max = max(arr[1:])
    return arr[0] if arr[0] > temp_max else temp_max


print(max_arr([1, 2, 3, 7, 5]))


def binary_search(arr, low, high, item):

    if high >= low:
        mid = (low + high) // 2

        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            return binary_search(arr, mid + 1, high, item)
        else:
            return binary_search(arr, low, mid - 1, item)
    else:
        return None


print(binary_search([1, 2, 3, 7, 5], 0, (len([1, 2, 3, 7, 5]) - 1), 2))
