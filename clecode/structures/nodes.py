__all__ = [
    "ListNode",
    "TreeNode",
]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"val= {self.val}, next_id= {id(self.next)}"


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"val={self.val}, left_id= {id(self.left)}, right_id= {id(self.right)}"
