'''
20.Valid Parentheses
20.有效的括号

https://leetcode-cn.com/problems/
valid-parentheses

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

 
示例 1：

输入：s = "()"
输出：true

示例 2：

输入：s = "()[]{}"
输出：true

示例 3：

输入：s = "(]"
输出：false

示例 4：

输入：s = "([)]"
输出：false

示例 5：

输入：s = "{[]}"
输出：true
 
提示：

1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成


class Solution:
    def isValid(self, s: str) -> bool:
'''

from clecode import decorator_default


@decorator_default("")
def ctest(method_name, class_name):  
    return f"""
    
    >>> 
    >>> res = {class_name}().{method_name}()
    """


class Solution:
    def isValid(self, s: str) -> bool:
        pass


if __name__ == "__main__":  
    import doctest  
    
    doctest.testmod()
