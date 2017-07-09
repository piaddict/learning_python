test = [None] * 5
for i in range(5):
    def inner():
        return i
    test[i] = inner

for j in range(5):
    print(test[j]())
# => 4 4 4 4 4

test = [None] * 5
for i in range(5):
    def outer(i):
        def inner():
            return i
        return inner
    test[i] = outer(i)

for j in range(5):
    print(test[j]())
# => 0 1 2 3 4
