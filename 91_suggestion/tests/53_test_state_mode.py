#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.state import stateful, State, behavior, switch


# 53：用状态模式美化代码
def test_state_mode():
    @stateful
    class User(object):
        # 退出状态类，定义退出状态时可进行的操作
        class signout(State):
            default = True  # 通过default 属性定义默认状态

            @behavior
            def signin(self, user, pwd):
                print('signin with user and pwd')
                switch(self, User.signin)

        # 登录状态类，定义登录状态时可进行的操作
        class signin(State):
            @behavior
            def move(self, dst):
                print(dst)

            @behavior
            def atk(self, other):
                print(other)

            @behavior
            def signout(self):
                print('signout!!')
                switch(self, User.signout)

    user = User()
    # user.move('move0')            # 默认状态为signout, 此时不能进行signin类中的操作（报错）
    user.signin('user', 'pwd')  # 调用此方法将状态转换为signin
    user.move('move1')  # 此时状态为signin， 可调用该类下的方法
    user.signout()  # 状态转为signout
    # user.move('move2')            # 不能进行signin类中的操作（报错）
