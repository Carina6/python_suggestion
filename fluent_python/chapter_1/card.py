#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2018/10/29 15:06
# @Author: hlliu
import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

ranks = [str(n) for n in range(1, 10)] + list('JQKA')
suits = 'spades diamonds clubs hearts'.split()

'''
一个类包含__len__,__getitem__方法, 
len,getitem 操作的是成员变量list，实现这两个特殊方法，使该类相当于一个list，具有list的操作
'''


class FrenchDeck:

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, item):
        return self.cards[item]

    # def __contains__(self, item):
    #     return True


# collections.namedtuple
def test_card1():
    beer_card = Card('7', 'diamonds')
    print(beer_card)


# 切片
def test_card2():
    deck = FrenchDeck()
    print(len(deck))
    print(deck[0])
    print(deck[-1])

    print(deck[:3])
    print(deck[12::13])


def test_card3():
    deck = FrenchDeck()
    print(choice(deck))


# iteration 特性,遍历
def test_card5():
    deck = FrenchDeck()
    for c in deck:
        print(c)


# in 特性：如果实现了__contain__方法，使用in的时候调用__contain__方法，
# 如果没有实现，则遍历比较
def test_card6():
    deck = FrenchDeck()
    print(Card('Q', 'hearts') in deck)
    print(Card('q', 'hearts') in deck)


# 反转
def test_card7():
    deck = FrenchDeck()
    for c in reversed(deck):
        print(c)


# 排序 此处根据 黑 红 梅 光 排序
def test_card8():
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def spades_high(card):
        rank_value = ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]

    deck = FrenchDeck()
    sorted_deck = sorted(deck, key=spades_high)
    for d in sorted_deck:
        print(d)
