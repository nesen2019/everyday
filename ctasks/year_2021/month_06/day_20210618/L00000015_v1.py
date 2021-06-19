'''
15.3Sum
15.三数之和

https://leetcode-cn.com/problems/
3sum

给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。
 
示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

示例 2：

输入：nums = []
输出：[]

示例 3：

输入：nums = [0]
输出：[]

 
提示：

0 <= nums.length <= 3000
-105 <= nums[i] <= 105


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
'''

from typing import List
from clecode import decorator_default


@decorator_default("")
def ctest(method_name, class_name):
    return f"""
    
    >>> 
    >>> res = {class_name}().{method_name}()
    """


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        len_nums = len(nums)
        res = list()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            target = -a
            left = i + 1
            right = len_nums - 1
            while left < right:
                sum_lr = nums[left] + nums[right]
                if sum_lr > target:
                    right -= 1

                elif sum_lr < target:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left > 0 and left + 1 < len_nums and nums[left] == nums[left - 1]:
                        left += 1
                    while right > 0 and right + 1 < len_nums and nums[right] == nums[right + 1]:
                        right -= 1

        return res


Solution.threeSum.__doc__ = ctest("threeSum")

if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # # print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
    # print(Solution().threeSum([-4, -1, -1, 0, 1, 2]))
    # print(Solution().threeSum([0, 0, 0, 0]))
    # print(Solution().threeSum([-2, 0, 0, 2, 2]))
