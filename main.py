from typing import List

def merge_sort(arr: List[int]) -> None:
    n = len(arr)
    dummy = [0] * n
    i = 1
    while i < n:
        for low in range(0, n, 2 * i):
            mid, high = low + i - 1, min(low + 2 * i - 1, n - 1)
            j, k = low, mid + 1
            for l in range(low, high + 1):
                if j > mid:
                    dummy[l] = arr[k]
                    k += 1
                elif k > high:
                    dummy[l] = arr[j]
                    j += 1
                else:
                    if arr[j] <= arr[k]:
                        dummy[l] = arr[j]
                        j += 1
                    else:
                        dummy[l] = arr[k]
                        k += 1

            arr[low:high + 1] = dummy[low:high + 1]
        i <<= 1

if __name__ == '__main__':
    with open('list.txt', 'r') as f:
        a = list(map(int, f.read().split()))

    print('List before sorting', a)
    merge_sort(a)
    print('List after sorting', a)

    with open("list.txt", "w") as f:
        f.write(" ".join(map(str, a)))
