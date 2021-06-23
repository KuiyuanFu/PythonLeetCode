# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#
# https://leetcode.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (39.39%)
# Likes:    2911
# Dislikes: 228
# Total Accepted:    211.5K
# Total Submissions: 535.1K
# Testcase Example:  '[3,2,3]'
#
# Given an integer array of size n, find all elements that appear more than ⌊
# n/3 ⌋ times.
#
# Follow-up: Could you solve the problem in linear time and in O(1) space?
#
#
# Example 1:
#
#
# Input: nums = [3,2,3]
# Output: [3]
#
#
# Example 2:
#
#
# Input: nums = [1]
# Output: [1]
#
#
# Example 3:
#
#
# Input: nums = [1,2]
# Output: [1,2]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求数组中，元素个数大于三分之一的元素。
# 更普遍的讲，是求个数大于k分之一的元素。
# 首先最多有k-1个这样的元素，那么就使用k-1长的空间保存可能的元素，要使大于k分之一的元素一定能留到最后，那么就需要保证 n*(k-1)/k 个其他元素，最多执行k-1次减个数的操作。
# 由于空间为k-1，那么对于每个元素，如果已经存储了此元素，元素个数就加一。如果不存在，且还有剩余位置，那就加入到候选中，若没有剩余位置，则所有候选元素个数减一，若个数为零，则移除。这样最多执行k次，才会减一个个数，个数大于n/k的一定会在候选元素集合中。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ret = []
        if not nums:
            return ret
        k = 3

        candidates = {}
        for n in nums:
            if n in candidates:
                candidates[n] += 1
            else:
                if len(candidates) == k - 1:
                    for key in list(candidates.keys()):
                        candidates[key] = candidates[key] - 1
                        if candidates[key] == 0:
                            candidates.pop(key)
                else:
                    candidates[n] = 1
        for key in candidates.keys():
            if nums.count(key) > len(nums) // k:
                ret.append(key)

        return ret


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [3,2,3]')
    print('Exception :')
    print('[3]')
    print('Output :')
    print(str(Solution().majorityElement([3, 2, 3])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1]')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().majorityElement([1])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1,2]')
    print('Exception :')
    print('[1,2]')
    print('Output :')
    print(str(Solution().majorityElement([1, 2])))
    print()

    pass
# @lc main=end