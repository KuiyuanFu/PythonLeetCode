# @lc app=leetcode id=914 lang=python3
#
# [914] X of a Kind in a Deck of Cards
#
# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/description/
#
# algorithms
# Easy (33.00%)
# Likes:    1247
# Dislikes: 305
# Total Accepted:    85.7K
# Total Submissions: 260.4K
# Testcase Example:  '[1,2,3,4,4,3,2,1]'
#
# In a deck of cards, each card has an integer written on it.
#
# Return true if and only if you can choose X >= 2 such that it is possible to
# split the entire deck into 1 or more groups of cards, where:
#
#
# Each group has exactly X cards.
# All the cards in each group have the same integer.
#
#
#
# Example 1:
#
#
# Input: deck = [1,2,3,4,4,3,2,1]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
#
#
# Example 2:
#
#
# Input: deck = [1,1,1,2,2,2,3,3]
# Output: false
# Explanation: No possible partition.
#
#
#
# Constraints:
#
#
# 1 <= deck.length <= 10^4
# 0 <= deck[i] < 10^4
#
#
#

# @lc tags=binary-search;random

# @lc imports=start

from functools import reduce
from imports import *

# @lc imports=end

# @lc idea=start
#
# 是否可以将一组整数分为相同个数，组内相同的数。
# 直接计数，GCD。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        pre = len(deck)
        for _, n in Counter(deck).items():
            pre = gcd(pre, n)
            if pre == 1:
                return False
        return True

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('deck = [1,2,3,4,4,3,2,1]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('deck = [1,1,1,2,2,2,3,3]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3])))
    print()

    pass
# @lc main=end