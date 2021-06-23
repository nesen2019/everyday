'''
剑指 Offer 51.数组中的逆序对 LCOF
剑指 Offer 51.数组中的逆序对

https://leetcode-cn.com/problems/
shu-zu-zhong-de-ni-xu-dui-lcof

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
 
示例 1:
输入: [7,5,6,4]
输出: 5
 
限制：
0 <= 数组长度 <= 50000

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
'''

"""
- 归并排序
- 离散化树状数组
"""

from typing import List
from clecode import decorator_default


@decorator_default("")
def ctest(method_name, class_name):
    return f"""
    
    >>> 
    >>> {class_name}().{method_name}([7,5,6,4])
    5
    
    >>> {class_name}().{method_name}([7, 5, 6])
    2


    """


class Solution:
    def mergeSort(self, nums, tmp, l, r):
        if l >= r:
            return 0

        mid = (l + r) // 2
        inv_count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid + 1, r)
        i, j, pos = l, mid + 1, l
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
                inv_count += (j - (mid + 1))
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1
        for k in range(i, mid + 1):
            tmp[pos] = nums[k]
            inv_count += (j - (mid + 1))
            pos += 1
        for k in range(j, r + 1):
            tmp[pos] = nums[k]
            pos += 1
        nums[l:r + 1] = tmp[l:r + 1]
        return inv_count

    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        tmp = [0] * n
        return self.mergeSort(nums, tmp, 0, n - 1)


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/shu-zu-zhong-de-ni-xu-dui-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


Solution.reversePairs.__doc__ = ctest("reversePairs", "Solution")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
