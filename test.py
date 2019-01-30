# with open('users.txt') as f:
#     user_info = f.readlines()
# for user in user_info:
#     user = user.strip('\n')
#     user_list = user.strip().split('|')
#     print(user_list[0])
#     print(user_list[1])

# i = input('enter')
# print(type(i))

# prod_info = {
#     'Apple':10,
#     'Tesla':700000,
#     'Mac_Pro':2000,
#     'Lenovo':4500,
#     'Chicken':15,
#     'book':100
# }
# # 打印商品名称和价格
# prod_list = list(prod_info.items())
# print(prod_list)
# print(prod_list[0][1])
# # 打印商品名称
# prod_name_list = list(prod_info.keys())
# print(prod_name_list)
# # 定义一个空的购物车列表
# shopping_list = []

# user = {'name':'a','psd':'b'}
# tag = True
# lock = 0
# while tag:
#     if lock < 3:
#         uname = input('enter name >>>')
#         pwd = input('enter psd >>>')
#         if uname == user['name'] and pwd == user['psd']:
#             print('login')
#             break
#         else:
#             lock +=1
#             print('error')
#             continue
#     else:
#         tag = False
#         print('lock')
#         break

# print("\033[31;1m你好麽，\033[0m我很好。。\n\n")
# print("\033[32;1m你好麽，\033[0m我很好。。")
# print("\033[33;1m你好麽，\033[0m我很好。。")
# print("\033[34;1m你好麽，\033[0m我很好。。")
# print("\033[35;1m你好麽，\033[0m我很好。。")
# print("\033[36;1m你好麽，\033[0m我很好。。")
# print("\033[37;1m你好麽，\033[0m我很好。。")
#
# #背景色
# print("\033[41;1m你好麽，\033[0m我很好。。")
# print("\033[42;1m你好麽，\033[0m我很好。。")
# print("\033[43;1m你好麽，\033[0m我很好。。")
# print("\033[44;1m你好麽，\033[0m我很好。。")
# print("\033[45;1m你好麽，\033[0m我很好。。")
# print("\033[46;1m你好麽，\033[0m我很好。。")
# print("\033[47;1m你好麽，\033[0m我很好。。")

func = lambda x,y,z=1:x+y+z
print(func(1, 2))

list2 = ['albert_NBA','james_NBA','zhangning_CUBA']
res = filter(lambda x:True if x.endswith('NBA') else False, list2)
print(list(res))

res = filter(lambda x:x.endswith('NBA'),list2)
print(list(res))

print('hello git')