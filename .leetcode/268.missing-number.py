# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
# https://leetcode.com/problems/missing-number/description/
#
# algorithms
# Easy (55.82%)
# Likes:    3249
# Dislikes: 2575
# Total Accepted:    704.1K
# Total Submissions: 1.3M
# Testcase Example:  '[3,0,1]'
#
# Given an array nums containing n distinct numbers in the range [0, n], return
# the only number in the range that is missing from the array.
#
# Follow up: Could you implement a solution using only O(1) extra space
# complexity and O(n) runtime complexity?
#
#
# Example 1:
#
#
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range
# [0,3]. 2 is the missing number in the range since it does not appear in
# nums.
#
#
# Example 2:
#
#
# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range
# [0,2]. 2 is the missing number in the range since it does not appear in
# nums.
#
#
# Example 3:
#
#
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range
# [0,9]. 8 is the missing number in the range since it does not appear in
# nums.
#
#
# Example 4:
#
#
# Input: nums = [0]
# Output: 1
# Explanation: n = 1 since there is 1 number, so all numbers are in the range
# [0,1]. 1 is the missing number in the range since it does not appear in
# nums.
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 10^4
# 0 <= nums[i] <= n
# All the numbers of nums are unique.
#
#
#

# @lc tags=array;math;bit-manipulation

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定n个数字，元素唯一，且处在0-n，找到唯一不存在的数字。
# 直接异或，再异或上所有数字，那么只有唯一的数字只异或了一遍，那么就是结果了。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            n = n ^ i ^ nums[i]
        return n


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [3,0,1]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().missingNumber([3, 0, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [0,1]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().missingNumber([0, 1])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [9,6,4,2,3,5,7,0,1]')
    print('Exception :')
    print('8')
    print('Output :')
    print(str(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])))
    print()

    print('Example 4:')
    print('Input : ')
    print('nums = [0]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().missingNumber([0])))
    print()

    pass
# @lc main=end