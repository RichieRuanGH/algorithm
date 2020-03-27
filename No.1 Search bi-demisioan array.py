'''
来源 leetcode 搜索二维矩阵
编写一个高效算法搜索有序m*n的矩阵， 并找到一个目标值是否存在其中,是返回true 没有则返回false

矩阵结构
[
    [1,4,7,11,15],
    [2,5,8,12,19],
    [3,6,9,16,22],
    [10,13,14,17,24],
    [18,21,23,26,30],
]
'''

bi_array = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19, 20, 55],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]
for i_outer in range(0, len(bi_array)):
    print(bi_array[i_outer])


def search_tar(bi: list, target: int):
    """

    :param bi: 传入的二维数组
    :param target:  目标值
    :return:True or False

    思路： 每行最后一个数是该行最大，但该列最小， 以此为判断点，
        如果比该数小，则在本行递减查找，
        如果比该数大，则在下一行重新寻找
        直到最终返回结果
    """
    if len(bi) == 0:
        return False
    i = 0
    # j = len(bi[0])-1
    while i < len(bi):
        j = len(bi[i]) - 1   # 可以保证数组长度不一致时，取当前数组的长度
        while j >= 0:
            if bi[i][j] > target:
                j = j-1
            elif bi[i][j] < target:
                i = i+1
                break
            else:
                return True
    return False


print(search_tar(bi_array, 20))


search_tar()