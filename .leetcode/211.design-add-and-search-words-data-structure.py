# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#
# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
#
# algorithms
# Medium (41.04%)
# Likes:    3106
# Dislikes: 130
# Total Accepted:    293.8K
# Total Submissions: 712.7K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n' +
#   '[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# Design a data structure that supports adding new words and finding if a
# string matches any previously added string.
#
# Implement the WordDictionary class:
#
#
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched
# later.
# bool search(word) Returns true if there is any string in the data structure
# that matches word or false otherwise. word may contain dots '.' where dots
# can be matched with any letter.
#
#
#
# Example:
#
#
# Input
#
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]
#
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
#
#
#
# Constraints:
#
#
# 1 <= word.length <= 500
# word in addWord consists lower-case English letters.
# word in search consist of  '.' or lower-case English letters.
# At most 50000 calls will be made to addWord and search.
#
#
#

# @lc tags=backtracking;design;trie

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 设计一个结构可以存储字符串，并进行查找，支持通配符。
# 使用前缀树。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class TreeNode:
    def __init__(self, val: str = ''):
        self.val = val
        self.children = [None] * 26
        self.flag = False


class WordDictionary:
    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        p = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not p.children[index]:
                p.children[index] = TreeNode(c)
            p = p.children[index]
        p.flag = True

    def search(self, word: str) -> bool:
        def recur(p: TreeNode, index: int) -> bool:
            if index == len(word):
                return p.flag
            c = word[index]
            if c == '.':
                for child in p.children:
                    if child and recur(child, index + 1):
                        return True
            else:
                return p.children[ord(c) - ord('a')] and recur(
                    p.children[ord(c) - ord('a')], index + 1)

        return recur(self.root, 0)


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    pass
# @lc main=end