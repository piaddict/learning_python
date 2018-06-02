# 문자에 붙은 숫자를 1 증가시카는 함수를 작성하라.
# 만약 숫자가 없다면 문자 끝에 1을 붙여야 한다.

# Examples:
# foo -> foo1
# foobar23 -> foobar24
# foo0042 -> foo0043
# foo9 -> foo10
# foo099 -> foo100

# 주의: 앞자리 0의 개수는 유지되어야 함


def increment_string(strng):
    rstrng = list(strng)
    rstrng.reverse()
    idx = 0
    for idx, c in enumerate(rstrng):
        if not c.isnumeric():
            break
    nums = strng[-idx:]
    if idx == 0 and len(nums) != 1:
        return strng + "1"
    pnums = int(nums) + 1
    pnums = str(pnums).zfill(len(nums))
    return strng[:-idx] + pnums


# best practice

def better_increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "":
        return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))


def test():
    assert increment_string("foobar23") == "foobar24"
    assert increment_string("foo") == "foo1"
