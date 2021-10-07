# @lc app=leetcode id=630 lang=python3
#
# [630] Course Schedule III
#
# https://leetcode.com/problems/course-schedule-iii/description/
#
# algorithms
# Hard (35.14%)
# Likes:    1619
# Dislikes: 48
# Total Accepted:    49.6K
# Total Submissions: 140.8K
# Testcase Example:  '[[100,200],[200,1300],[1000,1250],[2000,3200]]'
#
# There are n different online courses numbered from 1 to n. You are given an
# array courses where courses[i] = [durationi, lastDayi] indicate that the i^th
# course should be taken continuously for durationi days and must be finished
# before or on lastDayi.
#
# You will start on the 1^st day and you cannot take two or more courses
# simultaneously.
#
# Return the maximum number of courses that you can take.
#
#
# Example 1:
#
#
# Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
# Output: 3
# Explanation:
# There are totally 4 courses, but you can take 3 courses at most:
# First, take the 1^st course, it costs 100 days so you will finish it on the
# 100^th day, and ready to take the next course on the 101^st day.
# Second, take the 3^rd course, it costs 1000 days so you will finish it on the
# 1100^th day, and ready to take the next course on the 1101^st day.
# Third, take the 2^nd course, it costs 200 days so you will finish it on the
# 1300^th day.
# The 4^th course cannot be taken now, since you will finish it on the 3300^th
# day, which exceeds the closed date.
#
#
# Example 2:
#
#
# Input: courses = [[1,2]]
# Output: 1
#
#
# Example 3:
#
#
# Input: courses = [[3,2],[4,3]]
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= courses.length <= 10^4
# 1 <= durationi, lastDayi <= 10^4
#
#
#

# @lc tags=greedy

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 课程规划，每一个课程有持续时间，和最晚结束时间。求最多上多少课。
# 贪心，题目是在给定时间内上多少课，也就是需要把时间安排满。
# 以结束时间为键排序，之后统计已花费时间，若新加入课程后，时间不超时，那么就加入；否则，去掉最耗时的课程。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = [(e, d) for d, e in courses]
        courses.sort()
        buffer = []
        time = 0
        for e, d in courses:
            time += d
            heappush(buffer, -d)
            if time > e:
                time += heappop(buffer)
        return len(buffer)


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Exception :')
    print('3')
    print(str(Solution().scheduleCourse([[9, 14], [7, 12], [1, 11], [4, 7]])))

    print('Example 1:')
    print('Input : ')
    print('courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]')
    print('Exception :')
    print('3')
    print('Output :')
    print(
        str(Solution().scheduleCourse([[100, 200], [200, 1300], [1000, 1250],
                                       [2000, 3200]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('courses = [[1,2]]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().scheduleCourse([[1, 2]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('courses = [[3,2],[4,3]]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().scheduleCourse([[3, 2], [4, 3]])))
    print()
    print(str(Solution().scheduleCourse([[1, 2], [2, 3]])))
    pass
# @lc main=end