import numpy as np
import os
from typing import List
from itertools import combinations


def equal_element_in_list(lst_true: List, lst_comp: List) -> bool:
    """

    :param lst_true:
    :param lst_comp:
    :return: (bool), True or False

    e.g.
    l1 = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    l2 = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]]
    l1 = [1, 2, 3]
    l2 = [3, 1, 2]

    """
    if len(lst_true) != len(lst_comp):
        return False

    for i, j in combinations(range(len(lst_comp)), 2):
        if lst_comp[i] == lst_comp[j]:
            return False
    for i in lst_comp:
        if i not in lst_true:
            return False

    return True
