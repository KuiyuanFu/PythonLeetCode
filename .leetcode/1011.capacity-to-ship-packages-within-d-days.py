# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
#
# algorithms
# Medium (64.40%)
# Likes:    5242
# Dislikes: 113
# Total Accepted:    177.2K
# Total Submissions: 275.2K
# Testcase Example:  '[1,2,3,4,5,6,7,8,9,10]\n5'
#
# A conveyor belt has packages that must be shipped from one port to another
# within days days.
#
# The i^th package on the conveyor belt has a weight of weights[i]. Each day,
# we load the ship with packages on the conveyor belt (in the order given by
# weights). We may not load more weight than the maximum weight capacity of the
# ship.
#
# Return the least weight capacity of the ship that will result in all the
# packages on the conveyor belt being shipped within days days.
#
#
# Example 1:
#
#
# Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# Output: 15
# Explanation: A ship capacity of 15 is the minimum to ship all the packages in
# 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10
#
# Note that the cargo must be shipped in the order given, so using a ship of
# capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6,
# 7), (8), (9), (10) is not allowed.
#
#
# Example 2:
#
#
# Input: weights = [3,2,2,4,1,4], days = 3
# Output: 6
# Explanation: A ship capacity of 6 is the minimum to ship all the packages in
# 3 days like this:
# 1st day: 3, 2
# 2nd day: 2, 4
# 3rd day: 1, 4
#
#
# Example 3:
#
#
# Input: weights = [1,2,3,1,1], days = 4
# Output: 3
# Explanation:
# 1st day: 1
# 2nd day: 2
# 3rd day: 3
# 4th day: 1, 1
#
#
#
# Constraints:
#
#
# 1 <= days <= weights.length <= 5 * 10^4
# 1 <= weights[i] <= 500
#
#

# @lc tags=tree;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一组重量，给定天数，求每天最少容量。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l, r = max(weights), sum(weights)

        while l < r:
            m = (l + r) // 2
            d = days - 1
            t = 0
            for n in weights:
                t += n
                if t > m:
                    t = n

                    d -= 1
                    if d < 0:
                        l = m + 1
                        break
            if d >= 0:
                r = m

        return r

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('weights = [1,2,3,4,5,6,7,8,9,10], days = 5')
    print('Exception :')
    print('15')
    print('Output :')
    print(str(Solution().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)))
    print()

    print('Example 2:')
    print('Input : ')
    print('weights = [3,2,2,4,1,4], days = 3')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().shipWithinDays([3, 2, 2, 4, 1, 4], 3)))
    print()

    print('Example 3:')
    print('Input : ')
    print('weights = [1,2,3,1,1], days = 4')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().shipWithinDays([1, 2, 3, 1, 1], 4)))
    print()

    pass
# @lc main=end