# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#
# https://leetcode.com/problems/shortest-palindrome/description/
#
# algorithms
# Hard (30.93%)
# Likes:    1716
# Dislikes: 156
# Total Accepted:    117.8K
# Total Submissions: 380.4K
# Testcase Example:  '"aacecaaa"'
#
# You are given a string s. You can convert s to a palindrome by adding
# characters in front of it.
#
# Return the shortest palindrome you can find by performing this
# transformation.
#
#
# Example 1:
# Input: s = "aacecaaa"
# Output: "aaacecaaa"
# Example 2:
# Input: s = "abcd"
# Output: "dcbabcd"
#
#
# Constraints:
#
#
# 0 <= s.length <= 5 * 10^4
# s consists of lowercase English letters only.
#
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个字符串，转为其为回文，只能在前面加字符。
# 使用KMP算法中建立LPS表的过程，来确定从字符串起始位置开始的最长回文。
# KMP算法，用作字符串匹配，使用额外的一个LPS表，来记录需要匹配的模式的每一位的最长合适前缀。即，模式中此位元素之前n个元素组成的n长序列，与模式前n个元素相同。这样用文本进行匹配时，若文本某一位与模式中此位不匹配时，可以通过LPS表，读取前面相同序列的长度，直接判断是否匹配模式的第n+1个元素，这样就不用从头开始判断了。
# LPS的建立过程，即判断上一位是否与当前位相同，若相同，则加一。否者看上一位的值，如果不为0，说明上一位的是有对应的匹配长度的，接着判断。
#
# @lc idea=end

# @lc group=string

# @lc rank=10


# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        #
        temp = s + '#' + s[::-1]
        table = [0] * len(temp)
        length = 0
        i = 1
        # set LPS
        while i < len(temp):
            if temp[i] == temp[length]:
                length += 1
                table[i] = length
                i += 1
            else:
                # not increase i.
                if length > 0:
                    length = table[length - 1]
                else:
                    length = 0
                    i += 1

        return s[table[-1]:][::-1] + s


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "aacecaaa"')
    print('Exception :')
    print('"aaacecaaa"')
    print('Output :')
    print(str(Solution().shortestPalindrome("aacecaaa")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "abcd"')
    print('Exception :')
    print('"dcbabcd"')
    print('Output :')
    print(str(Solution().shortestPalindrome("abcd")))
    print()

    pass
# @lc main=end