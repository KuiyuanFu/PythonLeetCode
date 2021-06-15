# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (53.20%)
# Likes:    4712
# Dislikes: 71
# Total Accepted:    426.7K
# Total Submissions: 798.7K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n' +
#   '[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# A trie (pronounced as "try") or prefix tree is a tree data structure used to
# efficiently store and retrieve keys in a dataset of strings. There are
# various applications of this data structure, such as autocomplete and
# spellchecker.
#
# Implement the Trie class:
#
#
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie
# (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously
# inserted string word that has the prefix prefix, and false otherwise.
#
#
#
# Example 1:
#
#
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]
#
# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
#
#
#
# Constraints:
#
#
# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 10^4 calls in total will be made to insert, search, and
# startsWith.
#
#
#

# @lc tags=design;trie

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 构造一棵前缀树。
# 每个结点存储一个字母，额外设置一个flag表示是否为单词的终点。
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


class Trie:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        p = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not p.children[index]:
                p.children[index] = TreeNode(c)
            p = p.children[index]
        p.flag = True

    def search(self, word: str) -> bool:
        p = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not p.children[index]:
                return False
            p = p.children[index]
        return p.flag

    def startsWith(self, prefix: str) -> bool:
        word = prefix
        p = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not p.children[index]:
                return False
            p = p.children[index]
        return True


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    # print('Example 1:')
    # print('Input : ')
    # print('')
    # print('Exception :')
    # print('')
    # print('Output :')
    # print(str(Solution().__init__()))
    # print()

    pass
# @lc main=end