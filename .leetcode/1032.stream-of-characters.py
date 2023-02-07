# @lc app=leetcode id=1032 lang=python3
#
# [1032] Stream of Characters
#
# https://leetcode.com/problems/stream-of-characters/description/
#
# algorithms
# Hard (51.58%)
# Likes:    1666
# Dislikes: 176
# Total Accepted:    80.9K
# Total Submissions: 156.9K
# Testcase Example:  '["StreamChecker","query","query","query","query","query","query","query","query","query","query","query","query"]\n' +
# '[[["cd","f","kl"]],["a"],["b"],["c"],["d"],["e"],["f"],["g"],["h"],["i"],["j"],["k"],["l"]]'
#
# Design an algorithm that accepts a stream of characters and checks if a
# suffix of these characters is a string of a given array of strings words.
#
# For example, if words = ["abc", "xyz"] and the stream added the four
# characters (one by one) 'a', 'x', 'y', and 'z', your algorithm should detect
# that the suffix "xyz" of the characters "axyz" matches "xyz" from words.
#
# Implement the StreamChecker class:
#
#
# StreamChecker(String[] words) Initializes the object with the strings array
# words.
# boolean query(char letter) Accepts a new character from the stream and
# returns true if any non-empty suffix from the stream forms a word that is in
# words.
#
#
#
# Example 1:
#
#
# Input
# ["StreamChecker", "query", "query", "query", "query", "query", "query",
# "query", "query", "query", "query", "query", "query"]
# [[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"],
# ["i"], ["j"], ["k"], ["l"]]
# Output
# [null, false, false, false, true, false, true, false, false, false, false,
# false, true]
#
# Explanation
# StreamChecker streamChecker = new StreamChecker(["cd", "f", "kl"]);
# streamChecker.query("a"); // return False
# streamChecker.query("b"); // return False
# streamChecker.query("c"); // return False
# streamChecker.query("d"); // return True, because 'cd' is in the wordlist
# streamChecker.query("e"); // return False
# streamChecker.query("f"); // return True, because 'f' is in the wordlist
# streamChecker.query("g"); // return False
# streamChecker.query("h"); // return False
# streamChecker.query("i"); // return False
# streamChecker.query("j"); // return False
# streamChecker.query("k"); // return False
# streamChecker.query("l"); // return True, because 'kl' is in the wordlist
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 2000
# 1 <= words[i].length <= 200
# words[i] consists of lowercase English letters.
# letter is a lowercase English letter.
# At most 4 * 10^4 calls will be made to query.
#
#
#

# @lc tags=union-find;graph

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一组单词，再给定一个字符流，每出现一个字符，累加在之前的字符后，组成新单词，这个新单词的任意后缀是否出现在给定的单词中。
# 字母树
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = {}
        for word in words:
            p = self.root
            for c in reversed(word):
                if c not in p:
                    p[c] = {}
                p = p[c]
            p['word'] = True
        self.s = []

    def query(self, letter: str) -> bool:
        self.s.append(letter)
        p = self.root
        for i in range(len(self.s) - 1, -1, -1):
            c = self.s[i]
            if c in p:
                p = p[c]
                if 'word' in p:
                    return True
            else:
                break
        return False


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    obj = StreamChecker(["cd", "f", "kl"])
    print(obj.query('a'))
    print(obj.query('b'))
    print(obj.query('c'))
    print(obj.query('d'))
    print(obj.query('e'))
    print(obj.query('f'))
    print(obj.query('g'))
    print(obj.query('h'))
    print(obj.query('i'))
    print(obj.query('j'))
    print(obj.query('k'))
    print(obj.query('l'))

    pass
# @lc main=end