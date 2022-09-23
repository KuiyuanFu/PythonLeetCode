# @lc app=leetcode id=985 lang=python3
#
# [985] Sum of Even Numbers After Queries
#
# https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/
#
# algorithms
# Medium (61.19%)
# Likes:    716
# Dislikes: 221
# Total Accepted:    65.8K
# Total Submissions: 107.5K
# Testcase Example:  '[1,2,3,4]\n[[1,0],[-3,1],[-4,0],[2,3]]'
#
# You are given an integer array nums and an array queries where queries[i] =
# [vali, indexi].
#
# For each query i, first, apply nums[indexi] = nums[indexi] + vali, then print
# the sum of the even values of nums.
#
# Return an integer array answer where answer[i] is the answer to the i^th
# query.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
# Output: [8,6,2,4]
# Explanation: At the beginning, the array is [1,2,3,4].
# After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values
# is 2 + 2 + 4 = 8.
# After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even
# values is 2 + 4 = 6.
# After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even
# values is -2 + 4 = 2.
# After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even
# values is -2 + 6 = 4.
#
#
# Example 2:
#
#
# Input: nums = [1], queries = [[4,0]]
# Output: [0]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# 1 <= queries.length <= 10^4
# -10^4 <= vali <= 10^4
# 0 <= indexi < nums.length
#
#
#

# @lc tags=greedy

# @lc imports=start
from logging.config import valid_ident
from imports import *

# @lc imports=end

# @lc idea=start
#
# 统计偶数之和。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def sumEvenAfterQueries(self, nums: List[int],
                            queries: List[List[int]]) -> List[int]:

        res = []
        s = sum(0 if i % 2 == 1 else i for i in nums)

        for v, i in queries:
            n1 = nums[i]
            f1 = n1 % 2 == 0
            n2 = n1 + v
            f2 = n2 % 2 == 0
            nums[i] = n2
            if f1 and f2:
                s += v
            elif f1 and not f2:
                s -= n1
            elif not f1 and f2:
                s += n2
            res.append(s)
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]')
    print('Exception :')
    print('[8,6,2,4]')
    print('Output :')
    print(
        str(Solution().sumEvenAfterQueries(
            [1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1], queries = [[4,0]]')
    print('Exception :')
    print('[0]')
    print('Output :')
    print(str(Solution().sumEvenAfterQueries([1], [[4, 0]])))
    print()

    pass
# @lc main=end