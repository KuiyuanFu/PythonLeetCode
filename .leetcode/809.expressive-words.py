# @lc app=leetcode id=809 lang=python3
#
# [809] Expressive Words
#
# https://leetcode.com/problems/expressive-words/description/
#
# algorithms
# Medium (46.27%)
# Likes:    633
# Dislikes: 1499
# Total Accepted:    87.2K
# Total Submissions: 188.5K
# Testcase Example:  '"heeellooo"\n["hello", "hi", "helo"]'
#
# Sometimes people repeat letters to represent extra feeling. For
# example:
#
#
# "hello" -> "heeellooo"
# "hi" -> "hiiii"
#
#
# In these strings like "heeellooo", we have groups of adjacent letters that
# are all the same: "h", "eee", "ll", "ooo".
#
# You are given a string s and an array of query strings words. A query word is
# stretchy if it can be made to be equal to s by any number of applications of
# the following extension operation: choose a group consisting of characters c,
# and add some number of characters c to the group so that the size of the
# group is three or more.
#
#
# For example, starting with "hello", we could do an extension on the group "o"
# to get "hellooo", but we cannot get "helloo" since the group "oo" has a size
# less than three. Also, we could do another extension like "ll" -> "lllll" to
# get "helllllooo". If s = "helllllooo", then the query word "hello" would be
# stretchy because of these two extension operations: query = "hello" ->
# "hellooo" -> "helllllooo" = s.
#
#
# Return the number of query strings that are stretchy.
#
#
# Example 1:
#
#
# Input: s = "heeellooo", words = ["hello", "hi", "helo"]
# Output: 1
# Explanation:
# We can extend "e" and "o" in the word "hello" to get "heeellooo".
# We can't extend "helo" to get "heeellooo" because the group "ll" is not size
# 3 or more.
#
#
# Example 2:
#
#
# Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
# Output: 3
#
#
#
# Constraints:
#
#
# 1 <= s.length, words.length <= 100
# 1 <= words[i].length <= 100
# s and words[i] consist of lowercase letters.
#
#
#

# @lc tags=binary-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 是否有弹性，即是否可以通过增加至少两个相同字符来达到目标字符串。
# 统计字符个数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:

        scs = []
        l = 0
        while l < len(s):
            r = l + 1
            while r < len(s) and s[r] == s[l]:
                r += 1
            scs.append((s[l], r - l))
            l = r
        res = 0
        for w in words:
            if len(w) > len(s):
                continue
            i = 0
            l = 0
            f = True
            while l < len(w):
                r = l + 1
                while r < len(w) and w[r] == w[l]:
                    r += 1
                c = w[l]
                times = r - l
                ct, ctimes = scs[i]
                if (c != ct )\
                    or (ctimes <= 2 and times != ctimes)\
                    or (times > ctimes):
                    f = False
                    break
                i += 1
                l = r

            if f and i == len(scs):
                res += 1
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "heeellooo", words = ["hello", "hi", "helo"]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().expressiveWords("heeellooo",
                                         ["hello", "hi", "helo"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().expressiveWords("zzzzzyyyyy", ["zzyy", "zy", "zyy"])))
    print()

    pass
# @lc main=end