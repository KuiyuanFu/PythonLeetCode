# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (54.72%)
# Likes:    3332
# Dislikes: 162
# Total Accepted:    799.3K
# Total Submissions: 1.5M
# Testcase Example:  '"leetcode"'
#
# Given a string s, find the first non-repeating character in it and return its
# index. If it does not exist, return -1.
#
#
# Example 1:
# Input: s = "leetcode"
# Output: 0
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
# Example 3:
# Input: s = "aabb"
# Output: -1
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s consists of only lowercase English letters.
#
#
#

# @lc tags=hash-table;string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 返回第一个没有不重复的索引。
# 字典。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:

        appeared = defaultdict(int)

        for c in s:

            appeared[c] += 1
        for i, c in enumerate(s):
            if appeared[c] == 1:
                return i
        return -1


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "leetcode"')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().firstUniqChar("leetcode")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "loveleetcode"')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().firstUniqChar("loveleetcode")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "aabb"')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().firstUniqChar("aabb")))
    print()

    pass
# @lc main=end