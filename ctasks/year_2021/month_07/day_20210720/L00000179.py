'''
179.Largest Number
179.最大数

https://leetcode-cn.com/problems/
largest-number

给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
 
示例 1：

输入：nums = [10,2]
输出："210"
示例 2：

输入：nums = [3,30,34,5,9]
输出："9534330"

示例 3：

输入：nums = [1]
输出："1"

示例 4：

输入：nums = [10]
输出："10"

 
提示：

1 <= nums.length <= 100
0 <= nums[i] <= 109


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
'''
from functools import cmp_to_key
from typing import List
from clecode import decorator_default


@decorator_default("")
def ctest(method_name, class_name):
    return f"""
    
    >>> 
    >>> {class_name}().{method_name}([10,2])
    '210'
    >>> {class_name}().{method_name}([3,30,34,5,9])
    '9534330'
    >>> {class_name}().{method_name}([1])
    '1'
    >>> {class_name}().{method_name}([10])
    '10'

    """


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 第一步：定义比较函数，把最大的放左边
        # 第二步：排序
        # 第三步：返回结果
        def compare(x, y): return int(y + x) - int(x + y)

        nums = sorted(map(str, nums), key=cmp_to_key(compare))
        return "0" if nums[0] == "0" else "".join(nums)


Solution.largestNumber.__doc__ = ctest("largestNumber", "Solution")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
