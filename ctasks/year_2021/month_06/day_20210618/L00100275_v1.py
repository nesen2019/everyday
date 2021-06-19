'''
剑指 Offer 03.数组中重复的数字 LCOF
剑指 Offer 03.数组中重复的数字

https://leetcode-cn.com/problems/
shu-zu-zhong-zhong-fu-de-shu-zi-lcof

找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
示例 1：
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 

 
限制：
2 <= n <= 100000

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
'''

from typing import List
from clecode import decorator_default


@decorator_default("")
def ctest(method_name, class_name):
    return f"""

    """


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]


Solution.findRepeatNumber.__doc__ = ctest("findRepeatNumber")


class SolutionV1:
    def findRepeatNumber(self, nums: List[int]) -> int:
        i = 0
        len_nums = len(nums)
        while i < len_nums:
            if i == nums[i]:
                i += 1
                continue
            if nums[i] == nums[nums[i]]:
                return nums[i]
            else:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]


SolutionV1.findRepeatNumber.__doc__ = ctest("findRepeatNumber", "SolutionV1")

if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # print(SolutionV1().findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))
    # print(ctest("findRepeatNumber"))
