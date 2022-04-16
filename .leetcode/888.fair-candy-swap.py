# @lc app=leetcode id=888 lang=python3
#
# [888] Fair Candy Swap
#
# https://leetcode.com/problems/fair-candy-swap/description/
#
# algorithms
# Easy (60.40%)
# Likes:    1249
# Dislikes: 230
# Total Accepted:    80.5K
# Total Submissions: 133.3K
# Testcase Example:  '[1,1]\n[2,2]'
#
# Alice and Bob have a different total number of candies. You are given two
# integer arrays aliceSizes and bobSizes where aliceSizes[i] is the number of
# candies of the i^th box of candy that Alice has and bobSizes[j] is the number
# of candies of the j^th box of candy that Bob has.
#
# Since they are friends, they would like to exchange one candy box each so
# that after the exchange, they both have the same total amount of candy. The
# total amount of candy a person has is the sum of the number of candies in
# each box they have.
#
# Return an integer array answer where answer[0] is the number of candies in
# the box that Alice must exchange, and answer[1] is the number of candies in
# the box that Bob must exchange. If there are multiple answers, you may return
# any one of them. It is guaranteed that at least one answer exists.
#
#
# Example 1:
#
#
# Input: aliceSizes = [1,1], bobSizes = [2,2]
# Output: [1,2]
#
#
# Example 2:
#
#
# Input: aliceSizes = [1,2], bobSizes = [2,3]
# Output: [1,2]
#
#
# Example 3:
#
#
# Input: aliceSizes = [2], bobSizes = [1,3]
# Output: [2,3]
#
#
#
# Constraints:
#
#
# 1 <= aliceSizes.length, bobSizes.length <= 10^4
# 1 <= aliceSizes[i], bobSizes[j] <= 10^5
# Alice and Bob have a different total number of candies.
# There will be at least one valid answer for the given input.
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 两人各有一组糖果盒子，每次交换一盒，使最终糖果数量相等。求两人各自交换出去的个数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def fairCandySwap(self, aliceSizes: List[int],
                      bobSizes: List[int]) -> List[int]:
        dif = (sum(aliceSizes) - sum(bobSizes)) // 2
        s = set(aliceSizes)
        for b in bobSizes:
            if b + dif in s:
                return [b + dif, b]

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('aliceSizes = [1,1], bobSizes = [2,2]')
    print('Exception :')
    print('[1,2]')
    print('Output :')
    print(str(Solution().fairCandySwap([1, 1], [2, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('aliceSizes = [1,2], bobSizes = [2,3]')
    print('Exception :')
    print('[1,2]')
    print('Output :')
    print(str(Solution().fairCandySwap([1, 2], [2, 3])))
    print()

    print('Example 3:')
    print('Input : ')
    print('aliceSizes = [2], bobSizes = [1,3]')
    print('Exception :')
    print('[2,3]')
    print('Output :')
    print(str(Solution().fairCandySwap([2], [1, 3])))
    print()

    pass
# @lc main=end