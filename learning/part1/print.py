# 输出数字类型
print(520)
print(98.5)

# 输出字符串，注意：字符串必须带引号，'' 和 "" 是等价的
print("hello world")
print('I love you!')

# 输入表达式
print(1 == 2)
print(1 + 3)

# 输出到文件
# 1:"a+" 的意思是指定目录不存在当前文件时会自动新建文件
# 2:输出到文件时必须使用 file=xxxx
fp = open('/Users/lexu/Desktop/works/leaning/python/learning/part1/text.txt', 'a+')
print("hello world", file=fp)
fp.close()

# 不换行输出
print('hello', 'world', 'python')

