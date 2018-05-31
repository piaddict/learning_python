def binary_search(dlist, target):
    left = 0
    right = len(dlist) - 1
    while (left <= right):
        mid = (left + right) // 2
        if (dlist[mid] == target):
            return mid
        elif (dlist[mid] < target):
            left = mid + 1
        else:
            right = mid - 1
    return None

def binary_search_recursion(dlist, target, left, right):
    if (left > right): return None
    mid = (left + right) // 2

    if (dlist[mid] == target):
        return mid
    elif (dlist[mid] < target):
        left = mid + 1
    else:
        right = mid - 1

    return binary_search_recursion(dlist, target, left, right)

slist = [7, 15, 22, 30, 35, 40, 44, 55, 88]
print(binary_search(slist, 44))
print(binary_search_recursion(slist, 44, 0, len(slist)))
