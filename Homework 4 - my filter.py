def get_element(*args):  # get element from the sequence
    yield from iter(*args)


def _filter(func, *args):  # select the desired elements from the sequence
    element = get_element(*args)
    for n in element:
        if func(n):
            yield n


number_list = range(-5, 5)
more_than_zero = _filter(lambda x: x > 0, number_list)
print(more_than_zero)  # print the object of the function
more_than_zero = list(_filter(lambda x: x > 0, number_list))
print(more_than_zero)  # print the result of the function

more_than_zero1 = list(filter(lambda x: x > 0, number_list))
print(more_than_zero1)  # the result of the built-in function filter

