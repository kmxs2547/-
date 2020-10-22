#输出四位的列表
a = [x for x in range(1,101)]
npk =[]
for y in range(0,len(a),4):
    npk.append(a[y:y+4:1])
print(npk)
# print([a[y:y+4:1] for y in range(0,len(a),4)])


# b = [x for x in range(1,101)]
# nice = []
# boos = []
# for n in range(0, len(b), 2):
#     boos.append(b[n:n + 2])
# for k in range(0,len(b),3):
#     nice.append(b[k:k+2])
# print(boos)
# print(nice)
#
# print(k)