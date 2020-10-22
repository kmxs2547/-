#输出闰年
list=[year for year in range(1970,2051) if year%4==0 and year%100!= 0]
print(list)

