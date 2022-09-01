# @lc app=leetcode id=950 lang=python3
#
# [950] Reveal Cards In Increasing Order
#
# https://leetcode.com/problems/reveal-cards-in-increasing-order/description/
#
# algorithms
# Medium (77.47%)
# Likes:    2007
# Dislikes: 286
# Total Accepted:    61.1K
# Total Submissions: 78.9K
# Testcase Example:  '[17,13,11,2,3,5,7]'
#
# You are given an integer array deck. There is a deck of cards where every
# card has a unique integer. The integer on the i^th card is deck[i].
#
# You can order the deck in any order you want. Initially, all the cards start
# face down (unrevealed) in one deck.
#
# You will do the following steps repeatedly until all cards are
# revealed:
#
#
# Take the top card of the deck, reveal it, and take it out of the deck.
# If there are still cards in the deck then put the next top card of the deck
# at the bottom of the deck.
# If there are still unrevealed cards, go back to step 1. Otherwise, stop.
#
#
# Return an ordering of the deck that would reveal the cards in increasing
# order.
#
# Note that the first entry in the answer is considered to be the top of the
# deck.
#
#
# Example 1:
#
#
# Input: deck = [17,13,11,2,3,5,7]
# Output: [2,13,3,11,5,17,7]
# Explanation:
# We get the deck in the order [17,13,11,2,3,5,7] (this order does not matter),
# and reorder it.
# After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top
# of the deck.
# We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
# We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
# We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
# We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
# We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
# We reveal 13, and move 17 to the bottom.  The deck is now [17].
# We reveal 17.
# Since all the cards revealed are in increasing order, the answer is
# correct.
#
#
# Example 2:
#
#
# Input: deck = [1,1000]
# Output: [1,1000]
#
#
#
# Constraints:
#
#
# 1 <= deck.length <= 1000
# 1 <= deck[i] <= 10^6
# All the values of deck are unique.
#
#
#

# @lc tags=array;math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定卡牌，数字唯一，每次拿出第一张，把第二张放到最后，循环，直到没有卡牌。求一个初始排序，使结果为递增序列。
# 直接模拟
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        cards = deque(range(len(deck)))
        orders = []

        while cards:
            orders.append(cards.popleft())
            if cards:
                cards.append(cards.popleft())

        deck.sort()
        res = [0] * len(deck)
        for idx, order in enumerate(orders):
            res[order] = deck[idx]
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('deck = [17,13,11,2,3,5,7]')
    print('Exception :')
    print('[2,13,3,11,5,17,7]')
    print('Output :')
    print(str(Solution().deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7])))
    print()

    print('Example 2:')
    print('Input : ')
    print('deck = [1,1000]')
    print('Exception :')
    print('[1,1000]')
    print('Output :')
    print(str(Solution().deckRevealedIncreasing([1, 1000])))
    print()

    pass
# @lc main=end