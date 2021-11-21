# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#
# https://leetcode.com/problems/jewels-and-stones/description/
#
# algorithms
# Easy (87.31%)
# Likes:    3094
# Dislikes: 460
# Total Accepted:    685.6K
# Total Submissions: 784.3K
# Testcase Example:  '"aA"\n"aAAbbbb"'
#
# You're given strings jewels representing the types of stones that are jewels,
# and stones representing the stones you have. Each character in stones is a
# type of stone you have. You want to know how many of the stones you have are
# also jewels.
#
# Letters are case sensitive, so "a" is considered a different type of stone
# from "A".
#
#
# Example 1:
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
# Example 2:
# Input: jewels = "z", stones = "ZZ"
# Output: 0
#
#
# Constraints:
#
#
# 1 <= jewels.length, stones.length <= 50
# jewels and stones consist of only English letters.
# All the characters of jewels are unique.
#
#
#

# @lc tags=tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 计算石头中有多少是宝石。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = set(jewels)
        return [c in j for c in stones].count(True)


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('jewels = "aA", stones = "aAAbbbb"')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().numJewelsInStones("aA", "aAAbbbb")))
    print()

    print('Example 2:')
    print('Input : ')
    print('jewels = "z", stones = "ZZ"')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().numJewelsInStones("z", "ZZ")))
    print()

    pass
# @lc main=end