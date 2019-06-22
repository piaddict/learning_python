def ShellSort(dlist):
    n = len(dlist)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = dlist[i]
            j = i

            while j >= gap and dlist[j-gap] > temp:
                dlist[j] = dlist[j-gap]
                j -= gap

            dlist[j] = temp
        gap //= 2


target = [30, 50, 7, 40, 88, 15, 44]

ShellSort(target)
print(target)
