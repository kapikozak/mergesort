import logging
from typing import List

logging.basicConfig(level=logging.INFO)

def merge_sort(a: List[int], f: int|None = None, l: int|None = None) -> None:
    def merge(f_start: int, f_end: int, s_start: int, s_end: int) -> None:
        i, j, k = f_start, s_start, f_start
        while i <= f_end and j <= s_end:
            if a[i] <= a[j]:
                b[k] = a[i]
                i += 1
            else:
                b[k] = a[j]
                j += 1
            k += 1

        if i <= f_end:
            b[k:s_end + 1] = a[i:f_end + 1]
        elif j <= s_end:
            b[k:s_end + 1] = a[j:s_end + 1]

        a[f_start:s_end + 1] = b[f_start:s_end + 1]

    if f is None:
        logging.info('f argument was not specified, code runs with 0')
        f = 0
    if l is None:
        logging.info(f'l argument was not specified, code runs with {len(a)-1}')
        l = len(a) - 1

    n = l - f + 1
    b = [0] * len(a)
    size = 1
    while size < n:
        first = f
        while first <= l - size:
            first_end = first + size - 1
            second = first_end + 1
            second_end = min(second + size - 1, l)
            merge(first, first_end, second, second_end)
            first += 2 * size
        size <<= 1
#bottom up merge sort


if __name__ == '__main__':
    with open('list.txt', 'r') as f:
        a = list(map(int, f.read().split()))

    print('List before sorting', a)
    merge_sort(a)
    print('List after sorting', a)

    with open("list.txt", "w") as f:
        f.write(" ".join(map(str, a)))
