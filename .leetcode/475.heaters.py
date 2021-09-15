# @lc app=leetcode id=475 lang=python3
#
# [475] Heaters
#
# https://leetcode.com/problems/heaters/description/
#
# algorithms
# Medium (34.27%)
# Likes:    1064
# Dislikes: 977
# Total Accepted:    78.4K
# Total Submissions: 228.7K
# Testcase Example:  '[1,2,3]\n[2]'
#
# Winter is coming! During the contest, your first job is to design a standard
# heater with a fixed warm radius to warm all the houses.
#
# Every house can be warmed, as long as the house is within the heater's warm
# radius range.
#
# Given the positions of houses and heaters on a horizontal line, return the
# minimum radius standard of heaters so that those heaters could cover all
# houses.
#
# Notice that all the heaters follow your radius standard, and the warm radius
# will the same.
#
#
# Example 1:
#
#
# Input: houses = [1,2,3], heaters = [2]
# Output: 1
# Explanation: The only heater was placed in the position 2, and if we use the
# radius 1 standard, then all the houses can be warmed.
#
#
# Example 2:
#
#
# Input: houses = [1,2,3,4], heaters = [1,4]
# Output: 1
# Explanation: The two heater was placed in the position 1 and 4. We need to
# use radius 1 standard, then all the houses can be warmed.
#
#
# Example 3:
#
#
# Input: houses = [1,5], heaters = [2]
# Output: 3
#
#
#
# Constraints:
#
#
# 1 <= houses.length, heaters.length <= 3 * 10^4
# 1 <= houses[i], heaters[i] <= 10^9
#
#
#

# @lc tags=binary-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 加热器与房间在一个线上，之后每个加热器有一个辐射半径，问辐射半径最小是多少可以加热所有房间。
# 求房间到加热器的最小距离的最大值。
# 排序，依次遍历，加一个最远的加热器，使每次房间都处在两个加热器中间。
#
# @lc idea=end

# @lc group=binary-search

# @lc rank=3


# @lc code=start
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        heaters.append(2 * 10**9)
        i = 2
        l, r = heaters[0], heaters[1]
        res = 0
        for h in houses:
            while h > r:
                l, r, i = r, heaters[i], i + 1
            res = max(res, min(r - h, abs(h - l)))
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('houses = [1,2,3], heaters = [2]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().findRadius([1, 2, 3], [2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('houses = [1,2,3,4], heaters = [1,4]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().findRadius([1, 2, 3, 4], [1, 4])))
    print()

    print('Example 3:')
    print('Input : ')
    print('houses = [1,5], heaters = [2]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().findRadius([1, 5], [2])))
    print()

    pass
# @lc main=end