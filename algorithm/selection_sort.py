def SelectionSort(dlist):
    size = len(dlist)
    for element in range(size): # range는 반폐구간
        min_position = element
        for target in range(element + 1, size):
            if (dlist[target] < dlist[min_position]):
                min_position = target
        (dlist[element], dlist[min_position]) = (dlist[min_position], dlist[element])

alist = [30, 50, 7, 40, 88, 15, 44, 55, 22, 33, 77, 90, 11, 66, 1, 85]
SelectionSort(alist)
print(alist)
