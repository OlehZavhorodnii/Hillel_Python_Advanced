numbers = [1, 2, 3, 6, 7, 8]


def _filter(*args):
    yield from _filter(*args)
    return list()


n = _filter(numbers)
print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
