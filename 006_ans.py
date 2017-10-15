'''006:数字排列组合成三位数
有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
'''

# -*- coding: utf-8 -*-
# python3.6.2
# time: 2017.10.15

cnt = 0     #记录一共有多少个这样的三位数
print("满足条件的三位数有：")
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i !=j and i != k and j != k:
                print(i*100+j*10+k)
                cnt += 1
print("一共有%d个这样的数"%cnt)
