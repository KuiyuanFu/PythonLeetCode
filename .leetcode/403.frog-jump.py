# @lc app=leetcode id=403 lang=python3
#
# [403] Frog Jump
#
# https://leetcode.com/problems/frog-jump/description/
#
# algorithms
# Hard (42.04%)
# Likes:    1849
# Dislikes: 140
# Total Accepted:    131K
# Total Submissions: 310.8K
# Testcase Example:  '[0,1,3,5,6,8,12,17]'
#
# A frog is crossing a river. The river is divided into some number of units,
# and at each unit, there may or may not exist a stone. The frog can jump on a
# stone, but it must not jump into the water.
#
# Given a list of stones' positions (in units) in sorted ascending order,
# determine if the frog can cross the river by landing on the last stone.
# Initially, the frog is on the first stone and assumes the first jump must be
# 1 unit.
#
# If the frog's last jump was k units, its next jump must be either k - 1, k,
# or k + 1 units. The frog can only jump in the forward direction.
#
#
# Example 1:
#
#
# Input: stones = [0,1,3,5,6,8,12,17]
# Output: true
# Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd
# stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3
# units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th
# stone.
#
#
# Example 2:
#
#
# Input: stones = [0,1,2,3,4,8,9,11]
# Output: false
# Explanation: There is no way to jump to the last stone as the gap between the
# 5th and 6th stone is too large.
#
#
#
# Constraints:
#
#
# 2 <= stones.length <= 2000
# 0 <= stones[i] <= 2^31 - 1
# stones[0] == 0
# stones is sorted in a strictly increasing order.
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 青蛙跳河，只能踩石头上，每次跳跃的距离与上一次的距离范围为1。
# 记录每个石头上可能的跳跃距离。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        sd = dict([(s, set()) for s in stones])
        sd[0].add(1)
        for s in stones:
            for d in sd[s]:
                n = s + d
                if n in sd:
                    sd[n].add(d)
                    sd[n].add(d + 1)
                    if d - 1 > 0:
                        sd[n].add(d - 1)
        return len(sd[stones[-1]]) != 0
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('stones = [0,1,3,5,6,8,12,17]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().canCross([0, 1, 3, 5, 6, 8, 12, 17])))
    print()

    print('Example 2:')
    print('Input : ')
    print('stones = [0,1,2,3,4,8,9,11]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().canCross([0, 1, 2, 3, 4, 8, 9, 11])))
    print()

    pass
# @lc main=end