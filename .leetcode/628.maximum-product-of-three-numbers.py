# @lc app=leetcode id=628 lang=python3
#
# [628] Maximum Product of Three Numbers
#
# https://leetcode.com/problems/maximum-product-of-three-numbers/description/
#
# algorithms
# Easy (46.68%)
# Likes:    2082
# Dislikes: 485
# Total Accepted:    175.8K
# Total Submissions: 376.7K
# Testcase Example:  '[1,2,3]'
#
# Given an integer array nums, find three numbers whose product is maximum and
# return the maximum product.
#
#
# Example 1:
# Input: nums = [1,2,3]
# Output: 6
# Example 2:
# Input: nums = [1,2,3,4]
# Output: 24
# Example 3:
# Input: nums = [-1,-2,-3]
# Output: -6
#
#
# Constraints:
#
#
# 3 <= nums.length <= 10^4
# -1000 <= nums[i] <= 1000
#
#
#

# @lc tags=array;math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 得到最大乘积。
# 根据正负的个数来判断。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        pmax = [-1000, -1000, -1000]
        pmin = [-1000, -1000, -1000]
        nmax = [-1000, -1000, -1000]
        nmin = [-1000, -1000, -1000]
        z = False
        for n in nums:
            if n == 0:
                z = True
            elif n > 0:
                heappushpop(pmax, n)
                heappushpop(pmin, -n)
            else:
                heappushpop(nmax, n)
                heappushpop(nmin, -n)
        pn = 3 - pmax.count(-1000)
        nn = 3 - nmax.count(-1000)

        def p(n1, n2, n3):
            return n1 * n2 * n3

        res = p(nums[0], nums[1], nums[2])
        if pn == 3:
            res = max(res, p(*pmax))
        if nn == 3:
            res = max(res, p(*nmax))
        if pn >= 1 and nn >= 2:
            res = max(res, p(max(pmax), nmin[1], nmin[2]))
        if z:
            res = max(res, 0)
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().maximumProduct([1, 2, 3])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,3,4]')
    print('Exception :')
    print('24')
    print('Output :')
    print(str(Solution().maximumProduct([1, 2, 3, 4])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [-1,-2,-3]')
    print('Exception :')
    print('-6')
    print('Output :')
    print(str(Solution().maximumProduct([-1, -2, -3])))
    print()
    print(str(Solution().maximumProduct([-1, -2, -3, -4])))
    pass
# @lc main=end