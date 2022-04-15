# @lc app=leetcode id=886 lang=python3
#
# [886] Possible Bipartition
#
# https://leetcode.com/problems/possible-bipartition/description/
#
# algorithms
# Medium (47.25%)
# Likes:    2235
# Dislikes: 51
# Total Accepted:    104.5K
# Total Submissions: 221.1K
# Testcase Example:  '4\n[[1,2],[1,3],[2,4]]'
#
# We want to split a group of n people (labeled from 1 to n) into two groups of
# any size. Each person may dislike some other people, and they should not go
# into the same group.
#
# Given the integer n and the array dislikes where dislikes[i] = [ai, bi]
# indicates that the person labeled ai does not like the person labeled bi,
# return true if it is possible to split everyone into two groups in this
# way.
#
#
# Example 1:
#
#
# Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4] and group2 [2,3].
#
#
# Example 2:
#
#
# Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false
#
#
# Example 3:
#
#
# Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= n <= 2000
# 0 <= dislikes.length <= 10^4
# dislikes[i].length == 2
# 1 <= dislikes[i][j] <= n
# ai < bi
# All the pairs of dislikes are unique.
#
#
#

# @lc tags=string;stack

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 分组，有相互不喜欢的组合。不喜欢的组合不能分在一组中，问是否可以分成两组。
# 随机取节点，之后判断是否冲突。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        candidates = set(range(1, n + 1))
        dislikesList = [[] for _ in range(n + 1)]
        s1, s2 = set(), set()
        ca1, ca2 = [], []
        for l, r in dislikes:
            dislikesList[l].append(r)
            dislikesList[r].append(l)

        while candidates:
            p = candidates.pop()
            s1.add(p)
            ca1.append(p)
            while ca1:
                while ca1:
                    p = ca1.pop()
                    for pdl in dislikesList[p]:
                        if pdl in s1:
                            return False
                        if pdl not in s2:
                            s2.add(pdl)
                            ca2.append(pdl)
                            candidates.remove(pdl)
                ca1, ca2 = ca2, ca1
                s1, s2 = s2, s1

        return True

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 4, dislikes = [[1,2],[1,3],[2,4]]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().possibleBipartition(4, [[1, 2], [1, 3], [2, 4]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 3, dislikes = [[1,2],[1,3],[2,3]]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().possibleBipartition(3, [[1, 2], [1, 3], [2, 3]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]')
    print('Exception :')
    print('false')
    print('Output :')
    print(
        str(Solution().possibleBipartition(
            5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]])))
    print()

    pass
# @lc main=end