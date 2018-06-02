# 폐구간내의 숫자 xy를 x^1 + y^2 ... 형식으로 나타낼 수 있는 숫자이면 반환
# 없다면 비어있는 리스트 반환


def calc_sum(number):
    nums_pow = list(n**(idx + 1) for idx, n in enumerate(number))
    return sum(nums_pow)


def sum_dig_pow(a, b):
    result = []
    for i in range(a, b+1):
        num = list(int(x) for x in str(i))
        if i == calc_sum(num):
            result.append(i)
    return result


# best practice

def filter_func(a):
    return sum(int(d) ** (i+1) for i, d in enumerate(str(a))) == a


def better_sum_dig_pow(a, b):
    return filter(filter_func, range(a, b+1))
