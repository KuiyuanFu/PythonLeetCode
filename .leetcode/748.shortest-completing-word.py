# @lc app=leetcode id=748 lang=python3
#
# [748] Shortest Completing Word
#
# https://leetcode.com/problems/shortest-completing-word/description/
#
# algorithms
# Easy (58.12%)
# Likes:    270
# Dislikes: 793
# Total Accepted:    44.8K
# Total Submissions: 76.7K
# Testcase Example:  '"1s3 PSt"\n["step","steps","stripe","stepple"]'
#
# Given a string licensePlate and an array of strings words, find the shortest
# completing word in words.
#
# A completing word is a word that contains all the letters in licensePlate.
# Ignore numbers and spaces in licensePlate, and treat letters as case
# insensitive. If a letter appears more than once in licensePlate, then it must
# appear in the word the same number of times or more.
#
# For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b'
# (ignoring case), and 'c' twice. Possible completing words are "abccdef",
# "caaacab", and "cbca".
#
# Return the shortest completing word in words. It is guaranteed an answer
# exists. If there are multiple shortest completing words, return the first one
# that occurs in words.
#
#
# Example 1:
#
#
# Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
# Output: "steps"
# Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and
# 't'.
# "step" contains 't' and 'p', but only contains 1 's'.
# "steps" contains 't', 'p', and both 's' characters.
# "stripe" is missing an 's'.
# "stepple" is missing an 's'.
# Since "steps" is the only word containing all the letters, that is the
# answer.
#
#
# Example 2:
#
#
# Input: licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
# Output: "pest"
# Explanation: licensePlate only contains the letter 's'. All the words contain
# 's', but among these "pest", "stew", and "show" are shortest. The answer is
# "pest" because it is the word that appears earliest of the 3.
#
#
# Example 3:
#
#
# Input: licensePlate = "Ah71752", words =
# ["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"]
# Output: "husband"
#
#
# Example 4:
#
#
# Input: licensePlate = "OgEu755", words =
# ["enough","these","play","wide","wonder","box","arrive","money","tax","thus"]
# Output: "enough"
#
#
# Example 5:
#
#
# Input: licensePlate = "iMSlpe4", words =
# ["claim","consumer","student","camera","public","never","wonder","simple","thought","use"]
# Output: "simple"
#
#
#
# Constraints:
#
#
# 1 <= licensePlate.length <= 7
# licensePlate contains digits, letters (uppercase or lowercase), or space '
# '.
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 15
# words[i] consists of lower case English letters.
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 最短的包含指定字母的单词。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def shortestCompletingWord(self, licensePlate: str,
                               words: List[str]) -> str:
        orda = ord('a')

        def toArray(word):
            a = [0] * 26
            for c in word:
                a[ord(c) - orda] += 1
            return a

        def toTa(licensePlate):
            ta = [0] * 26
            licensePlate = licensePlate.lower()
            for c in licensePlate:
                if 'a' <= c <= 'z':
                    ta[ord(c) - orda] += 1
            return ta

        ta = toTa(licensePlate)

        def compare(a, ta):
            for i in range(26):
                if ta[i] > a[i]:
                    return False
            return True

        res, l = '', 16
        for word in words:
            if compare(toArray(word), ta):
                if len(word) < l:
                    res, l = word, len(word)
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]'
    )
    print('Exception :')
    print('"steps"')
    print('Output :')
    print(
        str(Solution().shortestCompletingWord(
            "1s3 PSt", ["step", "steps", "stripe", "stepple"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('licensePlate = "1s3 456", words = ["looks","pest","stew","show"]')
    print('Exception :')
    print('"pest"')
    print('Output :')
    print(
        str(Solution().shortestCompletingWord(
            "1s3 456", ["looks", "pest", "stew", "show"])))
    print()

    print('Example 3:')
    print('Input : ')
    print(
        'licensePlate = "Ah71752", words =["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"]'
    )
    print('Exception :')
    print('"husband"')
    print('Output :')
    print(
        str(Solution().shortestCompletingWord("Ah71752", [
            "suggest", "letter", "of", "husband", "easy", "education", "drug",
            "prevent", "writer", "old"
        ])))
    print()

    print('Example 4:')
    print('Input : ')
    print(
        'licensePlate = "OgEu755", words =["enough","these","play","wide","wonder","box","arrive","money","tax","thus"]'
    )
    print('Exception :')
    print('"enough"')
    print('Output :')
    print(
        str(Solution().shortestCompletingWord("OgEu755", [
            "enough", "these", "play", "wide", "wonder", "box", "arrive",
            "money", "tax", "thus"
        ])))
    print()

    print('Example 5:')
    print('Input : ')
    print(
        'licensePlate = "iMSlpe4", words =["claim","consumer","student","camera","public","never","wonder","simple","thought","use"]'
    )
    print('Exception :')
    print('"simple"')
    print('Output :')
    print(
        str(Solution().shortestCompletingWord("iMSlpe4", [
            "claim", "consumer", "student", "camera", "public", "never",
            "wonder", "simple", "thought", "use"
        ])))
    print()

    pass
# @lc main=end