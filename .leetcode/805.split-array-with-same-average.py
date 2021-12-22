# @lc app=leetcode id=805 lang=python3
#
# [805] Split Array With Same Average
#
# https://leetcode.com/problems/split-array-with-same-average/description/
#
# algorithms
# Hard (26.53%)
# Likes:    728
# Dislikes: 111
# Total Accepted:    23.7K
# Total Submissions: 89.1K
# Testcase Example:  '[1,2,3,4,5,6,7,8]'
#
# You are given an integer array nums.
#
# You should move each element of nums into one of the two arrays A and B such
# that A and B are non-empty, and average(A) == average(B).
#
# Return true if it is possible to achieve that and false otherwise.
#
# Note that for an array arr, average(arr) is the sum of all the elements of
# arr over the length of arr.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,4,5,6,7,8]
# Output: true
# Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of
# them have an average of 4.5.
#
#
# Example 2:
#
#
# Input: nums = [3,1]
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 30
# 0 <= nums[i] <= 10^4
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将数组分成平均值相同的两组。
# 所有组合。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        target = sum(nums) / len(nums)
        if target in nums:
            return True

        # classify
        ll, bl = [], []
        for n in nums:
            t = n - target
            if t > 0:
                bl.append(t)
            elif t < 0:
                ll.append(t)
        # all combine
        def getCombine(ls: List[int]):
            s = set()
            for l in ls:
                t = set()
                for r in s:
                    t.add(l + r)
                s.add(l)
                for l in t:
                    s.add(l)
            res = set()
            for n in s:
                res.add(round(n, 8))
            return res

        ls, bs = getCombine(ll), getCombine(bl)

        # match

        m = max(bs)

        for l in ls:
            r = -l
            if r in bs and r != m:
                return True
        return False

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':

    print('Example 2:')
    print('Input : ')
    print('nums = [4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 5]')
    print('Exception :')
    print('true')
    print('Output :')
    print(
        str(Solution().splitArraySameAverage(
            [4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 5])))
    print()

    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3,4,5,6,7,8]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().splitArraySameAverage([1, 2, 3, 4, 5, 6, 7, 8])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [3,1]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().splitArraySameAverage([3, 1])))
    print()

    pass
# @lc main=end