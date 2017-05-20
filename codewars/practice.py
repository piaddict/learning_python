def find_outlier(integers):
    odds = list()
    evens = list()
    for x in integers:
        if x%2==1:
            odds.append(x)
        else:
            evens.append(x)

    if len(odds) == 1:
        return odds[0]
    else:
        return evens[0]


print(find_outlier([2,6,8,10,3]))
