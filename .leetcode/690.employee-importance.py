# @lc app=leetcode id=690 lang=python3
#
# [690] Employee Importance
#
# https://leetcode.com/problems/employee-importance/description/
#
# algorithms
# Easy (60.96%)
# Likes:    1324
# Dislikes: 1103
# Total Accepted:    147.8K
# Total Submissions: 239.9K
# Testcase Example:  '[[1,5,[2,3]],[2,3,[]],[3,3,[]]]\n1'
#
# You have a data structure of employee information, which includes the
# employee's unique ID, their importance value, and their direct subordinates'
# IDs.
#
# You are given an array of employees employees where:
#
#
# employees[i].id is the ID of the i^th employee.
# employees[i].importance is the importance value of the i^th employee.
# employees[i].subordinates is a list of the IDs of the direct subordinates of
# the i^th employee.
#
#
# Given an integer id that represents the ID of an employee, return the total
# importance value of this employee and all their direct subordinates.
#
#
# Example 1:
#
#
# Input: employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
# Output: 11
# Explanation: Employee 1 has an importance value of 5 and has two direct
# subordinates: employee 2 and employee 3.
# They both have an importance value of 3.
# Thus, the total importance value of employee 1 is 5 + 3 + 3 = 11.
#
#
# Example 2:
#
#
# Input: employees = [[1,2,[5]],[5,-3,[]]], id = 5
# Output: -3
# Explanation: Employee 5 has an importance value of -3 and has no direct
# subordinates.
# Thus, the total importance value of employee 5 is -3.
#
#
#
# Constraints:
#
#
# 1 <= employees.length <= 2000
# 1 <= employees[i].id <= 2000
# All employees[i].id are unique.
# -100 <= employees[i].importance <= 100
# One employee has at most one direct leader and may have several
# subordinates.
# The IDs in employees[i].subordinates are valid IDs.
#
#
#

# @lc tags=hash-table;depth-first-search;breadth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 树列表表示法。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d = {}

        for employee in employees:
            d[employee.id] = employee
        res = 0
        q = [id]
        while q:
            e = d[q.pop()]
            res += e.importance
            for id in e.subordinates:
                q.append(id)
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1')
    print('Exception :')
    print('11')
    print('Output :')
    print(str(Solution().__init__(error, error, error)))
    print()

    print('Example 2:')
    print('Input : ')
    print('employees = [[1,2,[5]],[5,-3,[]]], id = 5')
    print('Exception :')
    print('-3')
    print('Output :')
    print(str(Solution().__init__(error, error, error)))
    print()

    pass
# @lc main=end