# @lc app=leetcode id=1007 lang=python3
#
# [1007] Minimum Domino Rotations For Equal Row
#
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/description/
#
# algorithms
# Medium (52.44%)
# Likes:    2592
# Dislikes: 239
# Total Accepted:    186.8K
# Total Submissions: 356.2K
# Testcase Example:  '[2,1,2,4,2,2]\n[5,2,6,2,3,2]'
#
# In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom
# halves of the i^th domino. (A domino is a tile with two numbers from 1 to 6 -
# one on each half of the tile.)
#
# We may rotate the i^th domino, so that tops[i] and bottoms[i] swap values.
#
# Return the minimum number of rotations so that all the values in tops are the
# same, or all the values in bottoms are the same.
#
# If it cannot be done, return -1.
#
#
# Example 1:
#
#
# Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
# Output: 2
# Explanation:
# The first figure represents the dominoes as given by tops and bottoms: before
# we do any rotations.
# If we rotate the second and fourth dominoes, we can make every value in the
# top row equal to 2, as indicated by the second figure.
#
#
# Example 2:
#
#
# Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
# Output: -1
# Explanation:
# In this case, it is not possible to rotate the dominoes to make one row of
# values equal.
#
#
#
# Constraints:
#
#
# 2 <= tops.length <= 2 * 10^4
# bottoms.length == tops.length
# 1 <= tops[i], bottoms[i] <= 6
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一组二元值，每次可以呼唤一个二元制，使第一个值相同，或第二个值相同，求最少次数。若不能，则-1。
# 计数
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        length = len(tops)

        counter = defaultdict(int)
        for idx in range(length):
            t = tops[idx]
            b = bottoms[idx]
            counter[t] += 1
            if t != b:
                counter[b] += 1
        for k, v in counter.items():
            if v == length:
                return length - max(tops.count(k), bottoms.count(k))

        return -1

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]')
    print('Exception :')
    print('2')
    print('Output :')
    print(
        str(Solution().minDominoRotations([2, 1, 2, 4, 2, 2],
                                          [5, 2, 6, 2, 3, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().minDominoRotations([3, 5, 1, 2, 3], [3, 6, 3, 3, 4])))
    print()

    pass
# @lc main=end