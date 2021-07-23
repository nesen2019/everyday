'''
剑指 Offer 38.字符串的排列 LCOF
剑指 Offer 38.字符串的排列

https://leetcode-cn.com/problems/
zi-fu-chuan-de-pai-lie-lcof

输入一个字符串，打印出该字符串中字符的所有排列。
 
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
 
示例:
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]

 
限制：
1 <= s 的长度 <= 8

class Solution:
    def permutation(self, s: str) -> List[str]:
'''

from typing import List
from clecode import decorator_default
from clecode.core.compare import equal_element_in_list


@decorator_default("")
def ctest(method_name, class_name):
    return f"""
    
    >>> 
    >>> res = {class_name}().{method_name}("abc")
    >>> res_true = ["abc","acb","bac","bca","cab","cba"]
    >>> equal_element_in_list(res_true, res)
    True
    """


class Solution:
    def permutation(self, s: str) -> List[str]:
        c, res = list(s), []

        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c))  # 添加排列方案
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic:
                    continue  # 重复，因此剪枝
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]  # 交换，将 c[i] 固定在第 x 位
                dfs(x + 1)  # 开启固定第 x + 1 位字符
                c[i], c[x] = c[x], c[i]  # 恢复交换

        dfs(0)
        return res


# 作者：jyd
# 链接：https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/solution/mian-shi-ti-38-zi-fu-chuan-de-pai-lie-hui-su-fa-by/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

Solution.permutation.__doc__ = ctest("permutation", "Solution")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
