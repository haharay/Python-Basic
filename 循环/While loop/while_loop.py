square = 1

while square <= 10:
    print(square)    # 此行执行10次
    square += 1      # 此行执行10次

print("Finished")  # 执行1次

square = 0
number = 1

while square < 81:
    square = number ** 2
    print(square)
    number += 1
