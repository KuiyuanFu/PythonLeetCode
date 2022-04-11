# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#
# https://leetcode.com/problems/boats-to-save-people/description/
#
# algorithms
# Medium (52.42%)
# Likes:    2966
# Dislikes: 79
# Total Accepted:    141.4K
# Total Submissions: 269.7K
# Testcase Example:  '[1,2]\n3'
#
# You are given an array people where people[i] is the weight of the i^th
# person, and an infinite number of boats where each boat can carry a maximum
# weight of limit. Each boat carries at most two people at the same time,
# provided the sum of the weight of those people is at most limit.
#
# Return the minimum number of boats to carry every given person.
#
#
# Example 1:
#
#
# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)
#
#
# Example 2:
#
#
# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)
#
#
# Example 3:
#
#
# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)
#
#
#
# Constraints:
#
#
# 1 <= people.length <= 5 * 10^4
# 1 <= people[i] <= limit <= 3 * 10^4
#
#
#

# @lc tags=depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 每个船有载重上限，且最多两人，求最少船数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        l, r = 0, len(people) - 1
        while l <= r:
            res += 1
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('people = [1,2], limit = 3')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().numRescueBoats([1, 2], 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('people = [3,2,2,1], limit = 3')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().numRescueBoats([3, 2, 2, 1], 3)))
    print()

    print('Example 3:')
    print('Input : ')
    print('people = [3,5,3,4], limit = 5')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().numRescueBoats([3, 5, 3, 4], 5)))
    print()

    pass
# @lc main=end