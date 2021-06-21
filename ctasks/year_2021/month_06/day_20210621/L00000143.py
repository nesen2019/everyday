'''
143.Reorder List
143.重排链表

https://leetcode-cn.com/problems/
reorder-list

给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
示例 1:
给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:
给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
'''
"""
1 链表线性化及重建  
2 
"""

from typing import List
from clecode.structures import ListNode, HandleLink
from clecode import decorator_default


@decorator_default("")
def ctest(method_name, class_name):
    return f"""
    
    >>> head = HandleLink([1, 2, 3, 4]).data_root
    >>> {class_name}().{method_name}(head)
    >>> HandleLink(head).data_list
    [1, 4, 2, 3]

    >>> head = HandleLink([1, 2, 3, 4, 5]).data_root
    >>> {class_name}().{method_name}(head)
    >>> HandleLink(head).data_list
    [1, 5, 2, 4, 3]


    """


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        lst = list()
        while head:
            lst.append(head)
            head = head.next
        head = lst.pop(0)
        node = head
        while lst:
            node.next = lst.pop()
            node = node.next
            if lst:
                node.next = lst.pop(0)
                node = node.next

        node.next = None


Solution.reorderList.__doc__ = ctest("reorderList")


class SolutionV1:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return

        mid = self.middle_node(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reversed_node(l2)
        self.merge_two_list(l1, l2)

        pass

    def middle_node(self, node):
        slow = fast = node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reversed_node(self, node):
        cur = None
        while node:
            tmp = node.next
            node.next = cur
            cur = node
            node = tmp
        return cur

    def merge_two_list(self, l1, l2):
        while l1 and l2:
            l1_next = l1.next
            l2_next = l2.next

            l1.next = l2
            l1.next.next = l1_next

            l2 = l2_next
            l1 = l1_next


SolutionV1.reorderList.__doc__ = ctest("reorderList", "SolutionV1")

if __name__ == '__main__ss':
    # test merge_two_list
    c = SolutionV1()
    head = HandleLink([1, 2, 3]).data_root
    l1 = head
    l2 = HandleLink([4, 5]).data_root
    d = c.merge_two_list(l1, l2)
    print(HandleLink(head).data_list)

if __name__ == '__main__as':
    # test reversed_node
    c = SolutionV1()
    node = HandleLink([1, 2, 3]).data_root
    d = c.reversed_node(node)
    print(HandleLink(d).data_list)

if __name__ == '__main__das':
    # test middle_node
    c = SolutionV1()
    node = HandleLink([1, 2, 3, 4]).data_root
    d = c.middle_node(node)
    print(HandleLink(d).data_list)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
