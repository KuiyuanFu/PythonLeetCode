# @lc app=leetcode id=686 lang=python3
#
# [686] Repeated String Match
#
# https://leetcode.com/problems/repeated-string-match/description/
#
# algorithms
# Medium (33.11%)
# Likes:    1200
# Dislikes: 870
# Total Accepted:    112.8K
# Total Submissions: 340K
# Testcase Example:  '"abcd"\n"cdabcdab"'
#
# Given two strings a and b, return the minimum number of times you should
# repeat string a so that string b is a substring of it. If it is impossible
# for b​​​​​​ to be a substring of a after repeating it, return -1.
#
# Notice: string "abc" repeated 0 times is "",  repeated 1 time is "abc" and
# repeated 2 times is "abcabc".
#
#
# Example 1:
#
#
# Input: a = "abcd", b = "cdabcdab"
# Output: 3
# Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b
# is a substring of it.
#
#
# Example 2:
#
#
# Input: a = "a", b = "aa"
# Output: 2
#
#
# Example 3:
#
#
# Input: a = "a", b = "a"
# Output: 1
#
#
# Example 4:
#
#
# Input: a = "abc", b = "wxyz"
# Output: -1
#
#
#
# Constraints:
#
#
# 1 <= a.length <= 10^4
# 1 <= b.length <= 10^4
# a and b consist of lower-case English letters.
#
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求字符a至少重复多少次，才能让b成为其子串。
# 循环，比较。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if len(b) == 0:
            return 0
        la, lb = len(a), len(b)
        a = a * (2 + lb // la)
        for i in range(la):
            if a[i:i + lb] == b:
                return (i + lb - 1) // la + 1
        return -1


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('a = "abcd", b = "cdabcdab"')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().repeatedStringMatch("abcd", "cdabcdab")))
    print()

    print('Example 2:')
    print('Input : ')
    print('a = "a", b = "aa"')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().repeatedStringMatch("a", "aa")))
    print()

    print('Example 3:')
    print('Input : ')
    print('a = "a", b = "a"')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().repeatedStringMatch("a", "a")))
    print()

    print('Example 4:')
    print('Input : ')
    print('a = "abc", b = "wxyz"')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().repeatedStringMatch("abc", "wxyz")))
    print()

    pass
# @lc main=end