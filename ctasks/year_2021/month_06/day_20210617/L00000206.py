'''
206.Reverse Linked List
206.反转链表

https://leetcode-cn.com/problems/
reverse-linked-list

给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。


 
示例 1：


输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]

示例 2：


输入：head = [1,2]
输出：[2,1]

示例 3：

输入：head = []
输出：[]

 
提示：

链表中节点的数目范围是 [0, 5000]
-5000 <= Node.val <= 5000

 
进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
'''

from typing import List
from clecode.structures import ListNode, HandleLink
from clecode import decorator_default


@decorator_default("")
def ctest(method_name, class_name):
    return f"""
    
    >>> head = HandleLink([1,2,3,4,5]).data_root
    >>> res = {class_name}().{method_name}(head)
    >>> HandleLink(res).data_list
    [5, 4, 3, 2, 1]

    >>> head = HandleLink([1,2]).data_root
    >>> res = {class_name}().{method_name}(head)
    >>> HandleLink(res).data_list
    [2, 1]

    >>> head = HandleLink([]).data_root
    >>> res = {class_name}().{method_name}(head)
    >>> HandleLink(res).data_list
    []

    """


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre


class SolutionV1:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead


Solution.reverseList.__doc__ = ctest("reverseList", "Solution")
SolutionV1.reverseList.__doc__ = ctest("reverseList", "SolutionV1")

#
# 作者：edelweisskoko
# 链接：https://leetcode-cn.com/problems/reverse-linked-list/solution/shi-pin-tu-jie-206-fan-zhuan-lian-biao-d-zvli/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


if __name__ == "__main__":
    import doctest

    doctest.testmod()
