import re
#引用re模块
x_list =input('请输入数据：')
#利用input函数向x_list列表输入数据
m_list=re.split('\ |\,',x_list)
#通过re模块可使用多种分割符对x_list列表数据进行分割，暂时可使用的切割符有：空格以及逗号。
m=[]
#创建一个空列表
n=0
#设定列表数据的起始位数
for i in m_list:
    m.append(len(str(i)))
    n+=1
#借用for循环通过append函数得出m_list列表的长度以计算出数据位数并在插入到m列表的尾部
print(m)
#最后通过print函数输出m列表
