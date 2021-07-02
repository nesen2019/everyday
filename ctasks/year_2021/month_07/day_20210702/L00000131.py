'''
131.Palindrome Partitioning
131.分割回文串

https://leetcode-cn.com/problems/
palindrome-partitioning

给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
回文串 是正着读和反着读都一样的字符串。
 
示例 1：

输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]

示例 2：

输入：s = "a"
输出：[["a"]]

 
提示：

1 <= s.length <= 16
s 仅由小写英文字母组成


class Solution:
    def partition(self, s: str) -> List[List[str]]:
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
    def partition(self, s: str) -> List[List[str]]:
        pass


if __name__ == "__main__":  
    import doctest  
    
    doctest.testmod()
