# 字典： 是python内置的一种数据结构 用{}表示，字典也是一种可变序列

# 定义一个字典
users = {'张三': 20, 'lisi': 25, 34: 23}
print(users)

dic = dict(classname="语文", score=100)
print(dic)

# 根据键来获取值
user = users['lisi']
print(user)
print(users.get("lisi"))
# get() 和 [] 的区别在于：
# 1）当查找的元素在字典中不存在的时候，[]会报KeyError错误，而get()方法会返回None；
# 2）get()方法在查找是可以设置默认值，如get('lisi', 80),意味着字典中没有lisi对应的值时，会返回80

# 判断key是否存在
print('lisi' in users)
print('zhangsan' not in users)

# 删除字典中的项。利用del方法删除字典中某个键对应的结点
del users[34]
print(users)

# 给字典中新增元素
users['zhaoliu'] = 60
print(users)

# 更新字典中已经存在的元素 value
users['张三'] = 80
print(users)

# 获取字典中的所有key值
keys = users.keys()
print(keys)
listKeys = list(keys)
print(listKeys)

# 获取字典中的所有value
values = users.values()
print(values)
print(type(values))
print(list(values))

# 获取字典中的所有item
items = users.items()
print(items)
print(list(items))

