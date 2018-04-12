# feet per hour
def race(v1, v2, g):
    if v1 >= v2:
        return None

    s = g / ((v2 - v1) / 3600)
    h = int(s / 3600)
    m = int(s % 3600 / 60)
    s = int(s % 60)

    return [h, m, s]

# Test.assert_equals(race(720, 850, 70), [0, 32, 18])
# Test.assert_equals(race(80, 91, 37), [3, 21, 49])
# Test.assert_equals(race(80, 100, 40), [2, 0, 0])
