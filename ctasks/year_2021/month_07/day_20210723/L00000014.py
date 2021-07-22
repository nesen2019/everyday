'''
14.Longest Common Prefix
14.最长公共前缀

https://leetcode-cn.com/problems/
longest-common-prefix

编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
 
示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"

示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
 
提示：

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
'''

"""
- 横向扫描
- 纵向扫描
- 分治
- 二分
"""

from typing import List
from clecode import decorator_default


@decorator_default("")
def ctest(method_name, class_name):
    return f"""
    
    >>> strs = ["flower","flow","flight"]
    >>> {class_name}().{method_name}(strs)
    'fl'
    >>> strs = ["dog","racecar","car"]
    >>> {class_name}().{method_name}(strs)
    ''
    """


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break

        return prefix

    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/longest-common-prefix/solution/zui-chang-gong-gong-qian-zhui-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

Solution.longestCommonPrefix.__doc__ = ctest("longestCommonPrefix", "Solution")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
