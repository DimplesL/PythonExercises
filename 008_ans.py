'''008：统计字母、空格、数字、字符

输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
'''

# -*- coding: utf-8 -*-
# python3.6.2
# time: 2017.10.26
# there is no ++ operator in Python

import string
def main():
    s = raw_input('input a string:')
    letter = 0
    space = 0
    digit = 0
    other = 0
    for c in s:
        if c.isalpha():
            letter+=1
        elif c.isspace():
            space+=1
        elif c.isdigit():
            digit+=1
        else:
            other+=1
    print 'There are %d letters,%d spaces,%d digits and %d other characters in your string.'%(letter,space,digit,other)

if __name__ == '__main__':
    main()
