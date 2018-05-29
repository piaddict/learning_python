def SelectionSort(list):
    size = len(list)
    for element in range(0, size): # range는 반폐구간
        min_position = element
        for target in range(element + 1, size):
            if (list[target] < list[min_position]):
                min_position = target
        temp = list[element]
        list[element] = list[min_position]
        list[min_position] = temp

alist = [30, 50, 7, 40, 88, 15, 44, 55, 22, 33, 77, 90, 11, 66, 1, 85]
SelectionSort(alist)
print(alist)
