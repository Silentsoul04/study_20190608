# coding=utf-8
# 切片操作（slice）可以从一个字符串中获取子字符串（字符串的一部分）。
# 我们使用一对方括号、起始偏移量start、终止偏移量end 以及可选的步长step 来定义一个分片。
# 格式： [start:end:step]
# [:] 提取从开头（默认位置0）到结尾（默认位置-1）的整个字符串
# [start:] 从start 提取到结尾
# [:end] 从开头提取到end - 1
# [start:end] 从start 提取到end - 1
# [start:end:step] 从start 提取到end - 1，每step 个字符提取一个
# 左侧第一个字符的位置/偏移量为0，右侧最后一个字符的位置/偏移量为-1

s = '2272人付款'
print(s[:-3])  #　2272，表示从开头提取到index为-4的字符（包含-4）
print(s[1:])   # 从index为1提取到结尾
print(s[-3:-1])    #    人付   从倒数第3个元素到倒数第一个（但是不包括倒数第一个）
print(s[-3:])   # 人付款
s = 'python'
print(s[::-3])
####
# 字符串：
s = '0123456789'

index:
[  0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]

# slice：[::]
# [开始:结束(不含):方向&步数(默认为1)]

s = '0123456789'
s[:]      # '0123456789'
s[::2]    # '02468'
s[::3]    # '0369'

s = '0123456789'
s[1::2]     # '13579'
s[2::2]    # '2468'
s[2::4]    # '26'

s = '0123456789'
s[:2:1]      # '01'
s[1:2:1]      # '1'
s[1:2:2]       # '1'
s[1:5:2]       # '13'

# slice：
# [开始:结束(不含):方向&步数]  步长为负数表示从右边开始切片，相当于逆序

s = '0123456789'
s[::-1]    # '9876543210'    逆序一个字符串的方法
s[::-2]    # '97531'
s[::-3]    # '9630'

s = '0123456789'
s[:2:-1]       # '9876543'     从右边开始切片，直到index2为止（不包含index为2的元素）
s[1:2:-1]      # ''
s[2:1:-1]        # '2'
s[2::-1]        # '210'      # 如果步长为负数，从右边往左边开始切，起始为index 2，
s[-1:-2:-1]       # '9'
s[-1:-5:-2]    # '97'

# 版权声明：本文为CSDN博主「Loewi大湿」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_42317507/article/details/93479543
#