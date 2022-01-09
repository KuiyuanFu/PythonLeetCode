# @lc app=leetcode id=810 lang=python3
#
# [810] Chalkboard XOR Game
#
# https://leetcode.com/problems/chalkboard-xor-game/description/
#
# algorithms
# Hard (52.47%)
# Likes:    112
# Dislikes: 224
# Total Accepted:    6.1K
# Total Submissions: 11.6K
# Testcase Example:  '[1,1,2]'
#
# You are given an array of integers nums represents the numbers written on a
# chalkboard.
#
# Alice and Bob take turns erasing exactly one number from the chalkboard, with
# Alice starting first. If erasing a number causes the bitwise XOR of all the
# elements of the chalkboard to become 0, then that player loses. The bitwise
# XOR of one element is that element itself, and the bitwise XOR of no elements
# is 0.
#
# Also, if any player starts their turn with the bitwise XOR of all the
# elements of the chalkboard equal to 0, then that player wins.
#
# Return true if and only if Alice wins the game, assuming both players play
# optimally.
#
#
# Example 1:
#
#
# Input: nums = [1,1,2]
# Output: false
# Explanation:
# Alice has two choices: erase 1 or erase 2.
# If she erases 1, the nums array becomes [1, 2]. The bitwise XOR of all the
# elements of the chalkboard is 1 XOR 2 = 3. Now Bob can remove any element he
# wants, because Alice will be the one to erase the last element and she will
# lose.
# If Alice erases 2 first, now nums become [1, 1]. The bitwise XOR of all the
# elements of the chalkboard is 1 XOR 1 = 0. Alice will lose.
#
#
# Example 2:
#
#
# Input: nums = [0,1]
# Output: true
#
#
# Example 3:
#
#
# Input: nums = [1,2,3]
# Output: true
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] < 2^16
#
#
#

# @lc tags=math;recursion

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 异或游戏，两者依次去掉一个数，如果使结果成0，就输了。
# 问第一个人是否一定可以获胜。
# 除了全剩一个数，否则总是可以选择到使剩余和不等于0的数。
#
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        from functools import reduce
        r = reduce(lambda x, y: x ^ y, nums)
        return r == 0 or len(nums) % 2 == 0

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,1,2]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().xorGame([1, 1, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [0,1]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().xorGame([0, 1])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1,2,3]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().xorGame([1, 2, 3])))
    print()

    pass
# @lc main=end