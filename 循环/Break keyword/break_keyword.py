count = 0

while True:  # 此条件不可能为False
    print(count)
    count += 1
    if count >= 5:
        break           # 如果count >= 5，退出循环


zoo = ["lion", "tiger", "elephant"]
while True:                         # 此条件不可能为False
    animal = zoo.pop()       # 从列表末尾抽取一个元素
    print(animal)
    if animal == "elephant":
        break           # 退出循环
