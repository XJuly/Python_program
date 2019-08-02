# -*- coding:utf-8 -*-
# Author: Jaylen
# date: 2019/8/2


import os
prod_info = [
    ['Apple',10],
    ['Tesla',700000],
    ['Mac_Pro',2000],
    ['Lenovo',4500],
    ['Chicken',15],
    ['book',100]
]


login = False
tag = True
current_user = ''
shopping_list = {}
while True:
    print('''
    请选择：
    1. 登录
    2. 注册
    3. 购物
    ''')

    choice = input('>>>:')
    if choice == '1':
        count = 0
        while not login:
            if count == 3:
                print('尝试次数过多！')
                # 存入黑名单
                with open('blacklist.txt','a+') as f1:
                    f1.write(user)
                break
            # 交互界面
            user = input('username:')
            pwd = input('password:')
            with open('users.txt') as f2, open('blacklist.txt') as f3:
                blacklist = [word.strip() for word in f3.readlines()]
                if user not in blacklist:
                    for line in f2:
                        if line.startswith(user):
                            info = line.strip().split('|')
                            name = info[0]
                            password = info[1]
                            account = int(info[2])

                            if user == name and pwd == password:
                                print('用户%s登录成功！请选择3开始购物！' %name)
                                login = True
                                current_user = user
                                break
                else:
                    print('该账户已被锁定！请使用其他账户！')
                    continue

                if not login:
                    count += 1
                    print('用户名或密码错误！')
        else:
            print('您已登录！')

    elif choice == '2':
        if not current_user:
            user = input('username:').strip()
            while user and not login:
                with open('users.txt') as file:
                    for line in file:
                        if line.startswith(user):
                            info = line.strip().split('|')
                            name = info[0]
                            if user == name:
                                print('该用户名已存在！')
                                user = ''
                                break
                if not user:
                    break
                pwd1 = input('password:')
                pwd2 = input('password again:')
                while pwd1 == pwd2:
                    account = input('注册成功!请输入您的余额：')
                    if not account.isdigit():
                        continue

                    with open('users.txt', 'a+') as f4:
                        f4.write('\n' + user +'|' + pwd1 + '|' + account)
                    login = True
                    account = int(account)
                    break
                else:
                    print('两次密码不一致，请重试！')
        else:
            print('您已登录！请输入3购物或q退出！')

    elif choice == '3':
        if not login:
            print('请先登录！')

        while tag:
            for index, product in enumerate(prod_info):
                print(index, product)
            ind = input('输入商品编号购物，输入q退出>>:').strip()
            if ind.isdigit():
                ind = int(ind)
                if ind < 0 or ind >= len(prod_info):
                    print('无此选项！')
                    continue
                else:
                    product = prod_info[ind][0]
                    price = prod_info[ind][1]
                    if account >= price:
                        insure = input('是否确认购买%s：%s元 (y/n)' % (product, price))
                        if insure in ['y','Y','yes','Yes','YES']:
                            if product in shopping_list:
                                shopping_list[product]['count'] += 1
                            else:
                                shopping_list[product] = {'price': price , 'count' : 1}
                            account -= price

                    else:
                        print('余额不足！')
                    print('Your shopping list:', shopping_list)
            elif ind == 'q':
                tag = False
                print('您目前购买了如下商品：')
                print('id          商品                   数量             单价               总价')
                total_cost = 0
                for i, key in enumerate(shopping_list):
                    print('%s%18s%18s%18s%18s' % (i, key,shopping_list[key]['count'], shopping_list[key]['price'],
                        shopping_list[key]['price'] * shopping_list[key]['count']))

                    total_cost += shopping_list[key]['price'] * shopping_list[key]['count']
                print('''
                您的总花费为：%s
                余额为：%s''' %(total_cost,account))


                with open('users.txt') as file1, open('newusers.txt','w') as file2:
                    for line in file1:
                        if line.startswith(user):
                            user_info = line.strip().split('|')
                            if user == user_info[0]:
                                user_info[2] = str(account)
                            line = '|'.join(user_info) + '\n'
                        file2.write(line)
                os.remove('users.txt')
                os.rename('newusers.txt', 'users.txt')

    elif choice == 'q':
        break
    else:
        print('非法输入！')

