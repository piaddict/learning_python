def BubbleSort(dlist):
    size = len(dlist) - 1
    for element in range(size):
        for head in range(size - element):
            if (dlist[head] > dlist[head + 1]):
                (dlist[head], dlist[head + 1]) = (dlist[head + 1], dlist[head])

alist = [30, 50, 7, 40, 88, 15, 44, 55, 22, 33, 77, 90, 11, 66, 1, 85]
BubbleSort(alist)
print(alist)
