# @lc app=leetcode id=804 lang=python3
#
# [804] Unique Morse Code Words
#
# https://leetcode.com/problems/unique-morse-code-words/description/
#
# algorithms
# Easy (79.37%)
# Likes:    1096
# Dislikes: 953
# Total Accepted:    202.8K
# Total Submissions: 254.7K
# Testcase Example:  '["gin","zen","gig","msg"]'
#
# International Morse Code defines a standard encoding where each letter is
# mapped to a series of dots and dashes, as follows:
#
#
# 'a' maps to ".-",
# 'b' maps to "-...",
# 'c' maps to "-.-.", and so on.
#
#
# For convenience, the full table for the 26 letters of the English alphabet is
# given below:
#
#
#
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
#
# Given an array of strings words where each word can be written as a
# concatenation of the Morse code of each letter.
#
#
# For example, "cab" can be written as "-.-..--...", which is the concatenation
# of "-.-.", ".-", and "-...". We will call such a concatenation the
# transformation of a word.
#
#
# Return the number of different transformations among all words we have.
#
#
# Example 1:
#
#
# Input: words = ["gin","zen","gig","msg"]
# Output: 2
# Explanation: The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
# There are 2 different transformations: "--...-." and "--...--.".
#
#
# Example 2:
#
#
# Input: words = ["a"]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 12
# words[i] consists of lowercase English letters.
#
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 不同摩斯电码的个数。
# 集合。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        s = set()
        ms = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]
        for w in words:
            m = ''.join([ms[ord(c) - ord('a')] for c in w])
            s.add(m)
        return len(s)
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('words = ["gin","zen","gig","msg"]')
    print('Exception :')
    print('2')
    print('Output :')
    print(
        str(Solution().uniqueMorseRepresentations(["gin", "zen", "gig",
                                                   "msg"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('words = ["a"]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().uniqueMorseRepresentations(["a"])))
    print()

    pass
# @lc main=end