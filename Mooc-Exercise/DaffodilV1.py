'''
水仙花数问题：
是指一个n位数N（n>=3），它的每个位上的数字的n次幂之和等于这个数N
例如153:    1**3+5**3+3**3=153
'''
import os

def  isFlower(x):
    listName=[]
    temp=x
    while temp>0:
        # 求最后一位数，并添加到列表中
        listName.append(temp%10)
        # 去掉最后一位，因为已添加到列表中
        temp //= 10#地板除法，2.2以后新加的，直接把最后一位数干掉
    # 求出列表的长度，就是几位数
    k=len(listName)
    # 最后使用列表解析式，判断是否相等
    return sum([n ** k  for n in listName]) == x


# 在一定的范围内查找
for m in range(1,999):
    if isFlower(m):
        print(m)
