# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
# https://leetcode.com/problems/koko-eating-bananas/description/
#
# algorithms
# Medium (54.63%)
# Likes:    3940
# Dislikes: 175
# Total Accepted:    165.5K
# Total Submissions: 302.8K
# Testcase Example:  '[3,6,7,11]\n8'
#
# Koko loves to eat bananas. There are n piles of bananas, the i^th pile has
# piles[i] bananas. The guards have gone and will come back in h hours.
#
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she
# chooses some pile of bananas and eats k bananas from that pile. If the pile
# has less than k bananas, she eats all of them instead and will not eat any
# more bananas during this hour.
#
# Koko likes to eat slowly but still wants to finish eating all the bananas
# before the guards return.
#
# Return the minimum integer k such that she can eat all the bananas within h
# hours.
#
#
# Example 1:
#
#
# Input: piles = [3,6,7,11], h = 8
# Output: 4
#
#
# Example 2:
#
#
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
#
#
# Example 3:
#
#
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
#
#
#
# Constraints:
#
#
# 1 <= piles.length <= 10^4
# piles.length <= h <= 10^9
# 1 <= piles[i] <= 10^9
#
#
#

# @lc tags=two-pointers

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 吃香蕉，给定h小时，需要全部吃完n堆，每堆有个数，一个小时只能吃一堆中的特定数量，求最少的特定数量。
# 二分
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k: int):
            return sum(map(lambda x: (x - 1) // k + 1, piles)) <= h

        l, r = 1, max(piles)

        while l < r:
            m = (l + r) // 2
            if check(m):
                r = m
            else:
                l = m + 1
        return l

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('piles = [3,6,7,11], h = 8')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().minEatingSpeed([3, 6, 7, 11], 8)))
    print()

    print('Example 2:')
    print('Input : ')
    print('piles = [30,11,23,4,20], h = 5')
    print('Exception :')
    print('30')
    print('Output :')
    print(str(Solution().minEatingSpeed([30, 11, 23, 4, 20], 5)))
    print()

    print('Example 3:')
    print('Input : ')
    print('piles = [30,11,23,4,20], h = 6')
    print('Exception :')
    print('23')
    print('Output :')
    print(str(Solution().minEatingSpeed([30, 11, 23, 4, 20], 6)))
    print()

    pass
# @lc main=end