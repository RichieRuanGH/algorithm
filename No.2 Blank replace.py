'''
来源: 牛客 替换空格
要求： 将字符串中的空格 替换成%20

数据结构
"We Are Happy" --> "We%20Are%20Happy"


'''


#  测试部分
str_default = 'We Are Happy'

# str_input = input('Please enter a string with blank\n')

str_new = str_default.replace(' ', '%20')
print(str_new[1])

"""
        S.replace(old, new[, count]) -> str

        Return a copy of S with all occurrences of substring
        old replaced by new.  If the optional argument count is
        given, only the first count(第一次出现的count数) occurrences are replaced.
        0= no replace
"""


# 调包解法
def str_replace(str_input = input('Please enter a string with blank\n')):
    """

    :param str_input:输入字符串，如果为空，通过终端输入
    :return:  返回字符串变量

    方式：使用字符串自带方法
    """
    print('第一遍'+str_input.replace(' ', '%20'))
    return str_input.replace(' ', '%20')


str_new_f = str_replace()
print('第二遍'+str_new_f)


# 自定义解法
def str_replace_source(str_input: str, count: int = -1):
    """

    :param str_input: 输入字符串，如果为空，通过终端输入
    :param count: 指定需要从首次出现要替换的个数， 如果忽略则全部替换
    :return:

    方式：使用列表append方式+ 转变为字符串的方法
    """
    if str_input is None:
        str_input = input('Please enter a string with blank\n')
    str_temp = []
    for i in str_input:
        if i == ' ' and count != 0:  # count 作为函数递减， 当为0时不再执行，否则都执行
            str_temp.append('%20')
            count -= 1
        else:
            str_temp.append(i)
    print(''.join(str_temp))
    return str_temp


str_replace_source(None)
