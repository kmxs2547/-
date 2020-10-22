X_list=(input('请输入一串数字，用逗号隔开：').split(','))
a=[]
for i in X_list:
    a.append(i)
maxlength = max(len(i) for i in a)
longest_strings = [i for i in a if len(i) == maxlength]
unique_longest_strings = list(set(longest_strings))
max_value = max(unique_longest_strings)
print(max_value)
print(max(a))




# a = input('请输入一组数据，用逗号隔开：')
# b=list(a)
#
# # k =[12,234,456456,65776,6788]
# # b = max(k)
# k = max(b)
# print(type(b))
# print(k)








# import ast
# lists = ast.literal_eval(input("请输入列表，使用逗号隔开: "))
# # maxb = max(lists)
# # print(maxb)
# print(lists)


# a = []
# while 1:
#     s = input('请输入数字，用逗号隔开:')
#     if s == '':
#        break
#     else:
#         a.append(s)
# def funcrepeat(a):
#     if list(set(a)) == a:
#         print('你输入的值不重复')
#     else:
#         print('你输入的值重复了')
#     print(a)
# funcrepeat(a)








# len_value = max(a,key=lambda item:len(str(item)))
# lenk=[]
# for i in len_value:
#     lenk.append(i)
#
# max_value = max(lenk)
# print(len_value)
# print(lenk)
# print('这组数中的最大值为：',max_value)
# print(type(a))





# b = max(a)
# b=sorted(a,key=lambda  item:len(str(item)),reverse=True)
# print('从大到小排序为：',b)




# list01 = [4, 5, 65, 76, 7, 8]
# # 把第一个元素作为最大值
# max_value = list01[0]
# # 从第二个开始对比
# for i in range(1, len(list01)):
#     if max_value < list01[i]:
#         max_value = list01[i]
#
# print(max_value)



# def max2(list):
#      k=list(0)
#      for i in range(1,len(list)):
#          if list[i] > k:
#              k = list[i]
#      return k


# k=['343','123','345','999']
# print(max(k))