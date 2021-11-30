def get_denominator(file_name):
    try:
        with open(file_name, 'r') as f:
            denominator = int(f.read())
        if denominator == 0:
            raise ValueError
        # или, если учитывать условие, что наше число в файле находиться в диапазоне от 1 до 100:
        # if denominator not in range(1, 101):
        #     raise ValueError
    except FileNotFoundError:
        print('File not found')
    except ValueError:
        print('Wrong value')
    return denominator


def get_list_of_numbers(denominator):
    list_of_integer = [i * 1 for i in range(1, 101)]
    list_of_numbers = []
    try:
        for i in list_of_integer:
            if i % denominator == 0:
                list_of_numbers.append(i)
    except (ZeroDivisionError, TypeError):
        pass
    return list_of_numbers


def get_sum(list_of_numbers):
    number = sum(list_of_numbers)
    return number


def write_result(number, name_of_result_file):
    with open(name_of_result_file, 'w') as f:
        f.write(str(number))


if __name__ == '__main__':
    denominator = get_denominator('d.txt')
    list_of_numbers = get_list_of_numbers(denominator)
    number = get_sum(list_of_numbers)
    write_result(number, 'result_of_HW4')
