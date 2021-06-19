'''
88.Merge Sorted Array
88.合并两个有序数组

https://leetcode-cn.com/problems/
merge-sorted-array

给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。
 
示例 1：

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]

示例 2：

输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]

 
提示：

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[i] <= 109


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
'''

from typing import List
from clecode import decorator_default


@decorator_default("")
def ctest(method_name, class_name):
    return f"""
    
    >>> nums1 = [1,2,3,0,0,0]
    >>> m = 3
    >>> nums2 = [2,5,6]
    >>> n = 3
    >>> _ = {class_name}().{method_name}(nums1, m, nums2, n)
    >>> nums1
    [1, 2, 2, 3, 5, 6]
    
    """


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        def _merge(s1, s2):
            while s1 and s2:
                yield (s1 if s1[0] < s2[0] else s2).pop(0)
            yield from s1
            yield from s2

        # res = list(_merge(nums1[:m], nums2[:n]))
        # for i, j in enumerate(res):
        #     nums1[i] = j
        nums1[:] = list(_merge(nums1[:m], nums2[:n]))


Solution.merge.__doc__ = ctest("merge", "Solution")


class SolutionV1:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if n == 0:
            return nums1
        if m == 0:
            return nums2

        i = 0
        j = m


if __name__ == "__main__":
    import doctest

    doctest.testmod()
