# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (44.40%)
# Likes:    6118
# Dislikes: 257
# Total Accepted:    607.6K
# Total Submissions: 1.4M
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses - 1. You are given an array prerequisites where prerequisites[i] =
# [ai, bi] indicates that you must take course bi first if you want to take
# course ai.
#
#
# For example, the pair [0, 1], indicates that to take course 0 you have to
# first take course 1.
#
#
# Return true if you can finish all courses. Otherwise, return false.
#
#
# Example 1:
#
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
#
#
# Example 2:
#
#
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you
# should also have finished course 1. So it is impossible.
#
#
#
# Constraints:
#
#
# 1 <= numCourses <= 10^5
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.
#
#
#

# @lc tags=depth-first-search;breadth-first-search;graph;topological-sort

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定课程，课程有前置顺序，判断时候可以全部修完。
# 就是判断有向图是否有环。
# 使用拓扑排序来检测。
#
# @lc idea=end

# @lc group=depth-first-search;breadth-first-search;graph;topological-sort

# @lc rank=10


# @lc code=start
class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        dictSucceed = defaultdict(list)
        dictprecursor = defaultdict(int)
        roots = set(range(numCourses))
        for pre in prerequisites:
            dictSucceed[pre[0]].append(pre[1])
            dictprecursor[pre[1]] += 1
            if pre[1] in roots:
                roots.remove(pre[1])

        while roots:
            root = roots.pop()
            if root in dictSucceed:
                succeeds = dictSucceed.pop(root)
                for succeed in succeeds:
                    dictprecursor[succeed] -= 1
                    if dictprecursor[succeed] == 0:
                        dictprecursor.pop(succeed)
                        roots.add(succeed)
        if len(dictprecursor) == 0:
            return True
        else:
            return False


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('numCourses = 2, prerequisites = [[1,0]]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().canFinish(2, [[1, 0]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('numCourses = 2, prerequisites = [[1,0],[0,1]]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().canFinish(2, [[1, 0], [0, 1]])))
    print()

    pass
# @lc main=end