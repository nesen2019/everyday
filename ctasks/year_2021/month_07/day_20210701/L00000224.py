'''
224.Basic Calculator
224.基本计算器

https://leetcode-cn.com/problems/
basic-calculator

给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
 
示例 1：

输入：s = "1 + 1"
输出：2

示例 2：

输入：s = " 2-1 + 2 "
输出：3

示例 3：

输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23

 
提示：

1 <= s.length <= 3 * 105
s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
s 表示一个有效的表达式


class Solution:
    def calculate(self, s: str) -> int:
'''

from clecode import decorator_default


@decorator_default("")
def ctest(method_name, class_name):
    return f"""
    
    >>> 
    >>> {class_name}().{method_name}("1 + 1")
    2

    >>> {class_name}().{method_name}(" 2-1 + 2 ")
    3

    >>> {class_name}().{method_name}("(1+(4+5+2)-3)+(6+8)")
    23

    """


class Solution:
    def calculate(self, s: str) -> int:
        ops = [1]
        sign = 1

        ret = 0
        n = len(s)
        i = 0
        while i < n:
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                sign = ops[-1]
                i += 1
            elif s[i] == '-':
                sign = -ops[-1]
                i += 1
            elif s[i] == '(':
                ops.append(sign)
                i += 1
            elif s[i] == ')':
                ops.pop()
                i += 1
            else:
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + ord(s[i]) - ord('0')
                    i += 1
                ret += num * sign
        return ret


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/basic-calculator/solution/ji-ben-ji-suan-qi-by-leetcode-solution-jvir/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

Solution.calculate.__doc__ = ctest("calculate", Solution.__name__)


class SolutionV1:
    def calculate(self, s: str) -> int:
        stack = list()
        j = 0
        lens = len(s)
        while j < lens:
            i = s[j]
            if i == " ":
                pass
            elif i.isdigit():
                while j + 1 < lens and s[j + 1].isdigit():
                    i += s[j + 1]
                    j += 1
                i = int(i)
                if stack and stack[-1] == "+":
                    stack.pop()
                elif stack and stack[-1] == "-":
                    stack.pop()
                    i *= -1
                stack.append(i)
            elif i == "(":
                stack.append(i)
            elif i == "+" or i == "-":
                if stack and stack[-1] in ["+", "-"]:
                    stack.append("+" if stack.pop() == i else "-")
                else:
                    stack.append(i)
            elif i == ")":
                sum = 0
                while stack:
                    if stack[-1] == "(":
                        stack.pop()
                        if stack and stack[-1] in ["+", "-"]:
                            sum *= (1 if stack.pop() == "+" else -1)
                        break
                    sum += stack.pop()
                stack.append(sum)
            j += 1
        if len(stack) > 1:
            sum = 0
            for i in stack:
                sum += i
            return sum
        return stack[-1]


SolutionV1.calculate.__doc__ = ctest("calculate", SolutionV1.__name__)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
