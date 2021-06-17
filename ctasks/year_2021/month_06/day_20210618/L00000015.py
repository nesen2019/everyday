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


def equal_L00000015(res_true, res):
    if len(res_true) != len(res):
        return False
    for i in range(len(res_true)):
        res_true[i].sort()
        res[i].sort()
    for i in res:
        if i not in res_true:
            return False
    return True


@decorator_default("")
def ctest(method_name, class_name):
    return f"""

    >>> 
    >>> res = {class_name}().{method_name}([-1,0,1,2,-1,-4])
    >>> res_true = [[-1,-1,2],[-1,0,1]]
    >>> # ctest.__code__
    >>> decorator_default.equal_L00000015(res_true, res)
    True

    """


decorator_default.equal_L00000015 = equal_L00000015


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()

        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/3sum/solution/san-shu-zhi-he-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

Solution.threeSum.__doc__ = ctest("threeSum")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
