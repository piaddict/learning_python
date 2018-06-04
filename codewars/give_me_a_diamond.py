# asterisk ("*") 문자로 만들어진 다이아몬드를 출력하라
# 두꺼운 부분에서 가장자리로 갈때 마다 2개씩 줄여서 출력한다

#  *
# ***
#  *

# 짝수나 음수를 입력받으면 None을 반환한다


def diamond(n):
    if n <= 0 or n % 2 == 0:
        return None

    result = ""
    for i in range(1, n * 2, 2):
        factor = i if i < n else 2 * n - i
        result += " " * ((n - factor) // 2)
        result += "*" * factor
        result += "\n"
    return result


expected = " *\n***\n *\n"


def test():
    assert diamond(3) == expected
