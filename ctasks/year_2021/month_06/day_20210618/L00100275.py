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
    
    >>> nums = [2, 3, 1, 0, 2, 5, 3]
    >>> res = {class_name}().{method_name}(nums)
    >>> res in [2, 3] 
    True
    """


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        dic = set()
        for num in nums:
            if num in dic: return num
            dic.add(num)
        return -1


# 作者：jyd
# 链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/solution/mian-shi-ti-03-shu-zu-zhong-zhong-fu-de-shu-zi-yua/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
Solution.findRepeatNumber.__doc__ = ctest("findRepeatNumber")





if __name__ == "__main__":
    import doctest

    doctest.testmod()
