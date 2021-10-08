# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#
# https://leetcode.com/problems/replace-words/description/
#
# algorithms
# Medium (60.46%)
# Likes:    1203
# Dislikes: 148
# Total Accepted:    81.2K
# Total Submissions: 133.7K
# Testcase Example:  '["cat","bat","rat"]\n"the cattle was rattled by the battery"'
#
# In English, we have a concept called root, which can be followed by some
# other word to form another longer word - let's call this word successor. For
# example, when the root "an" is followed by the successor word "other", we can
# form a new word "another".
#
# Given a dictionary consisting of many roots and a sentence consisting of
# words separated by spaces, replace all the successors in the sentence with
# the root forming it. If a successor can be replaced by more than one root,
# replace it with the root that has the shortest length.
#
# Return the sentence after the replacement.
#
#
# Example 1:
# Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled
# by the battery"
# Output: "the cat was rat by the bat"
# Example 2:
# Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
# Output: "a a b c"
# Example 3:
# Input: dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa
# aaa aaa aaaaaa bbb baba ababa"
# Output: "a a a a a a a a bbb baba a"
# Example 4:
# Input: dictionary = ["catt","cat","bat","rat"], sentence = "the cattle was
# rattled by the battery"
# Output: "the cat was rat by the bat"
# Example 5:
# Input: dictionary = ["ac","ab"], sentence = "it is abnormal that this
# solution is accepted"
# Output: "it is ab that this solution is ac"
#
#
# Constraints:
#
#
# 1 <= dictionary.length <= 1000
# 1 <= dictionary[i].length <= 100
# dictionary[i] consists of only lower-case letters.
# 1 <= sentence.length <= 10^6
# sentence consists of only lower-case letters and spaces.
# The number of words in sentence is in the range [1, 1000]
# The length of each word in sentence is in the range [1, 1000]
# Each two consecutive words in sentence will be separated by exactly one
# space.
# sentence does not have leading or trailing spaces.
#
#
#

# @lc tags=hash-table;trie

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 用词根替换词。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        s = set(dictionary)
        res = []
        for idx, w in enumerate(sentence.split()):
            for i in range(1, len(w)):
                if w[:i] in s:
                    res.append(w[:i])
                    break
            if idx + 1 != len(res):
                res.append(w)
        return ' '.join(res)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'dictionary = ["cat","bat","rat"], sentence = "the cattle was rattledby the battery"'
    )
    print('Exception :')
    print('"the cat was rat by the bat"')
    print('Output :')
    print(
        str(Solution().replaceWords(["cat", "bat", "rat"],
                                    "the cattle was rattledby the battery")))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"'
    )
    print('Exception :')
    print('"a a b c"')
    print('Output :')
    print(
        str(Solution().replaceWords(["a", "b", "c"],
                                    "aadsfasf absbs bbab cadsfafs")))
    print()

    print('Example 3:')
    print('Input : ')
    print(
        'dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaaaaa aaa aaaaaa bbb baba ababa"'
    )
    print('Exception :')
    print('"a a a a a a a a bbb baba a"')
    print('Output :')
    print(
        str(Solution().replaceWords(
            ["a", "aa", "aaa", "aaaa"],
            "a aa a aaaa aaaaaa aaa aaaaaa bbb baba ababa")))
    print()

    print('Example 4:')
    print('Input : ')
    print(
        'dictionary = ["catt","cat","bat","rat"], sentence = "the cattle was rattled by the battery"'
    )
    print('Exception :')
    print('"the cat was rat by the bat"')
    print('Output :')
    print(
        str(Solution().replaceWords(["catt", "cat", "bat", "rat"],
                                    "the cattle was rattled by the battery")))
    print()

    print('Example 5:')
    print('Input : ')
    print(
        'dictionary = ["ac","ab"], sentence = "it is abnormal that thissolution is accepted"'
    )
    print('Exception :')
    print('"it is ab that this solution is ac"')
    print('Output :')
    print(
        str(Solution().replaceWords(
            ["ac", "ab"], "it is abnormal that thissolution is accepted")))
    print()

    pass
# @lc main=end