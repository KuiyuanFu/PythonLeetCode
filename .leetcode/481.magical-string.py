# @lc app=leetcode id=481 lang=python3
#
# [481] Magical String
#
# https://leetcode.com/problems/magical-string/description/
#
# algorithms
# Medium (48.64%)
# Likes:    148
# Dislikes: 822
# Total Accepted:    25.5K
# Total Submissions: 52.4K
# Testcase Example:  '6'
#
# A magical string s consists of only '1' and '2' and obeys the following
# rules:
#
#
# The string s is magical because concatenating the number of contiguous
# occurrences of characters '1' and '2' generates the string s itself.
#
#
# The first few elements of s is s = "1221121221221121122……". If we group the
# consecutive 1's and 2's in s, it will be "1 22 11 2 1 22 1 22 11 2 11 22
# ......" and the occurrences of 1's or 2's in each group are "1 2 2 1 1 2 1 2
# 2 1 2 2 ......". You can see that the occurrence sequence is s itself.
#
# Given an integer n, return the number of 1's in the first n number in the
# magical string s.
#
#
# Example 1:
#
#
# Input: n = 6
# Output: 3
# Explanation: The first 6 elements of magical string s is "122112" and it
# contains three 1's, so return 3.
#
#
# Example 2:
#
#
# Input: n = 1
# Output: 1
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

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 魔法字符串，由‘1’，‘2’两个字符组成，且统计连续字符串的每节长度，正好等于本身。
# 给定n，求前n个数字中1的个数。
# 直接生成列表，根据当前数字，确定附加的个数，附加的数字和之前的数字相反。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def magicalString(self, count: int) -> int:
        ss = [1, 2, 2]
        idx = 2
        n = 1
        while len(ss) < count:
            times = ss[idx]
            ss.append(n)
            if times == 2 and len(ss) < count:
                ss.append(n)
            n = n ^ 0b11
            idx += 1
        return ss.count(1)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 6')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().magicalString(6)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().magicalString(1)))
    print()

    pass
# @lc main=end