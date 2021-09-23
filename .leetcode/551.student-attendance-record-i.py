# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#
# https://leetcode.com/problems/student-attendance-record-i/description/
#
# algorithms
# Easy (46.79%)
# Likes:    139
# Dislikes: 11
# Total Accepted:    122.8K
# Total Submissions: 261.9K
# Testcase Example:  '"PPALLP"'
#
# You are given a string s representing an attendance record for a student
# where each character signifies whether the student was absent, late, or
# present on that day. The record only contains the following three
# characters:
#
#
# 'A': Absent.
# 'L': Late.
# 'P': Present.
#
#
# The student is eligible for an attendance award if they meet both of the
# following criteria:
#
#
# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
#
#
# Return true if the student is eligible for an attendance award, or false
# otherwise.
#
#
# Example 1:
#
#
# Input: s = "PPALLP"
# Output: true
# Explanation: The student has fewer than 2 absences and was never late 3 or
# more consecutive days.
#
#
# Example 2:
#
#
# Input: s = "PPALLL"
# Output: false
# Explanation: The student was late 3 consecutive days in the last 3 days, so
# is not eligible for the award.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s[i] is either 'A', 'L', or 'P'.
#
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 出勤。统计个数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:

        if s.count('A') > 1:
            return False
        if s.count('LLL') > 0:
            return False
        return True

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "PPALLP"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().checkRecord("PPALLP")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "PPALLL"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().checkRecord("PPALLL")))
    print()

    pass
# @lc main=end