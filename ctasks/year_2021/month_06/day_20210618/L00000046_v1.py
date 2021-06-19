'''
46.Permutations
46.全排列

https://leetcode-cn.com/problems/
permutations

给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
 
示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]

示例 3：

输入：nums = [1]
输出：[[1]]

 
提示：

1 <= nums.length <= 6
-10 <= nums[i] <= 10
nums 中的所有整数 互不相同


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 递归 回溯
        res = list()
        len_nums = len(nums)

        def backtrack(k):
            if k == len_nums:
                res.append(nums[:])
            for i in range(k, len_nums):
                nums[i], nums[k] = nums[k], nums[i]
                backtrack(k + 1)
                nums[i], nums[k] = nums[k], nums[i]

        backtrack(0)
        return res


Solution.permute.__doc__ = ctest("permute")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
