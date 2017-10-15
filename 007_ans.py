'''007：打印9*9乘法表
输出9*9口诀
'''

# -*- coding: utf-8 -*-
# python3.6.2
# time: 2017.10.16

for i in range(1,10):
    for j in range(1,10):
        print(i,'*',j,'=',i*j)
    print('')


#遗留的问题：如果想得到三角形排布的乘法表，如何修改代码？
