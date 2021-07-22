'''
215.Kth Largest Element in an Array
215.数组中的第K个最大元素

https://leetcode-cn.com/problems/
kth-largest-element-in-an-array

在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明: 
你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
'''
import heapq
from typing import List
from clecode import decorator_default


@decorator_default("")
def ctest(method_name, class_name):
    return f"""
    
    >>> 
    >>> {class_name}().{method_name}([3,2,1,5,6,4], 2)
    5
    >>> {class_name}().{method_name}([3,2,3,1,2,4,5,5,6], 4)
    4

    """


class Solution:

    # 使用容量为 k 的小顶堆
    # 元素个数小于 k 的时候，放进去就是了
    # 元素个数大于 k 的时候，小于等于堆顶元素，就扔掉，大于堆顶元素，就替换

    def findKthLargest(self, nums: List[int], k: int) -> int:
        size = len(nums)
        if k > size:
            raise Exception('程序出错')

        L = []
        for index in range(k):
            # heapq 默认就是小顶堆
            heapq.heappush(L, nums[index])

        for index in range(k, size):
            top = L[0]
            if nums[index] > top:
                # 看一看堆顶的元素，只要比堆顶元素大，就替换堆顶元素
                heapq.heapreplace(L, nums[index])
        # 最后堆顶中的元素就是堆中最小的，整个数组中的第 k 大元素
        return L[0]


# 作者：liweiwei1419
# 链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/partitionfen-er-zhi-zhi-you-xian-dui-lie-java-dai-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

Solution.findKthLargest.__doc__ = ctest("findKthLargest", "Solution")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
