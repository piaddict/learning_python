# 약속에 10분 일찍 도착해서 잠시 산책하려 한다. 걷기 앱이 있어서 한 블럭을 지날때마다 걸어야 하는 방향을 알려준다. 한 블럭을 걷는데 1분씩 걸린다. 정확히 10분만에 시작점으로 다시 돌아오게 하는 방향을 알려주면 True, 시작점에 돌아오지 못하면 False를 반환하는 함수를 생성하라.

# 비어있는 배열이나, 명확한 방위 (n, s, e, w)가 들어있지 않은 배열은 받지 않는다.

from collections import Counter


def isValidWalk(walk):
    direction = {'n': 0, 's': 0, 'e': 0, 'w': 0}
    for block in walk:
        direction[block] += 1
    return True if (direction['n'] == direction['s'] and direction['e'] == direction['w'] and len(walk) == 10) else False


def better_isValidWalk(walk):
    direction = Counter(walk)
    return True if (direction['n'] == direction['s'] and direction['e'] == direction['w'] and len(walk) == 10) else False
