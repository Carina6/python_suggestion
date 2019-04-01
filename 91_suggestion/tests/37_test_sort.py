#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 37：按需选择 sort() 或者 sorted()
def test_sort():
    print()
    persons = [{'name': 'Jon', 'age': 32}, {'name': 'Alan', 'age': 50}, {'name': 'Bob', 'age': 23}]

    # sorted 根据指定key排序，此例根据name正序，age倒序排列，不会改变person列表的原始值
    persons_sorted = sorted(persons, key=lambda x: (x['name'], -x['age']))
    print(persons_sorted)
    print(persons)

    # sort 根据指定key排序，会改变person列表的原始值
    persons.sort(key=lambda x: (x['name'], -x['age']))
    print(persons)