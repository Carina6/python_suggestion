#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2018/10/29 17:02
# @Author: hlliu

promos = []


def promotion(promo_func):
    promos.append(promo_func)
    print('decorator-{}'.format(promo_func))
    return promo_func


@promotion
def fidelity():
    return 'fidelity'


@promotion
def bulk_item():
    return 'bulk item'


@promotion
def large_order():
    return 'large order'


def best_promo():
    return 'best promo'


def main():
    print('running main()')
    print('promos ->', promos)
    print(fidelity())
    bulk_item()
    large_order()
    best_promo()


if __name__ == '__main__':
    main()