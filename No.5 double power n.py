"""
来源：牛客
要求： 给定一个float数，在不使用power的情况下，算出该浮点数的n次方

数据结构：
    指数为奇数时， 将指数 拆分为 n/2 n/2 + 1
    指数为偶数时， 将指数 拆分为 n/2 n/2

    n/2则用 位运算符 >> 实现

PS  位运算符
    >> 向左移一位，即数据/2 (向下取整)
    例
    8  1000   8>>1 = 0100 = 4
    7  0111   7>>1 = 0011 = 3

    << 向右移同理，但是 数据 *2
"""

# import math

def pow_float(double: float, exponent: int):
    if double == 0: return 0
    if double == 1: return 1

    t: float = PositivePower(double, abs(exponent))

    return t if exponent > 0 else 1/t


def PositivePower(double: float, exponent: int):
    """

    :param double:
    :param exponent:
    :return:

    当指数为7  递归返回指数
    (
            (
                (1*2)  # 这里指 指数相加的结果  1*1 =1^1 * 1^1 =1^1+1 = 1^1*2
                    =2 +1) =3)*2
                                 =6)+ 1 =7

    当指数为8  递归返回指数
    (
            (
                (1*2)
                    =2 ) * 2 =4
                              )* 2 =8
    """
    if exponent == 0: return 1
    if exponent == 1: return double
    t: float = PositivePower(double, exponent >> 1)   # 指数左移 除以2
    t *= t                                          # 上一行中t的返回值平方，逐层递归，当最后n=1时返回double， double*doulbe =doulbe^2
                                                    # 当上一层返回3的平方时， 数据是 doulbe^3 * double^3 = double^6
    if exponent & 0x01 == 1: t *= double            #该层实现指数再加1
    return t


print(pow_float(3.14, -5))
