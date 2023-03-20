# if 语句
print('------------if 语句--------------')
# score = int(input('请输入成绩。。。'))
score = 78
if score < 60:
    print("成绩不合格")
elif 0 < score < 60:
    print("成绩合格")
elif 60 < score < 80:
    print('成绩良好')
else:
    print('成绩优异')
# for 循环语句
print('-----------for 循环语句------------')
print(list(range(1, 10, 2)))
print(10 in range(1, 10, 2))

sum = 0
for i in range(2, 101, 2):
    sum += i
print("sum", sum)

print('-----------for 循环语句 输出水仙花数------------')

for i in range(100, 1000):
    ge = i % 10
    shi = i // 10 % 10
    bai = i // 100
    if ge ** 3 + shi ** 3 + bai ** 3 == i:
        print("水仙花数：", i)
print('-----------for 循环语句 输出9*9乘法表------------')

for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, "*", i, "=", i * j, end="\t")
    print()
# 列表生成式
a = [i for i in range(1, 10)]
print(a)
