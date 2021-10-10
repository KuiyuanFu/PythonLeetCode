# @lc app=leetcode id=659 lang=python3
#
# [659] Split Array into Consecutive Subsequences
#
# https://leetcode.com/problems/split-array-into-consecutive-subsequences/description/
#
# algorithms
# Medium (44.84%)
# Likes:    1832
# Dislikes: 514
# Total Accepted:    62.3K
# Total Submissions: 138.7K
# Testcase Example:  '[1,2,3,3,4,5]'
#
# You are given an integer array nums that is sorted in non-decreasing order.
#
# Determine if it is possible to split nums into one or more subsequences such
# that both of the following conditions are true:
#
#
# Each subsequence is a consecutive increasing sequence (i.e. each integer is
# exactly one more than the previous integer).
# All subsequences have a length of 3 or more.
#
#
# Return true if you can split nums according to the above conditions, or false
# otherwise.
#
# A subsequence of an array is a new array that is formed from the original
# array by deleting some (can be none) of the elements without disturbing the
# relative positions of the remaining elements. (i.e., [1,3,5] is a subsequence
# of [1,2,3,4,5] while [1,3,2] is not).
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,3,4,5]
# Output: true
# Explanation: nums can be split into the following subsequences:
# [1,2,3,3,4,5] --> 1, 2, 3
# [1,2,3,3,4,5] --> 3, 4, 5
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,3,4,4,5,5]
# Output: true
# Explanation: nums can be split into the following subsequences:
# [1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
# [1,2,3,3,4,4,5,5] --> 3, 4, 5
#
#
# Example 3:
#
#
# Input: nums = [1,2,3,4,4,5]
# Output: false
# Explanation: It is impossible to split nums into consecutive increasing
# subsequences of length 3 or more.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -1000 <= nums[i] <= 1000
# nums is sorted in non-decreasing order.
#
#
#

# @lc tags=heap;greedy

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将非严格递增数列，分成严格递增1的子序列。
# 动态规划。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        l1, l2, l3 = 0, 0, 0
        nums.append(nums[-1] + 2)
        pre = nums[0] - 2
        l = 0
        for n in nums:
            if pre == n:
                l += 1
            else:
                if l < l1 + l2:
                    return False
                l1, l2, l3 = max(
                    0, l - (l1 + l2 + l3)), l1, l2 + min(l3, l - (l1 + l2))
                l = 1
                if pre != n - 1:
                    if l1 != 0 or l2 != 0:
                        return False
                    l3 = 0
                    l = 1
            pre = n
        return True


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3,3,4,5]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isPossible([1, 2, 3, 3, 4, 5])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,3,3,4,4,5,5]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isPossible([1, 2, 3, 3, 4, 4, 5, 5])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1,2,3,4,4,5]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isPossible([1, 2, 3, 4, 4, 5])))
    print()
    print(str(Solution().isPossible([1])))
    print(str(Solution().isPossible([1, 2])))
    print(str(Solution().isPossible([1, 2, 3])))
    print(str(Solution().isPossible([1, 2, 3, 4, 5, 6])))
    print(str(Solution().isPossible([1, 2, 3, 4, 6, 7, 8, 9, 10, 11])))
    pass
# @lc main=end