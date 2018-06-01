# 고차함수를 연결한 단항 함수를 생성하려고 한다.

# chained([a,b,c,d])(input)
# Should yield the same result as d(c(b(a(input))))

def chained(functions):
    def infunc(x):
        for func in functions:
            x = func(x)
        return x
    return infunc


def f1(x): return x*2
def f2(x): return x+2
def f3(x): return x**2

chained([f1,f2,f3])(1)

def test():
    assert chained([f1,f2,f3])(1) == 16
