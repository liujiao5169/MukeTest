# coding=utf-8

# 99乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print('%d×%d=%d\t' % (i, j, i*j), end='')
        # print('{}×{}={}\t'.format(i, j, i*j), end='')
        # print(i, "×", j, "=", i * j, '\t', end='')
    print()

# 100以内质数
# i为被除数
for i in range(2, 101):
    # j为除数
    for j in range(2, i+1):
        # 先判断能整除，再判断是本身，不是本身直接跳出j循环
        if i % j == 0:
            if i == j:
                print(i, '\t', end='')
            else:
                break



