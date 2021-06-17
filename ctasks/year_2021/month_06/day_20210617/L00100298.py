'''
剑指 Offer 24.反转链表 LCOF
剑指 Offer 24.反转链表

https://leetcode-cn.com/problems/
fan-zhuan-lian-biao-lcof

定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
 
示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
 
限制：
0 <= 节点个数 <= 5000
 
注意：本题与主站 206 题相同：https://leetcode-cn.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre


Solution.reverseList.__doc__ = ctest("reverseList")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
