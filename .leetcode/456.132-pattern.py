# @lc app=leetcode id=456 lang=python3
#
# [456] 132 Pattern
#
# https://leetcode.com/problems/132-pattern/description/
#
# algorithms
# Medium (30.70%)
# Likes:    2632
# Dislikes: 150
# Total Accepted:    94.8K
# Total Submissions: 308.7K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array of n integers nums, a 132 pattern is a subsequence of three
# integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] <
# nums[k] < nums[j].
#
# Return true if there is a 132 pattern in nums, otherwise, return false.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,4]
# Output: false
# Explanation: There is no 132 pattern in the sequence.
#
#
# Example 2:
#
#
# Input: nums = [3,1,4,2]
# Output: true
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
#
#
# Example 3:
#
#
# Input: nums = [-1,3,2,0]
# Output: true
# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1,
# 3, 0] and [-1, 2, 0].
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 2 * 10^5
# -10^9 <= nums[i] <= 10^9
#
#
#

# @lc tags=stack

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断给定数组中是否有132模式存在。三个数，中间最高，右侧次之。
# 从右向左遍历，找右侧的最大值，之后只要遇到小于这个值的元素即可。
# 如果一个元素是右侧值，那么需要其左侧有一个大于其的元素。
#
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        rmax = -2000000000 - 1
        rmin = deque([2000000000 + 1])
        for n in reversed(nums):
            while n > rmin[0]:
                rmax = max(rmin.popleft(), rmax)
            if n < rmax:
                return True
            rmin.appendleft(n)
        return False


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3,4]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().find132pattern([1, 2, 3, 4])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [3,1,4,2]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().find132pattern([3, 1, 4, 2])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [-1,3,2,0]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().find132pattern([-1, 3, 2, 0])))
    print()
    print(str(Solution().find132pattern([3, 5, 0, 3, 4])))
    pass
# @lc main=end