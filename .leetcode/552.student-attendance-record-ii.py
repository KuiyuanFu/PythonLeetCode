# @lc app=leetcode id=552 lang=python3
#
# [552] Student Attendance Record II
#
# https://leetcode.com/problems/student-attendance-record-ii/description/
#
# algorithms
# Hard (38.86%)
# Likes:    852
# Dislikes: 152
# Total Accepted:    35K
# Total Submissions: 89.6K
# Testcase Example:  '2'
#
# An attendance record for a student can be represented as a string where each
# character signifies whether the student was absent, late, or present on that
# day. The record only contains the following three characters:
#
#
# 'A': Absent.
# 'L': Late.
# 'P': Present.
#
#
# Any student is eligible for an attendance award if they meet both of the
# following criteria:
#
#
# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
#
#
# Given an integer n, return the number of possible attendance records of
# length n that make a student eligible for an attendance award. The answer may
# be very large, so return it modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: n = 2
# Output: 8
# Explanation: There are 8 records with length 2 that are eligible for an
# award:
# "PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" is not eligible because there are 2 absences (there need to be
# fewer than 2).
#
#
# Example 2:
#
#
# Input: n = 1
# Output: 3
#
#
# Example 3:
#
#
# Input: n = 10101
# Output: 183236316
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^5
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定出勤表的长度，求出勤合格的个数。
# 动态规划吧。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def checkRecord(self, n: int) -> int:
        # if n == 1:
        #     return 3
        # elif n == 2:
        #     return 8
        # # PP LP
        # withoutAbsentEndWithZeroLate = 2
        # # PL
        # withoutAbsentEndWithOneLate = 1
        # # LL
        # withoutAbsentEndWithTwoLate = 1
        # # AP LA PA
        # oneAbsentEndWithZeroLate = 3
        # # AL
        # oneAbsentEndWithOneLate = 1
        # #
        # oneAbsentEndWithTwoLate = 0

        # P
        withoutAbsentEndWithZeroLate = 1
        # L
        withoutAbsentEndWithOneLate = 1
        #
        withoutAbsentEndWithTwoLate = 0
        # A
        oneAbsentEndWithZeroLate = 1
        #
        oneAbsentEndWithOneLate = 0
        #
        oneAbsentEndWithTwoLate = 0
        for _ in range(n - 1):
            wazl = withoutAbsentEndWithZeroLate + withoutAbsentEndWithOneLate + withoutAbsentEndWithTwoLate
            waol = withoutAbsentEndWithZeroLate
            wawl = withoutAbsentEndWithOneLate
            oazl = wazl + oneAbsentEndWithZeroLate + oneAbsentEndWithOneLate + oneAbsentEndWithTwoLate
            oaol = oneAbsentEndWithZeroLate
            oawl = oneAbsentEndWithOneLate

            withoutAbsentEndWithZeroLate = wazl % 1000000007
            withoutAbsentEndWithOneLate = waol % 1000000007
            withoutAbsentEndWithTwoLate = wawl % 1000000007
            oneAbsentEndWithZeroLate = oazl % 1000000007
            oneAbsentEndWithOneLate = oaol % 1000000007
            oneAbsentEndWithTwoLate = oawl % 1000000007

        return sum([
            withoutAbsentEndWithZeroLate, withoutAbsentEndWithOneLate,
            withoutAbsentEndWithTwoLate, oneAbsentEndWithZeroLate,
            oneAbsentEndWithOneLate, oneAbsentEndWithTwoLate
        ]) % 1000000007


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 2')
    print('Exception :')
    print('8')
    print('Output :')
    print(str(Solution().checkRecord(2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().checkRecord(1)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 10101')
    print('Exception :')
    print('183236316')
    print('Output :')
    print(str(Solution().checkRecord(10101)))
    print()
    print(str(Solution().checkRecord(3)))
    pass
# @lc main=end