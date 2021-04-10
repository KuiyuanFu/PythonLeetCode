#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (38.23%)
# Likes:    2272
# Dislikes: 5688
# Total Accepted:    559.1K
# Total Submissions: 1.5M
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
#
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a
# number of rows:
#
#
# string convert(string s, int numRows);
#
#
#
# Example 1:
#
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
#
#
# Example 2:
#
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
#
#
# Example 3:
#
#
# Input: s = "A", numRows = 1
# Output: "A"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000
#
#
#
#
# @lc idea=start
#
# Z字形转换，可以看到，行数为 n 时，除了 n 为 1，其余情况下循环长度为 2n-2 ，之后根据例子，除了第 1 行与第 n 行，其余各行在每个循环中都是有两个值的，且是随着行数增高而靠近的，根据这可以写出代码。
#
# @lc idea=end

from typing import *


# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = ''
        l = len(s)
        stepLength = 2*(numRows - 1)
        for i in range(numRows):
            j = i
            k = stepLength - i
            # 第一行 或 第 n 行
            if j == k or j == 0:
                while j < l:
                    result += s[j]
                    j += stepLength
            else:
                while True:
                    if (j < l):
                        result += s[j]
                        j += stepLength
                    
                    # 左侧的超过范围返回
                    else:
                        break
                    if (k < l):
                        result += s[k]
                    k += stepLength
            pass
        return result


# @lc code=end
if __name__ == "__main__":

    print(Solution().convert("PAYPALISHIRING", 3))
