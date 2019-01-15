#!/usr/bin/python3
# -*- coding: utf-8 -*-


from math import *


def ExpcalcBot(string):
    try:
        print('your enter answer is :', eval(string))
    except NameError:
        print('the express you enter is invalid')
    print("hi,I'm ExpcalcBot, please input your express or enter e to end.")

    inputstr=''
    while(1):
        print('please enter a number or operation.enter c to complete: ')
        inputstr = input()
        if inputstr == str('c'):
            sys.exit()
        elif repr(inputstr) != repr(''):
            ExpcalcBot(inputstr)
            inputstr=''
