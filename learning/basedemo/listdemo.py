# python 中的列表是一个可变的有序容器，它可以存储任意类型的元素，而且元素有序，容量可以扩充。
lst = ['hello', 'world', 98]
print(lst)
print(type(lst), type(lst[0]), type(lst[2]))
print(lst.index(98))

print('-------------list 元素查询----------------------')
for item in lst:
    print(item)
print(lst[0], lst[1], lst[2])
print(lst[-3], lst[-2], lst[-1])
