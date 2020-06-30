from time import time

FILENAME = 'names.txt'


# If only eng letters in names.txt
def get_alphabet_dict() -> dict:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return dict(zip(alphabet, range(1, len(alphabet)+1)))


def timer(function):
    def wraps(*args, **kwargs):
        start_time = time()
        res = function(*args, **kwargs)
        elapsed_time = time() - start_time
        print(f'{function.__name__} took {elapsed_time} seconds to complete')
        return res
    return wraps


def get_names(filename: str) -> list:
    with open(FILENAME, 'r') as reader:
        names = [i.strip('"').strip("'") for i in reader.readline().split(',')]
        return names


def get_sum_of_letters(name: str) -> int:
    alphabet_dict = get_alphabet_dict()
    return sum([alphabet_dict[letter.lower()] for letter in name])


@timer
def processing_names(names: list) -> int:
    result = 0
    for num, name in enumerate(names, start=1):
        name_sum = get_sum_of_letters(name)
        composition = name_sum * num
        result += composition
    return result


if __name__ == '__main__':
    res = processing_names(get_names(FILENAME))
    print(res)
    # names = get_names(FILENAME)
    # print(names[0])
    # print([(alphabet_dict[letter.lower()], letter) for letter in names[0]])
    # print(processing_names(names[0:1]))
