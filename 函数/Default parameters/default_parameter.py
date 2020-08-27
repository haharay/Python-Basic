def multiply_by(a, b=2):
    return a * b

print(multiply_by(3, 47))
print(multiply_by(3))    # 使用b参数的默认值调用函数


def hello(subject, name="John"):
    print("Hello %s! My name is %s" % (subject, name))

hello("PyCharm", "Jane")    # 以 "PyCharm "为主题参数，"Jane "为名称，调用 "hello "函数。
hello("PyCharm")            # 调用 "hello "函数，以 "PyCharm "为参数，默认值为名称。
