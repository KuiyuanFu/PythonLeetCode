# @lc app=leetcode id=798 lang=python3
#
# [798] Smallest Rotation with Highest Score
#
# https://leetcode.com/problems/smallest-rotation-with-highest-score/description/
#
# algorithms
# Hard (46.34%)
# Likes:    314
# Dislikes: 20
# Total Accepted:    8K
# Total Submissions: 17.2K
# Testcase Example:  '[2,3,1,4,0]'
#
# You are given an array nums. You can rotate it by a non-negative integer k so
# that the array becomes [nums[k], nums[k + 1], ... nums[nums.length - 1],
# nums[0], nums[1], ..., nums[k-1]]. Afterward, any entries that are less than
# or equal to their index are worth one point.
#
#
# For example, if we have nums = [2,4,1,3,0], and we rotate by k = 2, it
# becomes [1,3,0,2,4]. This is worth 3 points because 1 > 0 [no points], 3 > 1
# [no points], 0 <= 2 [one point], 2 <= 3 [one point], 4 <= 4 [one point].
#
#
# Return the rotation index k that corresponds to the highest score we can
# achieve if we rotated nums by it. If there are multiple answers, return the
# smallest such index k.
#
#
# Example 1:
#
#
# Input: nums = [2,3,1,4,0]
# Output: 3
# Explanation: Scores for each k are listed below:
# k = 0,  nums = [2,3,1,4,0],    score 2
# k = 1,  nums = [3,1,4,0,2],    score 3
# k = 2,  nums = [1,4,0,2,3],    score 3
# k = 3,  nums = [4,0,2,3,1],    score 4
# k = 4,  nums = [0,2,3,1,4],    score 3
# So we should choose k = 3, which has the highest score.
#
#
# Example 2:
#
#
# Input: nums = [1,3,0,2,4]
# Output: 0
# Explanation: nums will always have 3 points no matter how it shifts.
# So we will choose the smallest k, which is 0.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 0 <= nums[i] < nums.length
#
#
#

# @lc tags=array;math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 旋转，以获得最多分数，旋转后，如果值小于等于索引，就可以得分。
# 那么每一位是否得分就有一个区间。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def bestRotation(self, nums: List[int]) -> int:

        l = len(nums)
        dp = [0] * (l + 1)
        for i, n in enumerate(nums):

            # left rorate
            if n <= i:
                dp[0] += 1
                dp[(i - n) + 1] -= 1
            # right rorate
            dp[i + 1] += 1
            dp[min(i + 1 + ((l - 1) - n), l - 1) + 1] -= 1
        res = 0
        s = 0
        m = 0
        for i, n in enumerate(dp):
            s += n
            if s > m:
                m = s
                res = i
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,3,1,4,0]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().bestRotation([2, 3, 1, 4, 0])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,3,0,2,4]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().bestRotation([1, 3, 0, 2, 4])))
    print()
    print('Example 1:')
    print('Input : ')
    print('nums = [6,2,8,3,5,2,4,3,7,6]')
    print('Exception :')
    print('9')
    print('Output :')
    print(str(Solution().bestRotation([6, 2, 8, 3, 5, 2, 4, 3, 7, 6])))
    print()
    pass
# @lc main=end