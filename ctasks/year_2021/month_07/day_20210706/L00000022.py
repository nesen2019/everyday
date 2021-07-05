'''
22.Generate Parentheses
22.括号生成

https://leetcode-cn.com/problems/
generate-parentheses

数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
 
示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

示例 2：

输入：n = 1
输出：["()"]

 
提示：

1 <= n <= 8


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
'''

from typing import List
from clecode import decorator_default
from clecode.core.compare import equal_element_in_list


@decorator_default("")
def ctest(method_name, class_name):
    return f"""
    
    >>> # todo: 可能顺序不对出现错误
    >>> res = {class_name}().{method_name}(3)
    >>> res_true = ['((()))', '(()())', '(())()', '()(())', '()()()']
    >>> decorator_default.equal_element_in_list(res_true, res)
    True
    
    >>> {class_name}().{method_name}(1)
    ['()']
    """


decorator_default.equal_element_in_list = equal_element_in_list


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()

        backtrack([], 0, 0)
        return ans


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/generate-parentheses/solution/gua-hao-sheng-cheng-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

Solution.generateParenthesis.__doc__ = ctest("generateParenthesis", Solution)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
