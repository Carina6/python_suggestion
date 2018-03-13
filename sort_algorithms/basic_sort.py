#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
堆排序
已知下标为i的节点
父节点下标为：(i-1)/2
左子节点下标：2*i+1
右子节点下标：2*i+2
最后一个非叶子节点下标，即最后一个数的下标的父节点：(n-2)/2, n为数组长度
'''
def test_heap_sort():
    def heap_sort(nums):
        init_heap(nums)
        sort_nums = []
        for i in range(len(nums) - 1, -1, -1):
            sort_nums.append(nums[0])

            nums[0], nums[i] = nums[i], nums[0]
            nums.remove(nums[i])

            adjust_heap(nums, 0, i)
        return sort_nums

    # 初始化堆, 从最后一个非叶子节点（下标：(n-2)/2, n为数组长度）开始往前调整
    def init_heap(nums):
        for i in range((len(nums)-2)//2, -1, -1):
            adjust_heap(nums, i, len(nums))

    # 调整第i个节点的值，以及其后所影响的节点
    def adjust_heap(nums, i, n):
        j = 2 * i + 1
        while j < n:
            if j + 1 < n and nums[j] < nums[j+1]:
                j += 1
            if nums[j] < nums[i]:
                break
            nums[i], nums[j] = nums[j], nums[i]
            i = j
            j = 2 * i + 1

    print(heap_sort([1, 2, 3, 4, 5, 6, 7, 8, 9]))
