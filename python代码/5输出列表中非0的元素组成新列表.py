#-*- codeing = utf-8 -*-  '''防止中文乱码'''
#@Time ： 2020-09-24 22:25  '''自动生成时间'''
#@Author : 陈泽槐
#@File : zuo ye.py
#@Software : PyCharm '''代码环境'''

X_list=(input('请输入一串字符串，用逗号隔开：').split(','))
a=[]
for i in X_list:
    if i!='0':
        a.append(i)
print('等价于True的元素为：',a)