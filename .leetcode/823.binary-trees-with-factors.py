# @lc app=leetcode id=823 lang=python3
#
# [823] Binary Trees With Factors
#

# @lc tags=math

# @lc imports=start
from time import time
from imports import *

# @lc imports=end

# @lc idea=start
#
# 二叉树个数，每个非叶子结点的值等于子节点值的乘积。
# 排序
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        times = {}
        for n in arr:
            times[n] = 1
        for i in range(len(arr)):
            ai = arr[i]
            ti = times[ai]
            k = ai * ai
            if k in times:
                times[k] = (times[k] + ti * ti) % 1000000007
            for j in range(i):
                aj = arr[j]
                k = ai * aj
                if k in times:
                    times[k] = (times[k] + ti * times[aj] * 2) % 1000000007
        return sum(times.values()) % 1000000007
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('arr = [2,4]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().numFactoredBinaryTrees([2, 4])))
    print()

    print('Example 2:')
    print('Input : ')
    print('arr = [2,4,5,10]')
    print('Exception :')
    print('7')
    print('Output :')
    print(str(Solution().numFactoredBinaryTrees([2, 4, 5, 10])))
    print()

    pass
# @lc main=end