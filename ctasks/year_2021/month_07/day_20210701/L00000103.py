'''
103.Binary Tree Zigzag Level Order Traversal
103.二叉树的锯齿形层序遍历

https://leetcode-cn.com/problems/
binary-tree-zigzag-level-order-traversal

给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

返回锯齿形层序遍历如下：

[
  [3],
  [20,9],
  [15,7]
]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
'''

from typing import List
from clecode.structures import TreeNode, HandleTreeTwo
from clecode import decorator_default


@decorator_default("")
def ctest(method_name, class_name):
    return f"""
    
    >>> root = HandleTreeTwo([3,9,20,"#","#",15,7]).data_root
    >>> {class_name}().{method_name}(root)
    [[3], [20, 9], [15, 7]]

    """


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        stack = [[root]]
        res = []
        floor = 1
        while stack:
            floor += 1
            nodes = stack.pop()
            m_stacks = []
            m_res = []
            for node in nodes:
                m_res.append(node.val)
                if node.left: m_stacks.append(node.left)
                if node.right: m_stacks.append(node.right)
            if m_stacks:
                stack.append(m_stacks)
            if m_res:
                if floor % 2 == 0:
                    res.append(m_res)
                else:
                    res.append(m_res[::-1])
        return res


# 作者：zoc-k
# 链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/solution/python3-by-zoc-k-w7b2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

Solution.zigzagLevelOrder.__doc__ = ctest("zigzagLevelOrder", "Solution")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
