# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#
# https://leetcode.com/problems/keyboard-row/description/
#
# algorithms
# Easy (66.73%)
# Likes:    730
# Dislikes: 814
# Total Accepted:    135.5K
# Total Submissions: 202.8K
# Testcase Example:  '["Hello","Alaska","Dad","Peace"]'
#
# Given an array of strings words, return the words that can be typed using
# letters of the alphabet on only one row of American keyboard like the image
# below.
#
# In the American keyboard:
#
#
# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".
#
#
#
# Example 1:
#
#
# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]
#
#
# Example 2:
#
#
# Input: words = ["omk"]
# Output: []
#
#
# Example 3:
#
#
# Input: words = ["adsdf","sfd"]
# Output: ["adsdf","sfd"]
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 20
# 1 <= words[i].length <= 100
# words[i] consists of English letters (both lowercase and uppercase).
#
#
#

# @lc tags=hash-table

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断字符串是否可以由键盘一行打出。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        lines = [
            'qwertyuiop',
            'asdfghjkl',
            'zxcvbnm',
        ]
        idies = [0] * 26
        orda = ord('a')
        for i, l in enumerate(lines):
            for c in l:
                idies[ord(c) - orda] = i

        res = []
        for w in words:
            if len(w) == 1:
                res.append(w)
                continue
            idx = idies[ord(w[0].lower()) - orda]
            f = True
            for i in range(1, len(w)):
                c = w[i].lower()
                if idies[ord(c) - orda] != idx:
                    f = False
                    break
            if f:
                res.append(w)
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('words = ["Hello","Alaska","Dad","Peace"]')
    print('Exception :')
    print('["Alaska","Dad"]')
    print('Output :')
    print(str(Solution().findWords(["Hello", "Alaska", "Dad", "Peace"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('words = ["omk"]')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().findWords(["omk"])))
    print()

    print('Example 3:')
    print('Input : ')
    print('words = ["adsdf","sfd"]')
    print('Exception :')
    print('["adsdf","sfd"]')
    print('Output :')
    print(str(Solution().findWords(["adsdf", "sfd"])))
    print()

    pass
# @lc main=end