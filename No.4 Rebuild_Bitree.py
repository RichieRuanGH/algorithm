"""
来源： unknown
要求： 根据前序，中序 重建一个二叉树，**前序中序不含有重复数据

数据结构：
前序 [1, 2, 4, 7, 3, 5, 6, 8]
中序 [4, 7, 2, 1, 5, 3, 8, 6]

前序 [1, 4, 7]
中序 [4, 1, 7]

    1
  /   \
4      7
ps：
    BFS Board first search
    DFS Deep first search

    所有节点都是遇到叶子节点才返回，如果非叶子节点，则继续下探 (DFS)
    前序 preorder  根--左--右
    中序 inorder   左--根--右
    后续 Postorder 左--右--根

可通过中序 + 任意前后序生成层次列表
    层次 根左右下一层依次读取  (BFS)
"""
import mod

#
# rec = []
# for l in [1, 2, 4, 7, 3, 5, 6, 8]:
#     pass
#
# l1 = [1, 4, 7]
# l2 = [4, 1, 7]
# l2_new = l2[l2.index(l1[0])+1:]
# # l2 = l2[0:l2.index(l1[0])]
# l2_new.extend(l2[0:l2.index(l1[0])+1])
# '''
#     list.append(x)  向列表中添加元素
#     list.extend(list) 向列表中扩展新列表
# '''
#
# l2_new.reverse()
#
# print(l2_new)



# Solution

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        思路： 从前序找每一个树（子树）的根， 再从中序递归找下一颗子树，直到为空
        """

        def helper(in_left=0, in_right=len(inorder)):
            nonlocal pre_idx
            # if there is no elements to construct subtrees
            if in_left == in_right:
                return None

            # pick up pre_idx element as a root
            root_val = preorder[pre_idx]
            root = mod.TreeNode(root_val)      # 每个节点都是为一个根节点只不过没有， 最后一个节点的左右都为空。 红黑树也同理

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[root_val]

            # recursion
            pre_idx += 1
            # build left subtree
            root.left = helper(in_left, index)
            # build right subtree
            root.right = helper(index + 1, in_right)
            return root

        # start from first preorder element
        pre_idx = 0
        # build a hashmap value -> its index
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper()


l1 = [1, 2, 4, 7, 3, 5, 6, 8]
l2 = [4, 7, 2, 1, 5, 3, 8, 6]

enumerate(l2)

s1 = Solution()
new_tree = s1.buildTree(l1, l2)

print(new_tree.val)

def print_tree(tree: mod.TreeNode):
    if tree is None: return
    print(tree.val)
    print_tree(tree.left)
    print_tree(tree.right)


print_tree(new_tree)

