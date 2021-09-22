# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#
# https://leetcode.com/problems/k-diff-pairs-in-an-array/description/
#
# algorithms
# Medium (36.51%)
# Likes:    1385
# Dislikes: 1648
# Total Accepted:    181.8K
# Total Submissions: 496.2K
# Testcase Example:  '[3,1,4,1,5]\n2'
#
# Given an array of integers nums and an integer k, return the number of unique
# k-diff pairs in the array.
#
# A k-diff pair is an integer pair (nums[i], nums[j]), where the following are
# true:
#
#
# 0 <= i < j < nums.length
# |nums[i] - nums[j]| == k
#
#
# Notice that |val| denotes the absolute value of val.
#
#
# Example 1:
#
#
# Input: nums = [3,1,4,1,5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of
# unique pairs.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,4,5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4)
# and (4, 5).
#
#
# Example 3:
#
#
# Input: nums = [1,3,1,5,4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).
#
#
# Example 4:
#
#
# Input: nums = [1,2,4,4,3,3,0,9,2,3], k = 3
# Output: 2
#
#
# Example 5:
#
#
# Input: nums = [-1,-2,-3], k = 1
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -10^7 <= nums[i] <= 10^7
# 0 <= k <= 10^7
#
#
#

# @lc tags=array;two-pointers

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 数组中元素差为k的对数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0
        if k == 0:
            s = {}
            for n in nums:
                if n in s:
                    if s[n] == True:
                        res += 1
                        s[n] = False
                else:
                    s[n] = True
            return res
        else:
            s = set()
            for n in nums:
                if n in s:
                    continue
                l = n - k
                res += 1 if l in s else 0
                r = n + k
                res += 1 if r in s else 0
                s.add(n)
            return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().findPairs([1, 1, 1, 1, 1], 0)))
    print('Example 1:')
    print('Input : ')
    print('nums = [3,1,4,1,5], k = 2')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().findPairs([3, 1, 4, 1, 5], 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,3,4,5], k = 1')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().findPairs([1, 2, 3, 4, 5], 1)))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1,3,1,5,4], k = 0')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().findPairs([1, 3, 1, 5, 4], 0)))
    print()

    print('Example 4:')
    print('Input : ')
    print('nums = [1,2,4,4,3,3,0,9,2,3], k = 3')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().findPairs([1, 2, 4, 4, 3, 3, 0, 9, 2, 3], 3)))
    print()

    print('Example 5:')
    print('Input : ')
    print('nums = [-1,-2,-3], k = 1')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().findPairs([-1, -2, -3], 1)))
    print()

    pass
# @lc main=end