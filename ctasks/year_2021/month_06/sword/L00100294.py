'''
剑指 Offer 22.链表中倒数第k个节点 LCOF
剑指 Offer 22.链表中倒数第k个节点

https://leetcode-cn.com/problems/
lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof

输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。
 
示例：

给定一个链表: 1->2->3->4->5, 和 k = 2.

返回链表 4->5.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
'''

from typing import List
from clecode.structures import ListNode, HandleLink
from clecode import decorator_default


@decorator_default("")
def ctest(method_name, class_name):
    return f"""
    
    >>> head = HandleLink([1,2,3,4,5]).data_root
    >>> res = {class_name}().{method_name}(head, 2)
    >>> HandleLink(res).data_list
    [4, 5]
    """


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        former, latter = head, head
        for _ in range(k):
            former = former.next
        while former:
            former, latter = former.next, latter.next
        return latter


# 作者：jyd
# 链接：https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/solution/mian-shi-ti-22-lian-biao-zhong-dao-shu-di-kge-j-11/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

Solution.getKthFromEnd.__doc__ = ctest("getKthFromEnd", "Solution")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
