import csv
import random

# 打开文件，设置文件名和表头
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'name', 'age', 'email'])

    # 生成12000条随机数据并写入文
    for i in range(1, 12):
        id = i
        name = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 6))
        age = random.randint(18, 50)
        email = '{}@example.com'.format(name)
        writer.writerow([id, name, age, email])
        print(id, name, age, email)
