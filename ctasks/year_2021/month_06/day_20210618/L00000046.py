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
from clecode import compare


@decorator_default("")
def ctest(method_name, class_name):
    return f"""
    
    >>> nums = [1,2,3]
    >>> res = {class_name}().{method_name}(nums)
    >>> res_true = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    >>> compare.equal_element_in_list(res_true, res)
    True

    >>> nums = [0, 1]
    >>> res = {class_name}().{method_name}(nums)
    >>> res_true = [[0,1],[1,0]]
    >>> compare.equal_element_in_list(res_true, res)
    True

    >>> nums = [1]
    >>> res = {class_name}().{method_name}(nums)
    >>> res_true = [[1]]
    >>> compare.equal_element_in_list(res_true, res)
    True


    """


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/permutations/solution/quan-pai-lie-by-leetcode-solution-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


Solution.permute.__doc__ = ctest("permute")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
