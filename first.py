import functools
import logging
from itertools import permutations
import os
from time import time

CURR_PATH = os.path.abspath(os.curdir)
LOGS_PATH = 'logs'
LOGGER_NAME = 'first.log'
fmt = '%(asctime)s - %(process)d - %(levelname)s - %(module)s - %(message)s'
formatter = logging.Formatter(fmt)
logging.basicConfig(filemode=logging.DEBUG, format=fmt)
file_handler = logging.FileHandler(os.path.join(CURR_PATH, LOGS_PATH, LOGGER_NAME))
file_handler.setFormatter(formatter)
logger = logging.getLogger('Timing')
logger.addHandler(file_handler)


def timer(function):
    @functools.wraps(function)
    def wraps(*args, **kwargs):
        start_time = time()
        res = function(*args, **kwargs)
        elapsed_time = time() - start_time
        logger.warning(f'{function.__name__} took {elapsed_time} seconds to complete')
        return res
    return wraps


# solution with itertools
@timer
def search_pairs_pythonic(array: list, k: int) -> list:
    """
    returns not only (a,b) pairs but (b,a)
    :param array:
    :param k:
    :returns list
    """
    check = set()
    res_list = []
    for i in set(permutations(array, 2)):
        if i[0] not in check and i[1] not in check:
            if i[0] + i[1] == k:
                res_list.append(i)
                check.update([i[0], i[1]])
    return res_list


# solution without itertools
@timer
def search_pairs(array: list, k: int) -> list:
    deductions_dict = {}
    res_list = []
    check_set = set()
    # creating dict with deductions as keys
    for i in array:
        if k-i not in deductions_dict:
            deductions_dict[k-i] = (i, 1)
        else:
            deductions_dict[k-i] = (i, deductions_dict[k-i][1]+1)

    for i in array:
        # checking to avid similar pairs (a,b) (b,a)
        if i not in check_set and k-i not in check_set:
            if i in deductions_dict:
                dict_value = deductions_dict[i][0]
                num_count = deductions_dict[i][1]
                if i != dict_value:
                    if i + dict_value == k:
                        res_list.append((i, dict_value))
                        check_set.update([i, dict_value])
                else:
                    if num_count > 1 and i + dict_value == k:
                        res_list.append((i, dict_value))
                        check_set.update([i, dict_value])

    return res_list


if __name__ == '__main__':
    array = list(range(-1800, 1800, 3))
    res = search_pairs(array, 900)
    print(f'search pairs res: {res}')
    res = search_pairs_pythonic(array, 900)
    print(f'search pairs pythonic res: {res}')
    # сложность решения без itertools O(2n) что соответствует O(n)
