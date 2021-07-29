# @lc app=leetcode id=336 lang=python3
#
# [336] Palindrome Pairs
#
# https://leetcode.com/problems/palindrome-pairs/description/
#
# algorithms
# Hard (36.04%)
# Likes:    2207
# Dislikes: 203
# Total Accepted:    133.7K
# Total Submissions: 370.9K
# Testcase Example:  '["abcd","dcba","lls","s","sssll"]'
#
# Given a list of unique words, return all the pairs of the distinct indices
# (i, j) in the given list, so that the concatenation of the two words words[i]
# + words[j] is a palindrome.
#
#
# Example 1:
#
#
# Input: words = ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
#
#
# Example 2:
#
#
# Input: words = ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]
#
#
# Example 3:
#
#
# Input: words = ["a",""]
# Output: [[0,1],[1,0]]
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 5000
# 0 <= words[i].length <= 300
# words[i] consists of lower-case English letters.
#
#
#

# @lc tags=hash-table;string;trie

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一系列字符串，求所有两两组合能成回文的组合。
# 直接字典记录所有字符串，查询每一个字符串在右侧时能形成回文的条件。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        from collections import defaultdict
        buffer = {}
        for i, word in enumerate(words):
            buffer[word] = i
        result = set()

        def addResult(i, target, isleft=True):
            if target in buffer:
                j = buffer[target]
                if i != j:
                    if isleft:
                        result.add((j, i))
                    else:
                        result.add((i, j))

        def isPalindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        for i, word in enumerate(words):

            for m in range(len(word) + 1):
                sl = word[:m]
                sr = word[m:]
                if isPalindrome(sl):
                    addResult(i, sr[::-1])
                if isPalindrome(sr):
                    addResult(i, sl[::-1], False)

        return [[p[0], p[1]] for p in result]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Input : ')
    print('words = ["a","b","c","ab","ac","aa"]')
    print('Exception :')
    print('[[3,0],[1,3],[4,0],[2,4],[5,0],[0,5]]')
    print('Output :')
    print(str(Solution().palindromePairs(["a", "b", "c", "ab", "ac", "aa"])))
    print()

    print('Example 1:')
    print('Input : ')
    print('words = ["abcd","dcba","lls","s","sssll"]')
    print('Exception :')
    print('[[0,1],[1,0],[3,2],[2,4]]')
    print('Output :')
    print(
        str(Solution().palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('words = ["bat","tab","cat"]')
    print('Exception :')
    print('[[0,1],[1,0]]')
    print('Output :')
    print(str(Solution().palindromePairs(["bat", "tab", "cat"])))
    print()

    print('Example 3:')
    print('Input : ')
    print('words = ["a",""]')
    print('Exception :')
    print('[[0,1],[1,0]]')
    print('Output :')
    print(str(Solution().palindromePairs(["a", ""])))
    print()

    pass
# @lc main=end