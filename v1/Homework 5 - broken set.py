class BadClass:

    def __init__(self, val=0):
        self.__val = val

    def get_val(self):
        return self.__val

    def __eq__(self, other):
        return isinstance(other, BadClass) and self.get_val() == other.__val

    def __hash__(self):
        return hash(self.__val)


bad = BadClass()
even_worse = {bad}
assert (bad in even_worse)
even_worse.add(BadClass(1))
assert (bad in even_worse)
print('yeah, we good!')

still_bad = BadClass(2)
even_worse.add(still_bad)
assert (still_bad in even_worse)

