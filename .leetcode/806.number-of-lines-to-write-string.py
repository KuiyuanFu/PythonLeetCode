# @lc app=leetcode id=806 lang=python3
#
# [806] Number of Lines To Write String
#
# https://leetcode.com/problems/number-of-lines-to-write-string/description/
#
# algorithms
# Easy (65.75%)
# Likes:    346
# Dislikes: 1081
# Total Accepted:    50K
# Total Submissions: 75.9K
# Testcase Example:  '[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]\n' +
# '"abcdefghijklmnopqrstuvwxyz"'
#
# You are given a string s of lowercase English letters and an array widths
# denoting how many pixels wide each lowercase English letter is. Specifically,
# widths[0] is the width of 'a', widths[1] is the width of 'b', and so on.
#
# You are trying to write s across several lines, where each line is no longer
# than 100 pixels. Starting at the beginning of s, write as many letters on the
# first line such that the total width does not exceed 100 pixels. Then, from
# where you stopped in s, continue writing as many letters as you can on the
# second line. Continue this process until you have written all of s.
#
# Return an array result of length 2 where:
#
#
# result[0] is the total number of lines.
# result[1] is the width of the last line in pixels.
#
#
#
# Example 1:
#
#
# Input: widths =
# [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
# s = "abcdefghijklmnopqrstuvwxyz"
# Output: [3,60]
# Explanation: You can write s as follows:
# abcdefghij  // 100 pixels wide
# klmnopqrst  // 100 pixels wide
# uvwxyz      // 60 pixels wide
# There are a total of 3 lines, and the last line is 60 pixels wide.
#
# Example 2:
#
#
# Input: widths =
# [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
# s = "bbbcccdddaaa"
# Output: [2,4]
# Explanation: You can write s as follows:
# bbbcccdddaa  // 98 pixels wide
# a            // 4 pixels wide
# There are a total of 2 lines, and the last line is 4 pixels wide.
#
#
# Constraints:
#
#
# widths.length == 26
# 2 <= widths[i] <= 10
# 1 <= s.length <= 1000
# s contains only lowercase English letters.
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 简单计数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lc, wc = 0, 101

        for c in s:
            w = widths[ord(c) - ord('a')]
            if wc + w <= 100:
                wc += w
            else:
                lc += 1
                wc = w
        return [lc, wc % 101]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'widths =[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],s = "abcdefghijklmnopqrstuvwxyz"'
    )
    print('Exception :')
    print('[3,60]')
    print('Output :')
    print(
        str(Solution().numberOfLines([
            10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
            10, 10, 10, 10, 10, 10, 10, 10, 10
        ], "abcdefghijklmnopqrstuvwxyz")))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'widths =[4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],s = "bbbcccdddaaa"'
    )
    print('Exception :')
    print('[2,4]')
    print('Output :')
    print(
        str(Solution().numberOfLines([
            4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
            10, 10, 10, 10, 10, 10, 10, 10, 10
        ], "bbbcccdddaaa")))
    print()

    pass
# @lc main=end