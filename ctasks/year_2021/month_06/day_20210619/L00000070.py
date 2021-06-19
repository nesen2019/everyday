'''
70.Climbing Stairs
70.爬楼梯

https://leetcode-cn.com/problems/
climbing-stairs

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶


class Solution:
    def climbStairs(self, n: int) -> int:
'''

from clecode import decorator_default


@decorator_default("")
def ctest(method_name, class_name):
    return f"""
    >>> {class_name}().{method_name}(2)
    2

    >>> {class_name}().{method_name}(3)
    3

    >>> {class_name}().{method_name}(4)
    5


    """


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        a, b = 1, 0
        for _ in range(n):
            a, b = a + b, a
        return a


Solution.climbStairs.__doc__ = ctest("climbStairs")


class SolutionV1:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


SolutionV1.climbStairs.__doc__ = ctest("climbStairs", "SolutionV1")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
