from .nodes import ListNode

__all__ = [
    "HandleLink",
]


class HandleLink:
    def __init__(self, data=None, is_data_two=True):
        """

        :param data:
        :param is_data_two:

        >>> data_list = [1,2,3,4]
        >>> root = HandleLink(data_list).data_root

        >>> root = HandleLink([3,2,4,1]).data_root
        >>> data_list = HandleLink(root).data_list

        """
        self.data = data
        self.__root = None
        self.__list = list()
        self.__is_data_two = is_data_two
        self.data_two = list()  # (node.val, node)
        self.init_data(data)

    def init_data(self, data):
        if isinstance(data, ListNode):
            self.__root = data
            self.__list = self.data_list
            pass

        if isinstance(data, (list, tuple)):
            self.__list = data
            self.__root = self.data_root
            pass

    @property
    def data_root(self):
        """
        :param data_list:
        :return:

        >>> h_list = HandleLink([1, 2, 3, 4])
        >>> root = h_list.data_root
        >>> root.val
        1
        >>> root.next.val, root.next.next.val
        (2, 3)
        >>> h_list.data_root_node_n(3, root).val, h_list.data_root_node_n(3, root).next
        (4, None)
        """
        if self.__root:
            return self.__root

        data_list = self.data
        if not data_list:
            return None

        self.__root = ListNode(data_list[0])
        if self.__is_data_two:
            self.data_two.append((self.__root.val, self.__root))
        node = self.__root
        for i in data_list[1:]:
            node.next = ListNode(i)
            node = node.next
            if self.__is_data_two:
                self.data_two.append((node.val, node))
        self.__is_data_two = False
        return self.__root

    def data_root_node_n(self, n, root):
        node = root
        for i in range(n):
            node = node.next
        return node

    @property
    def data_list(self):
        """

        :return:

        >>> h_list = HandleLink([1,2,3,4])
        >>> root = h_list.data_root
        >>> new_h_list = HandleLink(root)
        >>> new_h_list.data_list
        [1, 2, 3, 4]
        >>> HandleLink(HandleLink([3,2,4,1]).data_root).data_list
        [3, 2, 4, 1]

        """
        if self.__list:
            return self.__list

        data_root = self.data
        if data_root is None:
            return []

        node = data_root
        while node:
            self.__list.append(node.val)
            if self.__is_data_two:
                self.data_two.append((node.val, node))
            node = node.next
        return self.__list

    @staticmethod
    def equal_root(root1, root2):
        """
        >>> r1 = HandleLink([1,3,2,4]).data_root
        >>> r2 = HandleLink([1,3,2,4]).data_root
        >>> HandleLink.equal_root(r1, r2)
        True

        >>> r1 = HandleLink([1,4,3]).data_root
        >>> r2 = HandleLink([1,4,3,2]).data_root
        >>> HandleLink.equal_root(r1, r2)
        False
        """
        while root1 and root2:
            if root1.val != root2.val:
                return False
            root1 = root1.next
            root2 = root2.next
        if root1 or root2:
            return False
        return True

    def __repr__(self):
        return str(self.data_list)

if __name__ == '__main__':
    import doctest

    doctest.testmod()
