from .nodes import TreeNode

__all__ = [
    "HandleTreeTwo",
]


class HandleTreeTwo:
    """
    Attribute:
    self.data
    self.placeholder
    self.__list
    self.__root

    Method:
    self.init_data(data)
    self.data_root
    self.data_list # 层序遍历
    self.data_list_inorder
    self.data_list_preorder
    self.data_list_subsequent

    """

    def __init__(self, data, placeholder="#", data_type="sequence"):
        """

        :param data: (list, TreeNode)
        :param placeholder: default: "#",
        :param data_type: default: "sequence", option:["sequence",["inorder",["preorder",["subsequent"
        """
        self.data = data
        self.placeholder = placeholder
        self.__data_type = data_type

        self.__root = None
        self.__lst = []
        self.init_data(data)

    def init_data(self, data):
        if isinstance(data, TreeNode):
            self.__root = data
            self.__lst = self.data_list

        if isinstance(data, (list, tuple)):
            self.__lst = data
            if self.__data_type == "sequence":
                self.__root = self.data_root

    @property
    def data_root(self):
        """

        :return:

        >>> h = HandleTreeTwo(data=[1,2,3,"#", 5,6])
        >>> root = h.data_root
        >>> root.val
        1
        >>> root.left.val, root.right.val
        (2, 3)
        >>> root.left.right.val
        5
        >>> root.right.left.val
        6
        """

        if self.__root:
            return self.__root
        data_list = self.data
        if not data_list:
            return None
        root = TreeNode(data_list[0])
        stack = [root]
        i = 1
        data_list = data_list if len(data_list) % 2 == 1 else data_list + [self.placeholder]
        while True:
            j = 2 ** i - 1
            now_floor = data_list[j:j + 2 ** i]
            if not now_floor:
                break
            for left, right in zip(now_floor[0::2], now_floor[1::2]):
                node = stack.pop(0)
                node.left = TreeNode(left) if left != self.placeholder else None
                node.right = TreeNode(right) if right != self.placeholder else None
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            i += 1
        self.__root = root
        return root

    @property
    def data_list(self):
        """

        :return:

        >>> h_tree = HandleTreeTwo([1, 2, 3, '#', 5, "#", 7, 8, 9])
        >>> root = h_tree.data_root
        >>> new_h_tree = HandleTreeTwo(root)
        >>> new_h_tree.data_list
        [1, 2, 3, '#', 5, '#', 7, 8, 9]
        """
        if self.__lst:
            return self.__lst
        data_root = self.__root
        data_list = list()
        stack = [data_root]
        while stack:
            node = stack.pop(0)
            if node is None:
                data_list.append(self.placeholder)
            else:
                data_list.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        while data_list[-1] == self.placeholder:
            data_list.pop()

        return data_list


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    #
    # h = HandleTreeTwo([1, 2, 3, "#", "#", 5, 6, 7, "#", 8])
    # h = HandleTreeTwo([1, 2, 3, "#", 5, 6, 7, 8, 9])
    # # print(h.data_root)
    # root = h.data_root
    # hh = HandleTreeTwo(root)
    # print(hh.data_list)
