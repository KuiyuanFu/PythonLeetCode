# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#
# https://leetcode.com/problems/can-place-flowers/description/
#
# algorithms
# Easy (31.66%)
# Likes:    1791
# Dislikes: 522
# Total Accepted:    202.2K
# Total Submissions: 637.5K
# Testcase Example:  '[1,0,0,0,1]\n1'
#
# You have a long flowerbed in which some of the plots are planted, and some
# are not. However, flowers cannot be planted in adjacent plots.
#
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty
# and 1 means not empty, and an integer n, return if n new flowers can be
# planted in the flowerbed without violating the no-adjacent-flowers rule.
#
#
# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
#
#
# Constraints:
#
#
# 1 <= flowerbed.length <= 2 * 10^4
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 花不能连续，问是否能安放给定数量的花。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], t: int) -> bool:
        flowerbed.append(0)
        l = 1
        n = 0
        for f in flowerbed:
            if f == 0:
                l += 1
                if l == 3:
                    l = 1
                    n += 1
            else:
                l = 0

        return t <= n
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('flowerbed = [1,0,0,0,1], n = 1')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1)))
    print()

    print('Example 2:')
    print('Input : ')
    print('flowerbed = [1,0,0,0,1], n = 2')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2)))
    print()
    print(str(Solution().canPlaceFlowers([1, 0, 0, 0, 0, 0, 1], 2)))
    print(str(Solution().canPlaceFlowers([0, 0, 1, 0, 1], 1)))
    pass
# @lc main=end