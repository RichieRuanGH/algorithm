"""
来源：牛客
要求：输入一个链表，从尾到头输出链表

数据结构：
"""


import ctypes


list_1 = [1, 2, 3, 4, 5, 6]
print()
# linked_l = {}
# for i in list_1:
#     linked_l[id(i)] = i
res = []   # 定义一个全局列表，并在之后使用，最终输出
def print_list(ll: list, i_count=0):
    if len(ll) == 0 or i_count == len(ll): return  # 设置两个递归断点用于返回
    i_count += 1
    print_list(ll, i_count)
    res.append(ll[i_count-1])
    print(ll[i_count-1])

    return res


rec = print_list(list_1)
print(rec)


# 定义单向链表Node类

class Node:  # 直接指向元素， 而不是元素地址
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, new_data):
        self.data = new_data

    def setNext(self, new_next):
        self.next = Node(new_next)

#
# linked1 = Node('first')
# print(linked1.getData())
# linked1.setData('first_new')
# print(linked1.getData())
# linked1.setNext('second')
# linked1 = linked1.getNext()
# print(linked1.getData())


# 定义双向链表Node类  继承

class Node_DWAY(Node):  # 直接指向元素， 而不是元素地址
    def __init__(self, initdata):
        self.previous = None
        super(Node_DWAY, self).__init__(initdata)

    def getPrev(self):
        return self.previous

    def setNext(self, new_next):
        self.next = Node_DWAY(new_next)
        self.next.previous = self


linked2 = Node_DWAY('first')
print(linked2.getData())
linked2.setData('first_new')
print(linked2.getData())
linked2.setNext('second')
linked2 = linked2.getNext()
print(linked2.getData())
linked2 = linked2.getPrev()
print(linked2.getData())

print()

def print_llist(ll: Node):
    if ll is None: return  # 当最后传入的节点为空才返回， 而不是 ll.next 为空


    print_llist(ll.next)
    print(ll.getData())

    return


print_llist(linked2)

#
# class Node:  # 指向元素地址  ，不可用
#     def __init__(self, initdata):
#         self.data = initdata
#         self.next = None
#
#     def getData(self):
#         return self.data
#
#     def getNext(self):
#         return Node(self.next)
#
#     def getId(self):
#         return id(self)
#
#     def setData(self, new_data):
#         self.data = new_data
#
#     def setNext(self, new_next):
#         tmp = Node(new_next)
#         self.next = id(tmp)    # 该方式不可行，因为Python原生没有从地址到数据的转换方式，如果返回id，则在getNext方法中只能返回
#                                # 一个以id值得新Node
#
#
# linked1 = Node('first')
# print(linked1.getData())
# linked1.setData('first_new')
# print(linked1.getData())
# linked1.setNext('second')
# linked1 = linked1.getNext()
# print(linked1.getData())
#