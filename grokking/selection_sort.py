def find_smallest(list):
    smallest = list[0]
    smallest_index = 0

    for i in range(1, len(list)):
        if list[i] < smallest:
            smallest = list[i]
            smallest_index = i

    return smallest_index


def selection_sort(list):
    newList = []

    for i in range(len(list)):
        smallest_index = find_smallest(list)
        newList.append(list.pop(smallest_index))

    return newList


input_list = [4, 44, 218, 66, 2, 101, 55, 380, 54]
print(selection_sort(input_list))
