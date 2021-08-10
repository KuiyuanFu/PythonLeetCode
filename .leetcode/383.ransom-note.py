# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
# https://leetcode.com/problems/ransom-note/description/
#
# algorithms
# Easy (53.81%)
# Likes:    997
# Dislikes: 252
# Total Accepted:    277K
# Total Submissions: 514.3K
# Testcase Example:  '"a"\n"b"'
#
# Given two stings ransomNote and magazine, return true if ransomNote can be
# constructed from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
#
#
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
#
#
# Constraints:
#
#
# 1 <= ransomNote.length, magazine.length <= 10^5
# ransomNote and magazine consist of lowercase English letters.
#
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断一个字符串是否可以由另外一个字符串构成。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        l = defaultdict(int)
        for c in ransomNote:
            l[c] += 1
        for c in magazine:
            l[c] -= 1
        for k in l:
            if l[k] > 0:
                return False
        return True
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('ransomNote = "a", magazine = "b"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().canConstruct("a", "b")))
    print()

    print('Example 2:')
    print('Input : ')
    print('ransomNote = "aa", magazine = "ab"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().canConstruct("aa", "ab")))
    print()

    print('Example 3:')
    print('Input : ')
    print('ransomNote = "aa", magazine = "aab"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().canConstruct("aa", "aab")))
    print()

    pass
# @lc main=end