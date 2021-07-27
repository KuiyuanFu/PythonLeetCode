# @lc app=leetcode id=330 lang=python3
#
# [330] Patching Array
#
# https://leetcode.com/problems/patching-array/description/
#
# algorithms
# Hard (35.40%)
# Likes:    681
# Dislikes: 86
# Total Accepted:    40.7K
# Total Submissions: 114.9K
# Testcase Example:  '[1,3]\n6'
#
# Given a sorted integer array nums and an integer n, add/patch elements to the
# array such that any number in the range [1, n] inclusive can be formed by the
# sum of some elements in the array.
#
# Return the minimum number of patches required.
#
#
# Example 1:
#
#
# Input: nums = [1,3], n = 6
# Output: 1
# Explanation:
# Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3,
# 4.
# Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3],
# [2,3], [1,2,3].
# Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
# So we only need 1 patch.
#
#
# Example 2:
#
#
# Input: nums = [1,5,10], n = 20
# Output: 2
# Explanation: The two patches can be [2, 4].
#
#
# Example 3:
#
#
# Input: nums = [1,2,2], n = 5
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 10^4
# nums is sorted in ascending order.
# 1 <= n <= 2^31 - 1
#
#
#

# @lc tags=greedy

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个递增数组，和一个目标值，每次可以向数组中添加一个数，最终使数组中的组合的和，可以覆盖所有下雨等于目标值的正整数。
# 记录现在还不能组成的最小值，如果数组中下一个值小于等于最小值，那么就可以通过组合，使最小值增加此数组元素值的大小；而如果大于最小值，啊么最小值就无法通过组合此数组元素值来达到，需要添加一个额外的数值，最好添加最小值本身，这样可以组合更多的值。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        minimum = 1
        maximum = n
        times = 0
        i = 0
        while minimum <= maximum:
            if i < len(nums) and nums[i] <= minimum:
                minimum += nums[i]
                i += 1
            else:
                minimum += minimum
                times += 1
        return times


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,3], n = 6')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().minPatches([1, 3], 6)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,5,10], n = 20')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().minPatches([1, 5, 10], 20)))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1,2,2], n = 5')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().minPatches([1, 2, 2], 5)))
    print()

    pass
# @lc main=end