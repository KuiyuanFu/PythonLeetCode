# @lc app=leetcode id=519 lang=python3
#
# [519] Random Flip Matrix
#
# https://leetcode.com/problems/random-flip-matrix/description/
#
# algorithms
# Medium (38.26%)
# Likes:    247
# Dislikes: 82
# Total Accepted:    11.5K
# Total Submissions: 30K
# Testcase Example:  '["Solution","flip","flip","flip","reset","flip"]\n[[3,1],[],[],[],[],[]]'
#
# There is an m x n binary grid matrix with all the values set 0 initially.
# Design an algorithm to randomly pick an index (i, j) where matrix[i][j] == 0
# and flips it to 1. All the indices (i, j) where matrix[i][j] == 0 should be
# equally likely to be returned.
#
# Optimize your algorithm to minimize the number of calls made to the built-in
# random function of your language and optimize the time and space complexity.
#
# Implement the Solution class:
#
#
# Solution(int m, int n) Initializes the object with the size of the binary
# matrix m and n.
# int[] flip() Returns a random index [i, j] of the matrix where matrix[i][j]
# == 0 and flips it to 1.
# void reset() Resets all the values of the matrix to be 0.
#
#
#
# Example 1:
#
#
# Input
# ["Solution", "flip", "flip", "flip", "reset", "flip"]
# [[3, 1], [], [], [], [], []]
# Output
# [null, [1, 0], [2, 0], [0, 0], null, [2, 0]]
#
# Explanation
# Solution solution = new Solution(3, 1);
# solution.flip();  // return [1, 0], [0,0], [1,0], and [2,0] should be equally
# likely to be returned.
# solution.flip();  // return [2, 0], Since [1,0] was returned, [2,0] and [0,0]
# solution.flip();  // return [0, 0], Based on the previously returned indices,
# only [0,0] can be returned.
# solution.reset(); // All the values are reset to 0 and can be returned.
# solution.flip();  // return [2, 0], [0,0], [1,0], and [2,0] should be equally
# likely to be returned.
#
#
#
# Constraints:
#
#
# 1 <= m, n <= 10^4
# There will be at least one free cell for each call to flip.
# At most 1000 calls will be made to flip and reset.
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 网格，每次随机选取一个为0的格子，置为1.
# 使用树。每个节点存储一个区间，和区间内的剩余数量。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Node:
    def __init__(self, rl, rr) -> None:
        self.left = None
        self.right = None
        self.rangeLeft = rl
        self.rangeRight = rr
        self.c = rr - rl + 1
        pass


class Solution:
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.reset()

    def flip(self) -> List[int]:
        randomInt = random.randrange(1, self.range + 1)
        self.range -= 1
        p = self.root
        while p.rangeLeft != p.rangeRight:
            p.c -= 1
            if not p.left:
                m = (p.rangeRight + p.rangeLeft) // 2
                p.left = Node(p.rangeLeft, m)
                p.right = Node(m + 1, p.rangeRight)
            if randomInt > p.left.c:
                randomInt -= p.left.c
                p = p.right
            else:
                p = p.left
        p.c -= 1
        return [p.rangeLeft // self.n, p.rangeLeft % self.n]

    def reset(self) -> None:
        self.range = self.m * self.n
        self.root = Node(0, self.range - 1)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':

    obj = Solution(3, 1)
    print(obj.flip())
    print(obj.flip())
    print(obj.flip())
    obj.reset()
    print(obj.flip())
    pass
# @lc main=end