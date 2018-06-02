# Two tortoises named A and B must run a race. A starts with an average speed of 720 feet per hour. Young B knows she runs faster than A, and furthermore has not finished her cabbage.
# When she starts, at last, she can see that A has a 70 feet lead but B's speed is 850 feet per hour. How long will it take B to catch A?
# More generally: given two speeds v1 (A's speed, integer > 0) and v2 (B's speed, integer > 0) and a lead g (integer > 0) how long will it take B to catch A?
# The result will be an array [hour, min, sec] which is the time needed in hours, minutes and seconds (round down to the nearest second).
# If v1 >= v2 then return nil, nothing, null, None or {-1, -1, -1} for C++, C, Go, Nim, [] for Kotlin.

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
