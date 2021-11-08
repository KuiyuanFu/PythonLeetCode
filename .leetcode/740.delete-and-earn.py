# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#
# https://leetcode.com/problems/delete-and-earn/description/
#
# algorithms
# Medium (52.41%)
# Likes:    2603
# Dislikes: 173
# Total Accepted:    91.2K
# Total Submissions: 169.9K
# Testcase Example:  '[3,4,2]'
#
# You are given an integer array nums. You want to maximize the number of
# points you get by performing the following operation any number of
# times:
#
#
# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must
# delete every element equal to nums[i] - 1 and every element equal to nums[i]
# + 1.
#
#
# Return the maximum number of points you can earn by applying the above
# operation some number of times.
#
#
# Example 1:
#
#
# Input: nums = [3,4,2]
# Output: 6
# Explanation: You can perform the following operations:
# - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
# - Delete 2 to earn 2 points. nums = [].
# You earn a total of 6 points.
#
#
# Example 2:
#
#
# Input: nums = [2,2,3,3,3,4]
# Output: 9
# Explanation: You can perform the following operations:
# - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums =
# [3,3].
# - Delete a 3 again to earn 3 points. nums = [3].
# - Delete a 3 once more to earn 3 points. nums = [].
# You earn a total of 9 points.
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2 * 10^4
# 1 <= nums[i] <= 10^4
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 最大分数，每次选择一个数获得其分数，之后删掉所有与其绝对值差一的元素。
# dp.
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        nums.sort()
        nums.append(nums[-1] + 1)

        prepreUsed, prepreUnused = 0, 0

        prepreN = nums[0] - 2
        preS = 0
        preN = nums[0]
        for n in nums:
            if preN == n:
                preS += n
            else:
                m = max(prepreUnused, prepreUsed)
                prepreUsed = preS + (prepreUnused if prepreN +
                                     1 == preN else m)
                prepreUnused = m

                prepreN, preN = preN, n
                preS = n

        return max(prepreUnused, prepreUsed)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [3,1]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().deleteAndEarn([3, 1])))
    print()
    print('Example 1:')
    print('Input : ')
    print('nums = [3,4,2]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().deleteAndEarn([3, 4, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [2,2,3,3,3,4]')
    print('Exception :')
    print('9')
    print('Output :')
    print(str(Solution().deleteAndEarn([2, 2, 3, 3, 3, 4])))
    print()

    pass
# @lc main=end