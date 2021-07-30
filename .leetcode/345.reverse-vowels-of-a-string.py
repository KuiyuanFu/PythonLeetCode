# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (45.78%)
# Likes:    1169
# Dislikes: 1580
# Total Accepted:    295.3K
# Total Submissions: 644.7K
# Testcase Example:  '"hello"'
#
# Given a string s, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both
# cases.
#
#
# Example 1:
# Input: s = "hello"
# Output: "holle"
# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"
#
#
# Constraints:
#
#
# 1 <= s.length <= 3 * 10^5
# s consist of printable ASCII characters.
#
#
#

# @lc tags=two-pointers;string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 翻转元音。
# 双指针。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = 'aeiouAEIOU'
        sl = [c for c in s]
        l, r = 0, len(sl) - 1
        while True:
            while l < r and sl[l] not in vowel:
                l += 1
            while l < r and sl[r] not in vowel:
                r -= 1
            if l < r:
                sl[l], sl[r] = sl[r], sl[l]
                l += 1
                r -= 1
            else:
                break
        return ''.join(sl)


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "hello"')
    print('Exception :')
    print('"holle"')
    print('Output :')
    print(str(Solution().reverseVowels("hello")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "leetcode"')
    print('Exception :')
    print('"leotcede"')
    print('Output :')
    print(str(Solution().reverseVowels("leetcode")))
    print()

    pass
# @lc main=end