# 练习一、打印金字塔
max_level = 5
for current_level in range(1, max_level + 1):
    for i in range(max_level - current_level):
        print(' ', end='')  # 在一行中连续打印多个空格
    for j in range(2 * current_level - 1):
        print('*', end='')  # 在一行中连续打印多个空格
    print()


# 练习二、去重
l = [

    {'name': 'albert', 'age': 18, 'sex': 'male'},

    {'name': 'james', 'age': 35, 'sex': 'male'},

    {'name': 'taylor', 'age': 25, 'sex': 'female'},

    {'name': 'albert', 'age': 18, 'sex': 'male'},

    {'name': 'albert', 'age': 18, 'sex': 'male'},

]
# print(set(l))  # 报错:unhashable type: 'dict'
s = set()
l1 = []
for item in l:
    val = (item['name'], item['age'], item['sex'])
    if val not in s:
        s.add(val)
        l1.append(item)
print(l1)


# 定义函数,既可以针对可以hash类型又可以针对不可hash类型(下一阶段课程)
def func(items, key=None):
    s = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in s:
            s.add(val)
            yield item

print(list(func(l, key=lambda dic: (dic['name'], dic['age'], dic['sex']))))

# 练习三
