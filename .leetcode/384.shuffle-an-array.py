# @lc app=leetcode id=384 lang=python3
#
# [384] Shuffle an Array
#
# https://leetcode.com/problems/shuffle-an-array/description/
#
# algorithms
# Medium (55.24%)
# Likes:    375
# Dislikes: 402
# Total Accepted:    207K
# Total Submissions: 374.4K
# Testcase Example:  '["Solution","shuffle","reset","shuffle"]\n[[[1,2,3]],[],[],[]]'
#
# Given an integer array nums, design an algorithm to randomly shuffle the
# array. All permutations of the array should be equally likely as a result of
# the shuffling.
#
# Implement the Solution class:
#
#
# Solution(int[] nums) Initializes the object with the integer array nums.
# int[] reset() Resets the array to its original configuration and returns
# it.
# int[] shuffle() Returns a random shuffling of the array.
#
#
#
# Example 1:
#
#
# Input
# ["Solution", "shuffle", "reset", "shuffle"]
# [[[1, 2, 3]], [], [], []]
# Output
# [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
#
# Explanation
# Solution solution = new Solution([1, 2, 3]);
# solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
# ⁠                      // Any permutation of [1,2,3] must be equally likely
# to be returned.
# ⁠                      // Example: return [3, 1, 2]
# solution.reset();      // Resets the array back to its original configuration
# [1,2,3]. Return [1, 2, 3]
# solution.shuffle();    // Returns the random shuffling of array [1,2,3].
# Example: return [1, 3, 2]
#
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 200
# -10^6 <= nums[i] <= 10^6
# All the elements of nums are unique.
# At most 5 * 10^4 calls in total will be made to reset and shuffle.
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定数组，返回随机打乱后的数组。
# 还是蓄水池的思想，每次随机交换之前的位置。
#
# @lc idea=end

# @lc group=reservoir-sampling

# @lc rank=10


# @lc code=start
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        nums = self.nums.copy()
        for i in range(len(nums)):
            j = random.randint(0, i)
            nums[i], nums[j] = nums[j], nums[i]
        return nums


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('')
    print('Exception :')
    print('')
    print('Output :')
    print(str(Solution().__init__(error)))
    print()

    pass
# @lc main=end