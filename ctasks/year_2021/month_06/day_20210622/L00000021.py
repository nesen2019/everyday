'''
21.Merge Two Sorted Lists
21.合并两个有序链表

https://leetcode-cn.com/problems/
merge-two-sorted-lists

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
 
示例 1：


输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

示例 2：

输入：l1 = [], l2 = []
输出：[]

示例 3：

输入：l1 = [], l2 = [0]
输出：[0]

 
提示：

两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
'''

"""
- 递归
- 迭代

"""

from typing import List
from clecode.structures import ListNode, HandleLink
from clecode import decorator_default


@decorator_default("")
def ctest(method_name, class_name):
    return f"""
    
    >>> l1 = HandleLink([1,2,4]).data_root
    >>> l2 = HandleLink([1,3,4]).data_root
    >>> res = {class_name}().{method_name}(l1, l2)
    >>> HandleLink(res).data_list
    [1, 1, 2, 3, 4, 4]
    
    >>> l1 = HandleLink([]).data_root
    >>> l2 = HandleLink([]).data_root
    >>> res = {class_name}().{method_name}(l1, l2)
    >>> HandleLink(res).data_list
    []
    
    >>> l1 = HandleLink([]).data_root
    >>> l2 = HandleLink([0]).data_root
    >>> res = {class_name}().{method_name}(l1, l2)
    >>> HandleLink(res).data_list
    [0]
    
    """


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """ 递归 """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/he-bing-liang-ge-you-xu-lian-biao-by-leetcode-solu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

Solution.mergeTwoLists.__doc__ = ctest("mergeTwoLists")


class SolutionV1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """ 迭代 """
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = l1 if l1 is not None else l2

        return prehead.next



SolutionV1.mergeTwoLists.__doc__ = ctest("mergeTwoLists", "SolutionV1")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
