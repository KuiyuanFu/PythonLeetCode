# @lc app=leetcode id=966 lang=python3
#
# [966] Vowel Spellchecker
#
# https://leetcode.com/problems/vowel-spellchecker/description/
#
# algorithms
# Medium (51.52%)
# Likes:    363
# Dislikes: 748
# Total Accepted:    36.9K
# Total Submissions: 71.7K
# Testcase Example:  '["KiTe","kite","hare","Hare"]\n' +'["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]'
#
# Given a wordlist, we want to implement a spellchecker that converts a query
# word into a correct word.
#
# For a given query word, the spell checker handles two categories of spelling
# mistakes:
#
#
# Capitalization: If the query matches a word in the wordlist
# (case-insensitive), then the query word is returned with the same case as the
# case in the wordlist.
#
#
# Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
# Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
# Example: wordlist = ["yellow"], query = "yellow": correct =
# "yellow"
#
#
# Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the
# query word with any vowel individually, it matches a word in the wordlist
# (case-insensitive), then the query word is returned with the same case as the
# match in the wordlist.
#
# Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
# Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no
# match)
# Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no
# match)
#
#
#
#
# In addition, the spell checker operates under the following precedence
# rules:
#
#
# When the query exactly matches a word in the wordlist (case-sensitive), you
# should return the same word back.
# When the query matches a word up to capitlization, you should return the
# first such match in the wordlist.
# When the query matches a word up to vowel errors, you should return the first
# such match in the wordlist.
# If the query has no matches in the wordlist, you should return the empty
# string.
#
#
# Given some queries, return a list of words answer, where answer[i] is the
# correct word for query = queries[i].
#
#
# Example 1:
# Input: wordlist = ["KiTe","kite","hare","Hare"], queries =
# ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
# Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
# Example 2:
# Input: wordlist = ["yellow"], queries = ["YellOw"]
# Output: ["yellow"]
#
#
# Constraints:
#
#
# 1 <= wordlist.length, queries.length <= 5000
# 1 <= wordlist[i].length, queries[i].length <= 7
# wordlist[i] and queries[i] consist only of only English letters.
#
#
#

# @lc tags=hash-table;two-pointers

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定字典，再给定查询字符串数组，求结果。
# 如果字典中有查询字符串，那么就返回。若没有，则看是否有不区分大小写的，返回第一个。若再没有，则返回不区分元音的第一个。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def spellchecker(self, wordlist: List[str],
                     queries: List[str]) -> List[str]:

        origin = set()
        capitalization = {}
        vowelErrors = {}
        vowels = set('aeiou')

        def removeVowel(s):
            s = s.lower()
            return ''.join(c if c not in vowels else ' ' for c in s)

        for word in wordlist:
            origin.add(word)
            lower = word.lower()
            if lower not in capitalization:
                capitalization[lower] = word
            vowel = removeVowel(word)
            if vowel not in vowelErrors:
                vowelErrors[vowel] = word

        res = []
        for word in queries:
            if word in origin:
                res.append(word)
            else:
                lower = word.lower()
                if lower in capitalization:
                    res.append(capitalization[lower])
                else:
                    vowel = removeVowel(word)
                    if vowel in vowelErrors:
                        res.append(vowelErrors[vowel])
                    else:
                        res.append('')
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'wordlist = ["KiTe","kite","hare","Hare"], queries =["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]'
    )
    print('Exception :')
    print('["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]')
    print('Output :')
    print(
        str(Solution().spellchecker(["KiTe", "kite", "hare", "Hare"], [
            "kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti",
            "keet", "keto"
        ])))
    print()

    print('Example 2:')
    print('Input : ')
    print('wordlist = ["yellow"], queries = ["YellOw"]')
    print('Exception :')
    print('["yellow"]')
    print('Output :')
    print(str(Solution().spellchecker(["yellow"], ["YellOw"])))
    print()

    pass
# @lc main=end