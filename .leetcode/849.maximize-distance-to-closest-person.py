# @lc app=leetcode id=849 lang=python3
#
# [849] Maximize Distance to Closest Person
#
# https://leetcode.com/problems/maximize-distance-to-closest-person/description/
#
# algorithms
# Medium (47.42%)
# Likes:    2521
# Dislikes: 162
# Total Accepted:    167.8K
# Total Submissions: 353.8K
# Testcase Example:  '[1,0,0,0,1,0,1]'
#
# You are given an array representing a row of seats where seats[i] = 1
# represents a person sitting in the i^th seat, and seats[i] = 0 represents
# that the i^th seat is empty (0-indexed).
#
# There is at least one empty seat, and at least one person sitting.
#
# Alex wants to sit in the seat such that the distance between him and the
# closest person to him is maximized.
#
# Return that maximum distance to the closest person.
#
#
# Example 1:
#
#
# Input: seats = [1,0,0,0,1,0,1]
# Output: 2
# Explanation:
# If Alex sits in the second open seat (i.e. seats[2]), then the closest person
# has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
#
#
# Example 2:
#
#
# Input: seats = [1,0,0,0]
# Output: 3
# Explanation:
# If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats
# away.
# This is the maximum distance possible, so the answer is 3.
#
#
# Example 3:
#
#
# Input: seats = [0,1]
# Output: 1
#
#
#
# Constraints:
#
#
# 2 <= seats.length <= 2 * 10^4
# seats[i] is 0 or 1.
# At least one seat is empty.
# At least one seat is occupied.
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 坐座位，距离旁人最大。
# 两次遍历
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        length = len(seats)
        dpRight = [length] * length
        dpRight[0] = dpRight[0] if seats[0] == 0 else 0
        dpLeft = [length] * length
        dpLeft[-1] = dpLeft[-1] if seats[-1] == 0 else 0

        for i in range(1, length):
            dpRight[i] = (dpRight[i - 1] + 1) if seats[i] == 0 else 0
        for i in reversed(range(length - 1)):
            dpLeft[i] = (dpLeft[i + 1] + 1) if seats[i] == 0 else 0

        return max(min(dpRight[i], dpLeft[i]) for i in range(length))


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('seats = [1,0,0,0,1,0,1]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().maxDistToClosest([1, 0, 0, 0, 1, 0, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('seats = [1,0,0,0]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().maxDistToClosest([1, 0, 0, 0])))
    print()

    print('Example 3:')
    print('Input : ')
    print('seats = [0,1]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().maxDistToClosest([0, 1])))
    print()

    pass
# @lc main=end