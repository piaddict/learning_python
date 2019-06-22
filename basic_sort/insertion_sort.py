def InsertionSort(dlist):
    size = len(dlist)
    for e in range(size):
        for t in range(e):
            if dlist[e - t] < dlist[e - t - 1]:
                dlist[e - t - 1], dlist[e - t] = dlist[e - t], dlist[e - t - 1]


target = [30, 50, 7, 40, 88, 15, 44]

InsertionSort(target)
print(target)
