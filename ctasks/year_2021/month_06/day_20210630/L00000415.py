'''
415.Add Strings
415.字符串相加

https://leetcode-cn.com/problems/
add-strings

给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
 
提示：

num1 和num2 的长度都小于 5100
num1 和num2 都只包含数字 0-9
num1 和num2 都不包含任何前导零
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
'''

from clecode import decorator_default


@decorator_default("")
def ctest(method_name, class_name):
    return f"""
    
    >>> 
    >>> {class_name}().{method_name}("456", "123")
    '579'

    >>> {class_name}().{method_name}("10", "123")
    '133'

    >>> {class_name}().{method_name}("10", "123")
    '133'
    """


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        return "1" + res if carry else res


# 作者：jyd
# 链接：https://leetcode-cn.com/problems/add-strings/solution/add-strings-shuang-zhi-zhen-fa-by-jyd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

Solution.addStrings.__doc__ = ctest("addStrings")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
