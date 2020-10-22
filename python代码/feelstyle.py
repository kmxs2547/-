# 导入标准库   import 相当于C预言的 include
import math
print(math.gcd(56,64))  #计算最大公约数

from math import gcd      #细节引用，仅引用math下的gcd，可以提高运算速度
print(gcd(56,64))

from math import gcd as k     #给导入对象起个名字：k
print(k(56,64))

x = [1,2,3]
print(type(x))
print(type(x)==list)    #内置函数type（）查看变量

# 幂乘运算
m = 2 ** 3  #2的3次方
s = 5 ** 2  #5的2次方
print(m,s)

a = 'tom said,'
b = '''"let's go."'''   #三引号下的双引号才是字符串，双引号下的单引号才是字符串
c = a+b
print(c)
print(c*3)
print(c + 'morning')


