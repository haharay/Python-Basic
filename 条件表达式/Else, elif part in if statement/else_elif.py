x = 28

if x < 0:
    print('x < 0')                      # 仅当 x < 0 时才执行
elif x == 0:
    print('x is zero')                 # 如果x<0不为真，检查x==0。
elif x == 1:
    print('x == 1')                    # 如果x<0和x !=0都不为真，检查x ==1。
else:
    print('non of the above is true')

name = "John"

if name == "John":
    print(True)
else:
    print(False)
