# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
# https://leetcode.com/problems/course-schedule-ii/description/
#
# algorithms
# Medium (43.41%)
# Likes:    3972
# Dislikes: 173
# Total Accepted:    415.3K
# Total Submissions: 953.1K
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
# Return the ordering of courses you should take to finish all courses. If
# there are many valid answers, return any of them. If it is impossible to
# finish all courses, return an empty array.
#
#
# Example 1:
#
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you
# should have finished course 0. So the correct course order is [0,1].
#
#
# Example 2:
#
#
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you
# should have finished both courses 1 and 2. Both courses 1 and 2 should be
# taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is
# [0,2,1,3].
#
#
# Example 3:
#
#
# Input: numCourses = 1, prerequisites = []
# Output: [0]
#
#
#
# Constraints:
#
#
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.
#
#
#

# @lc tags=depth-first-search;breadth-first-search;graph;topological-sort

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定课程，课程有前置顺序，判断是否可以全部修完。若可惜修完，返回一个学习顺序。
# 每一对课程，必须先修第二个，才能修第一个。
# 就是判断有向图是否有环。
# 使用拓扑排序来检测。
#
# @lc idea=end

# @lc group=depth-first-search;breadth-first-search;graph;topological-sort

# @lc rank=10


# @lc code=start
class Solution:
    def findOrder(self, numCourses: int,
                  prerequisites: List[List[int]]) -> List[int]:

        from collections import defaultdict
        dictSucceed = defaultdict(list)
        dictprecursor = defaultdict(int)
        roots = set(range(numCourses))
        for pre in prerequisites:
            dictSucceed[pre[1]].append(pre[0])
            dictprecursor[pre[0]] += 1
            if pre[0] in roots:
                roots.remove(pre[0])
        schedule = []
        while roots:
            root = roots.pop()
            schedule.append(root)
            if root in dictSucceed:
                succeeds = dictSucceed.pop(root)
                for succeed in succeeds:
                    dictprecursor[succeed] -= 1
                    if dictprecursor[succeed] == 0:
                        dictprecursor.pop(succeed)
                        roots.add(succeed)
        if len(dictprecursor) == 0:
            return schedule
        else:
            return []


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('numCourses = 2, prerequisites = [[1,0]]')
    print('Exception :')
    print('[0,1]')
    print('Output :')
    print(str(Solution().findOrder(2, [[1, 0]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]')
    print('Exception :')
    print('[0,2,1,3]')
    print('Output :')
    print(str(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('numCourses = 1, prerequisites = []')
    print('Exception :')
    print('[0]')
    print('Output :')
    print(str(Solution().findOrder(1, [])))
    print()

    pass
# @lc main=end