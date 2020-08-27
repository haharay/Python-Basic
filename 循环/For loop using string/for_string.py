hello_world = "Hello, World!"

for ch in hello_world:    # 输出hello_world的每个字符
    print(ch)

length = 0      # 初始化长度变量

for ch in hello_world:
    length += 1     # 在每次循环中长度增加1.

print(len(hello_world) == length)
