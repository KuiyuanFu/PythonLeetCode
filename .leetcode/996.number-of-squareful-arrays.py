# @lc app=leetcode id=996 lang=python3
#
# [996] Number of Squareful Arrays
#
# https://leetcode.com/problems/number-of-squareful-arrays/description/
#
# algorithms
# Hard (49.15%)
# Likes:    768
# Dislikes: 32
# Total Accepted:    27.8K
# Total Submissions: 56.6K
# Testcase Example:  '[1,17,8]'
#
# An array is squareful if the sum of every pair of adjacent elements is a
# perfect square.
#
# Given an integer array nums, return the number of permutations of nums that
# are squareful.
#
# Two permutations perm1 and perm2 are different if there is some index i such
# that perm1[i] != perm2[i].
#
#
# Example 1:
#
#
# Input: nums = [1,17,8]
# Output: 2
# Explanation: [1,8,17] and [17,8,1] are the valid permutations.
#
#
# Example 2:
#
#
# Input: nums = [2,2,2]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 12
# 0 <= nums[i] <= 10^9
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定数组，求排列的个数，使数组满足完美平方，即相邻两个数的和为一个平方数。
# 直接图。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def numSquarefulPerms(self, nums: List[int]) -> int:

        counter = Counter(nums)
        keys = list(counter.keys())
        values = list(counter.values())

        length = len(keys)

        neighborss = [[] for _ in range(length)]
        for i, j in combinations(range(length), 2):
            ni, nj = keys[i], keys[j]
            s = ni + nj
            f = int(s**0.5)
            if s == f * f:
                neighborss[i].append(j)
                neighborss[j].append(i)
        for i in range(length):
            if values[i] >= 2:
                s = keys[i] * 2
                f = int(s**0.5)
                if s == f * f:
                    neighborss[i].append(i)

        self.res = 0
        t = len(nums) - 1

        def recur(i, d):
            if d == t:
                self.res += 1
                return
            values[i] -= 1
            for n in neighborss[i]:
                if values[n] > 0:
                    recur(n, d + 1)
            values[i] += 1

        for i in range(length):
            recur(i, 0)

        return self.res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums =[1,1,8,1,8]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().numSquarefulPerms([1, 1, 8, 1, 8])))
    print()
    print('Example 1:')
    print('Input : ')
    print('nums = [1,1]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().numSquarefulPerms([1, 1])))
    print()
    print('Example 1:')
    print('Input : ')
    print('nums = [1,17,8]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().numSquarefulPerms([1, 17, 8])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [2,2,2]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().numSquarefulPerms([2, 2, 2])))
    print()

    pass
# @lc main=end