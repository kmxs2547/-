x = int(input("请输入一个自然数："))
if type(x) == int:
    print("二进制："+bin(x))
    print("八进制：" + oct(x))
    print("十六进制：" + hex(x))
else:
    print("输入错误")