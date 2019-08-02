# -*- coding:utf-8 -*-
# Author: Jaylen
# date: 2019/8/2

menu = {
    '北京':{
        "昌平":{
            "沙河":["oldboy","test"],
            "天通苑":["链家地产","我爱我家"]
        },
        "朝阳":{
            "望京":["奔驰","陌陌"],
            "国贸":["CICC","HP"],
            "东直门":["Advent","飞信"],
        },
        "海淀":{}
    },
    '山东':{
        "德州":{},
        "青岛":{},
        "济南":{}
    },
    '广东':{
        "东莞":{},
        "常熟":{},
        "佛山":{}
    }
}

current_layer = menu
parent_layer = []
tag = True
while tag:
    if current_layer:
        for key in current_layer:
            print(key)
    else:
        print('已到达底层！')
    choice = input('请输入您的选择：').strip()
    if choice in current_layer:
        parent_layer.append(current_layer)
        if isinstance(current_layer,list):
            print('已到达底层！')
        else:
            current_layer = current_layer[choice]

    elif choice == 'b':
        if parent_layer:
            current_layer = parent_layer.pop()

    elif choice == 'q':
        print('您已退出！')
        tag = False

    else:
        print('输入不合法！')