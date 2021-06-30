'''
739.Daily Temperatures
739.每日温度

https://leetcode-cn.com/problems/
daily-temperatures

请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。
例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
'''

from typing import List
from clecode import decorator_default


@decorator_default("")
def ctest(method_name, class_name):
    return f"""
    
    >>> temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    >>> {class_name}().{method_name}(temperatures)
    [1, 1, 4, 2, 1, 1, 0, 0]

    """


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        ans = [0] * length
        stack = []
        for i in range(length):
            temperature = temperatures[i]
            while stack and temperature > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/daily-temperatures/solution/mei-ri-wen-du-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

Solution.dailyTemperatures.__doc__ = ctest("dailyTemperatures", "Solution")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
