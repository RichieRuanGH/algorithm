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


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
