"""
来源： 牛客网
要求：给定一组整数数组，通过函数调整数字的顺序， 使所有奇数在偶数之前， 但不用排序

数据结构 or 样例数据：
[9,8,7,6,5,4,3,2,1]
思路: 冒泡算法的变种，从后向前比较，但不用比大小，只比较奇偶性
"""

ll = [9, 8, 7, 6, 5, 4, 3, 2, 1]
inp = list(int(x) for x in input("PLEASE ENTER NUMBER\n"))
"""
input 输入用法: 默认 input 将输入字符识别文字符串，需用int进行转换
但input默认将字符串按 字符循环， 即 10 转换为 ‘1‘，’0‘ ，如果需要指定分隔方式，可使用.split()
.split() 默认使用' ' 空格切分

"""
print(inp)

# for i_1 in range(8, 2, -1):   # range 倒序需用 -1 步长
#     print(i_1)

def oddAeven(ll: list):
    if len(ll) == 0: return 0
    # print(len(ll))
    for i in range(len(ll)-2, -1, -1):
        # print(i)
        for j in range(i, len(ll)-1):
            # print(j)
            if ll[j] % 2 == 0 and ll[j+1] % 2 == 1:
                swap(ll, j, j+1)

    return ll

def swap(ll: list, p1: int, p2: int):
    ll[p1] = ll[p1] ^ ll[p2]
    ll[p2] = ll[p1] ^ ll[p2]
    ll[p1] = ll[p1] ^ ll[p2]

    return ll


print(oddAeven(inp))

