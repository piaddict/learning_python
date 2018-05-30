# 알파벳 순서대로 점수가 매겨진다 (a = 1, b = 2, c = 3 etc.)

# 가장 높은 점수를 매긴 단어를 반환한다. 동점이면 앞에 있는 단어를 반환한다.
# 모든 입력은 소문자로 처리한다.

def high(x):
    xx = x.split()
    score = []
    for word in xx:
        score.append(sum([ord(char) - 96 for char in word]))
    pos = score.index(max(score))
    return xx[pos]

def better_high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
