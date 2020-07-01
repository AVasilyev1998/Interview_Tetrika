

def get_multiples_of_five(n: int, pow: int) -> int:
    res = 0
    if n % pow == 0:
        if n >= pow**2:
            while n % pow == 0:
                n /= pow
                res += 1
            return res
        else:
            return 1
    else:
        raise ValueError('n is not divisible by degree')


def get_zeros(n: int) -> int:
    fives = 0
    for i in reversed(list(range(1, n+1))):
        tmp_n = i
        if tmp_n % 5 == 0:
            fives += get_multiples_of_five(tmp_n, 5)
    return fives


if __name__ == '__main__':
    print(get_zeros(5))
    print(get_zeros(12))
    print(get_zeros(25))
    print(get_zeros(10000000))
    # сложность алгоритма O(nlogn)

