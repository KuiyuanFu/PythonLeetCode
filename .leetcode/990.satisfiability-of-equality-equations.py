# @lc app=leetcode id=990 lang=python3
#
# [990] Satisfiability of Equality Equations
#
# https://leetcode.com/problems/satisfiability-of-equality-equations/description/
#
# algorithms
# Medium (50.71%)
# Likes:    1827
# Dislikes: 23
# Total Accepted:    59K
# Total Submissions: 116.3K
# Testcase Example:  '["a==b","b!=a"]'
#
# You are given an array of strings equations that represent relationships
# between variables where each string equations[i] is of length 4 and takes one
# of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase
# letters (not necessarily different) that represent one-letter variable
# names.
#
# Return true if it is possible to assign integers to variable names so as to
# satisfy all the given equations, or false otherwise.
#
#
# Example 1:
#
#
# Input: equations = ["a==b","b!=a"]
# Output: false
# Explanation: If we assign say, a = 1 and b = 1, then the first equation is
# satisfied, but not the second.
# There is no way to assign the variables to satisfy both equations.
#
#
# Example 2:
#
#
# Input: equations = ["b==a","a==b"]
# Output: true
# Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
#
#
#
# Constraints:
#
#
# 1 <= equations.length <= 500
# equations[i].length == 4
# equations[i][0] is a lowercase letter.
# equations[i][1] is either '=' or '!'.
# equations[i][2] is '='.
# equations[i][3] is a lowercase letter.
#
#
#

# @lc tags=hash-table

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定两个比较式子，判断是否成立。
# 先找相同的，在看相同的是否不同
#
# @lc idea=end

# @lc group=graph

# @lc rank=5


# @lc code=start
class Solution:

    def equationsPossible(self, equations: List[str]) -> bool:
        neighbors = defaultdict(lambda: [])
        ne = []
        for e in equations:
            if '!=' in e:
                ne.append(e.split('!='))
            else:
                a, b = e.split('==')
                neighbors[a].append(b)
                neighbors[b].append(a)
        cluster = {}
        visited = set()
        for k in neighbors.keys():
            if k in visited:
                continue
            idx = len(cluster)
            visited.add(k)
            q = [k]
            while q:
                k = q.pop()
                cluster[k] = idx
                for n in neighbors[k]:
                    if n not in visited:
                        visited.add(n)
                        q.append(n)
        for a, b in ne:
            if a == b or (a in cluster and b in cluster
                          and cluster[a] == cluster[b]):
                return False
        return True


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('equations = ["a==b","b!=a"]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().equationsPossible(["a==b", "b!=a"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('equations = ["b==a","a==b"]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().equationsPossible(["b==a", "a==b"])))
    print()

    pass
# @lc main=end