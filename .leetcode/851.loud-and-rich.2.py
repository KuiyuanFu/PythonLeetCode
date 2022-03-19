# @lc app=leetcode id=851 lang=python3
#
# [851] Loud and Rich
#
# https://leetcode.com/problems/loud-and-rich/description/
#
# algorithms
# Medium (56.19%)
# Likes:    585
# Dislikes: 535
# Total Accepted:    22.6K
# Total Submissions: 40.2K
# Testcase Example:  '[[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]\n[3,2,5,4,6,1,7,0]'
#
# There is a group of n people labeled from 0 to n - 1 where each person has a
# different amount of money and a different level of quietness.
#
# You are given an array richer where richer[i] = [ai, bi] indicates that ai
# has more money than bi and an integer array quiet where quiet[i] is the
# quietness of the i^th person. All the given data in richer are logically
# correct (i.e., the data will not lead you to a situation where x is richer
# than y and y is richer than x at the same time).
#
# Return an integer array answer where answer[x] = y if y is the least quiet
# person (that is, the person y with the smallest value of quiet[y]) among all
# people who definitely have equal to or more money than the person x.
#
#
# Example 1:
#
#
# Input: richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet =
# [3,2,5,4,6,1,7,0]
# Output: [5,5,2,5,4,5,6,7]
# Explanation:
# answer[0] = 5.
# Person 5 has more money than 3, which has more money than 1, which has more
# money than 0.
# The only person who is quieter (has lower quiet[x]) is person 7, but it is
# not clear if they have more money than person 0.
# answer[7] = 7.
# Among all people that definitely have equal to or more money than person 7
# (which could be persons 3, 4, 5, 6, or 7), the person who is the quietest
# (has lower quiet[x]) is person 7.
# The other answers can be filled out with similar reasoning.
#
#
# Example 2:
#
#
# Input: richer = [], quiet = [0]
# Output: [0]
#
#
#
# Constraints:
#
#
# n == quiet.length
# 1 <= n <= 500
# 0 <= quiet[i] < n
# All the values of quiet are unique.
# 0 <= richer.length <= n * (n - 1) / 2
# 0 <= ai, bi < n
# ai != bi
# All the pairs of richer are unique.
# The observations in richer are all logically consistent.
#
#
#

# @lc tags=string

# @lc imports=start
import enum
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定n个人，与一些拥有钱数大小关系。
# 求大于等于其钱数的人中，最平静的人。
# 传播
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def loudAndRich(self, richer: List[List[int]],
                    quiet: List[int]) -> List[int]:
        length = len(quiet)
        pooerList = [[] for _ in range(length)]
        times = [0] * length
        for r, p in richer:
            pooerList[r].append(p)
            times[p] += 1
        res = list(range(length))
        s = [i for i, t in enumerate(times) if t == 0]

        while s:
            rich = s.pop()
            q, p = quiet[rich], res[rich]
            for poor in pooerList[rich]:
                if q < quiet[poor]:
                    quiet[poor] = q
                    res[poor] = p
                times[poor] -= 1
                if times[poor] == 0:
                    s.append(poor)

        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet =[3,2,5,4,6,1,7,0]'
    )
    print('Exception :')
    print('[5,5,2,5,4,5,6,7]')
    print('Output :')
    print(
        str(Solution().loudAndRich(
            [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]],
            [3, 2, 5, 4, 6, 1, 7, 0])))
    print()

    print('Example 2:')
    print('Input : ')
    print('richer = [], quiet = [0]')
    print('Exception :')
    print('[0]')
    print('Output :')
    print(str(Solution().loudAndRich([], [0])))
    print()

    pass
# @lc main=end