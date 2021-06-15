'''
5.Longest Palindromic Substring
5.最长回文子串

https://leetcode-cn.com/problems/
longest-palindromic-substring

给你一个字符串 s，找到 s 中最长的回文子串。
 
示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：

输入：s = "cbbd"
输出："bb"

示例 3：

输入：s = "a"
输出："a"

示例 4：

输入：s = "ac"
输出："a"

 
提示：

1 <= s.length <= 1000
s 仅由数字和英文字母（大写和/或小写）组成


class Solution:
    def longestPalindrome(self, s: str) -> str:
'''

from clecode import decorator_default


@decorator_default("")
def ctest(method_name, class_name):  
    return f"""
    
    >>> 
    >>> res = {class_name}().{method_name}()
    """


class Solution:
    def longestPalindrome(self, s: str) -> str:
        pass


if __name__ == "__main__":  
    import doctest  
    
    doctest.testmod()
