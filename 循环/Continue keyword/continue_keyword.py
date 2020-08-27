for i in range(5):
    if i == 3:
        continue   # 对当前循环i值，跳过剩余的代码。
    print(i)

for x in range(10):
    if x % 2 == 0:
        continue   # 对这次寻哈，跳过print(x)
    print(x)
