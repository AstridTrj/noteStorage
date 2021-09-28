import pandas as pd
import numpy as np


def find_number_lis(nums: list, k: int):
    N = len(nums)
    if N <= 1:
        return N
    lengths = [0] * N
    counts = [1] * N

    res = 0
    while len(nums) >= k:
        for j, num in enumerate(nums):
            for i in range(j):
                if nums[i] < nums[j]:
                    if lengths[i] >= lengths[j]:
                        lengths[j] = 1 + lengths[i]
                        counts[j] = counts[i]
                    elif lengths[i] + 1 == lengths[j]:
                        counts[j] += counts[i]
        res += len([i for i, c in enumerate(counts) if counts[i] == k])
        nums.pop(0)
    return res


if __name__ == "__main__":
    nk = input().split(' ')
    n, k = int(nk[0]), int(nk[1])
    nums_str = input().split(' ')
    nums = [int(i) for i in nums_str]
    res = find_number_lis(nums, k)
    print(res % 1000007)