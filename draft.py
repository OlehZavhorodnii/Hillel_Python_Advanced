class BadClass:

    def __init__(self, val=0):
        self.val = val
        self._hash = val

    # def __str__(self):
    #     return f'BadClass: {self.val}'

    def __eq__(self, other):
        return isinstance(other, BadClass) and self.val == other.val

    def __hash__(self):
        return hash(self._hash)


bad = BadClass()

even_worse = {bad}

assert (bad in even_worse)
# print(len(even_worse))
# print(bad in even_worse)

bad.val += 1
# even_worse.add(bad)
assert (bad in even_worse)
# print(len(even_worse))
# print(bad in even_worse)
print('yeah, we good!')

# bad.val += 2
# print('This is bad.val:', bad.val)

still_bad = BadClass(val=bad.val)
even_worse.add(still_bad)
# print(still_bad in even_worse)
assert (still_bad in even_worse)

