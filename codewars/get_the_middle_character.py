# 가운데 글자를 반환하는 함수를 작성하려 한다.
# 전체 글자 길이가 짝수면 가운데 두 글자, 홀수면 가운데 한 글자를 반환한다.

#Examples:
# Kata.getMiddle("test") should return "es"
# Kata.getMiddle("testing") should return "t"
# Kata.getMiddle("middle") should return "dd"
# Kata.getMiddle("A") should return "A"

def get_middle(s):
    size = len(s) // 2
    asize = len(s) % 2 - 1
    return s[size + asize : size + 1]
