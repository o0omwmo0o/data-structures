"""
三路快速排序（重写版）
由 Notebook 改写为 Python 脚本。
"""

import random


"""
随机快速排序（Randomized QuickSort）
特点：通过随机选择pivot，降低最坏情况发生概率
"""
import random
import time

def randomized_partition(arr, low, high):
    # 1. 随机选择pivot
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low - 1

    # 2. 标准partition过程
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # 3. 放置pivot
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def randomized_quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)


# 测试代码
if __name__ == "__main__":
    arr = [2,34,56,3,24,53,45,35,99,87]
    print("原数组：", arr)

    start = time.time()
    randomized_quicksort(arr, 0, len(arr) - 1)
    end = time.time()

    print("排序后：", arr)
    print("耗时：%.6f秒" % (end - start))

# -*- coding: utf-8 -*-
"""
三路快速排序（3-Way QuickSort）
特点：特别适用于大量重复元素
"""

import random
import time


def three_way_quicksort(arr, low, high):
    if low >= high:
        return

    # 1. 随机选择pivot
    pivot_index = random.randint(low, high)
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
    pivot = arr[low]

    # 2. 三路划分
    lt = low        # < pivot 区间右边界
    gt = high       # > pivot 区间左边界
    i = low + 1     # 当前扫描位置

    while i <= gt:
        if arr[i] < pivot:
            arr[i], arr[lt] = arr[lt], arr[i]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1

    # 3. 递归处理
    three_way_quicksort(arr, low, lt - 1)
    three_way_quicksort(arr, gt + 1, high)


# 测试代码
if __name__ == "__main__":
    # 构造大量重复数据
    arr = [84,3,5,6,6,34,8,98,8]
    print("原数组：", arr)

    start = time.time()
    three_way_quicksort(arr, 0, len(arr) - 1)
    end = time.time()

    print("排序后：", arr)
    print("耗时：%.6f秒" % (end - start))