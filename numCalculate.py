# 1~10000001の合計
num = range(1, 1000001)
sum_num = sum(num)
print(sum_num)
print("min:", min(num))
print("max:", max(num))

# 1-20 の奇数
numOdd = list(range(1, 21, 2))
print("1−２０奇数：", numOdd)

# 创建一个列表，其中包含3~30内能被3整除的数字；再使用一个for 循环将这个列表中的数字都打印出来。
num3 = range(3, 31, 3)
for value in num3:
    print(value)
# 将同一个数字乘三次称为立方。例如，在Python中，2的立方用2**3 表示。请创建一个列表，其中包含前10个整数（即1~10）的立方，再使用一个for 循
# 环将这些立方数都打印出来。
num4 = [value**3 for value in range(1, 11)]
for num in num4:
    i = 1
    print(str(i) + "的立方" + str(num))
    i = i+1
