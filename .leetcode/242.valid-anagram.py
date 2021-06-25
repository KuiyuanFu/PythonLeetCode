# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (59.19%)
# Likes:    2797
# Dislikes: 166
# Total Accepted:    854.6K
# Total Submissions: 1.4M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
#
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
#
#
# Constraints:
#
#
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
#
#
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
#
#

# @lc tags=hash-table;sort

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断两个字符串是否是字符相互颠倒的。
# 直接字典判断个数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        sDict = defaultdict(int)
        tDict = defaultdict(int)
        for c in s:
            sDict[c] += 1
        for c in t:
            tDict[c] += 1
        if len(sDict) != len(tDict):
            return False
        for k in sDict.keys():
            if k not in tDict or tDict[k] != sDict[k]:
                return False
        return True
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "anagram", t = "nagaram"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isAnagram("anagram", "nagaram")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "rat", t = "car"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isAnagram("rat", "car")))
    print()

    pass
# @lc main=end