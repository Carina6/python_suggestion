#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 387. First Unique Character in a String
def test_first_uniq_char():

    # java算法最佳 200ms
    def firstUniqChar(s):
        if len(s) == 0:
            return -1
        arr = []
        for i in range(26):
            arr.append(0)
        for i in range(len(s)):
            arr[ord(s[i])-ord('a')] += 1
        for i in range(len(s)):
            if arr[ord(s[i])-ord('a')] == 1:
                return i
        return -1

    # Python算法 最佳， 90+ms
    def firstUniqChar2(s):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        index = [s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1

    print(firstUniqChar2('aadadaad'))


# 1. two sum
def test_two_sum():
    # 时间复杂度为O(n^2) 5368 ms
    def two_sum(nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j

    # 时间复杂度为O(n) 44 ms
    def two_sum2(nums, target):
        value_dict = {}
        for i in range(len(nums)):
            if target-nums[i] in value_dict.keys():
                return value_dict.get(target-nums[i]), i
            else:
                value_dict[nums[i]] = i

    print(two_sum2([2, 7, 11, 15], 17))


