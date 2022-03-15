# @lc app=leetcode id=843 lang=python3
#
# [843] Guess the Word
#
# https://leetcode.com/problems/guess-the-word/description/
#
# algorithms
# Hard (43.24%)
# Likes:    1173
# Dislikes: 1297
# Total Accepted:    110.9K
# Total Submissions: 256.7K
# Testcase Example:  '"acckzz"\n["acckzz","ccbazz","eiowzz","abcczz"]\n10'
#
# This is an interactive problem.
#
# You are given an array of unique strings wordlist where wordlist[i] is 6
# letters long, and one word in this list is chosen as secret.
#
# You may call Master.guess(word) to guess a word. The guessed word should have
# type string and must be from the original list with 6 lowercase letters.
#
# This function returns an integer type, representing the number of exact
# matches (value and position) of your guess to the secret word. Also, if your
# guess is not in the given wordlist, it will return -1 instead.
#
# For each test case, you have exactly 10 guesses to guess the word. At the end
# of any number of calls, if you have made 10 or fewer calls to Master.guess
# and at least one of these guesses was secret, then you pass the test case.
#
#
# Example 1:
#
#
# Input: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"],
# numguesses = 10
# Output: You guessed the secret word correctly.
# Explanation:
# master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
# master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6
# matches.
# master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
# master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
# master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
# We made 5 calls to master.guess and one of them was the secret, so we pass
# the test case.
#
#
# Example 2:
#
#
# Input: secret = "hamada", wordlist = ["hamada","khaled"], numguesses = 10
# Output: You guessed the secret word correctly.
#
#
#
# Constraints:
#
#
# 1 <= wordlist.length <= 100
# wordlist[i].length == 6
# wordlist[i] consist of lowercase English letters.
# All the strings of wordlist are unique.
# secret exists in wordlist.
# numguesses == 10
#
#
#

# @lc tags=Unknown

# @lc imports=start
import collections
import itertools
from imports import *
# @lc imports=end

# @lc idea=start
#
# 给定一系列唯一的字符串，求一个目标字符串，目标字符串一定在给定字符串数组中。
# 给定API，得到测试的字符串与目标字符串的匹配个数。最多猜十次。
# 首先根据字符串两两间的相似度，作为图的边。
# 以上作废。
# 测试字符串，满足此字符串的每个字符，在对应位置上，频次和，最高。
#
# @lc idea=end

# @lc group=graph

# @lc rank=10


class Master:
    def guess(self, word: str) -> int:
        return 1


# @lc code=start
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:


class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def match(w1, w2):
            return sum(i == j for i, j in zip(w1, w2))

        n = 0
        while n < 6:
            count = [
                collections.Counter(w[i] for w in wordlist) for i in range(6)
            ]
            guess = max(wordlist,
                        key=lambda w: sum(count[i][c]
                                          for i, c in enumerate(w)))
            n = master.guess(guess)
            wordlist = [w for w in wordlist if match(w, guess) == n]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"],numguesses = 10'
    )
    print('Exception :')
    print('You guessed the secret word correctly.')
    print('Output :')
    print(str(Solution().findSecretWord(error, error)))
    print()

    print('Example 2:')
    print('Input : ')
    print('secret = "hamada", wordlist = ["hamada","khaled"], numguesses = 10')
    print('Exception :')
    print('You guessed the secret word correctly.')
    print('Output :')
    print(str(Solution().findSecretWord(error, error)))
    print()

    pass
# @lc main=end