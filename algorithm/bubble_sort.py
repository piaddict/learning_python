def BubbleSort(list):
    size = len(list) - 1
    for element in range(size):
        for head in range(size - element):
            if (list[head] > list[head + 1]):
                (list[head], list[head + 1]) = (list[head + 1], list[head])

alist = [30, 50, 7, 40, 88, 15, 44, 55, 22, 33, 77, 90, 11, 66, 1, 85]
BubbleSort(alist)
print(alist)
