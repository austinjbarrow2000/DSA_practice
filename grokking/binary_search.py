# Austin Barrow


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        if list[mid] == item:
            return mid
        elif list[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


list = [1, 15, 22, 23, 68, 101, 305]

print(binary_search(list, 305))
