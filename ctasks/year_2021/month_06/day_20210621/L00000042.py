'''
42.Trapping Rain Water
42.接雨水

https://leetcode-cn.com/problems/
trapping-rain-water

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
 
示例 1：


输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 

示例 2：

输入：height = [4,2,0,3,2,5]
输出：9

 
提示：

n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105


class Solution:
    def trap(self, height: List[int]) -> int:
'''

from typing import List
from clecode import decorator_default


@decorator_default("")
def ctest(method_name, class_name):
    return f"""
    
    >>> 
    >>> {class_name}().{method_name}([0,1,0,2,1,0,1,3,2,1,2,1])
    6

    >>> {class_name}().{method_name}([4,2,0,3,2,5])
    9

    """


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        leftMax = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax = [0] * (n - 1) + [height[n - 1]]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
        return ans


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/trapping-rain-water/solution/jie-yu-shui-by-leetcode-solution-tuvc/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

Solution.trap.__doc__ = ctest("trap")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
