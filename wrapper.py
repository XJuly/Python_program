# -*- coding:utf-8 -*-
# Author: Jaylen
# date: 2019/8/12


# 装饰器，认证功能，用户密码来源于文件，设定超时时间，超时需重新登录
import time

current_user = {
    'user': None,
    'login_time':None,
    'timeout':10
}


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = float(current_user['login_time'])
        res = func(*args, **kwargs)
        stop_time = time.time()
        t = stop_time - start_time
        print('已登录时间%.3ss' %t)
        funcs_dict = {
                '1':welcome,
                '2':shopping
        }
        while t < current_user['timeout']:
            choice = input('选择执行函数：')
            funcs_dict[choice]()
        else:
            current_user['user'] = None
            auth(func)

        return res

    return wrapper


def auth(func):
    def wrapper(*args, **kwargs):
        if current_user['user']:
            print('login already')
            return func(*args,**kwargs)

        name = input('username>>:').strip()
        pwd = input('pwd>>:').strip()
        with open('users.txt') as f:
            for line in f:
                if line.startswith(name):
                    info = line.strip().split('|')
                    if name == info[0] and pwd == info[1]:
                        print('login succeed')
                        current_user['user'] = name
                        current_user['login_time'] = time.time()
                        res = func(*args, **kwargs)
                        return res
                    else:
                        print('error')
                        break

    return wrapper


@auth
@timer
def welcome():
    print('welcome')


@auth
@timer
def shopping():
    print('shopping')



welcome()
shopping()