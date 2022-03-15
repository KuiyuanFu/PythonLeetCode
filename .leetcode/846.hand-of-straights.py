# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#
# https://leetcode.com/problems/hand-of-straights/description/
#
# algorithms
# Medium (56.12%)
# Likes:    1284
# Dislikes: 107
# Total Accepted:    84.6K
# Total Submissions: 150.6K
# Testcase Example:  '[1,2,3,6,2,3,4,7,8]\n3'
#
# Alice has some number of cards and she wants to rearrange the cards into
# groups so that each group is of size groupSize, and consists of groupSize
# consecutive cards.
#
# Given an integer array hand where hand[i] is the value written on the i^th
# card and an integer groupSize, return true if she can rearrange the cards, or
# false otherwise.
#
#
# Example 1:
#
#
# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
#
#
# Example 2:
#
#
# Input: hand = [1,2,3,4,5], groupSize = 4
# Output: false
# Explanation: Alice's hand can not be rearranged into groups of 4.
#
#
#
#
# Constraints:
#
#
# 1 <= hand.length <= 10^4
# 0 <= hand[i] <= 10^9
# 1 <= groupSize <= hand.length
#
#
#
# Note: This question is the same as 1296:
# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
#
#

# @lc tags=Unknown

# @lc imports=start
import queue
from imports import *
import collections

# @lc imports=end

# @lc idea=start
#
# 给定每组卡牌大小，问给定手牌是否可以分为指定大小，且每组内卡牌连续。
# 直接排序。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        c = collections.Counter(hand)
        keys = sorted(list(c.keys()))
        endPoints = [0] * len(keys)
        times = 0
        for idx, num in enumerate(keys):
            if times != 0:
                if keys[idx - 1] + 1 != num:
                    return False
            d = c[num] - times
            if d < 0:
                return False
            if d > 0:
                if idx + groupSize - 1 >= len(keys):
                    return False
                endPoints[idx + groupSize - 1] += d
            times += d
            times -= endPoints[idx]

        return True


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('hand = [1,2,3,6,2,3,4,7,8], groupSize = 3')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('hand = [1,2,3,4,5], groupSize = 4')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isNStraightHand([1, 2, 3, 4, 5], 4)))
    print()

    pass
# @lc main=end