# @lc app=leetcode id=676 lang=python3
#
# [676] Implement Magic Dictionary
#
# https://leetcode.com/problems/implement-magic-dictionary/description/
#
# algorithms
# Medium (55.97%)
# Likes:    864
# Dislikes: 168
# Total Accepted:    56K
# Total Submissions: 99.9K
# Testcase Example:  '["MagicDictionary", "buildDict", "search", "search", "search", "search"]\n' +
# '[[], [["hello","leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]'
#
# Design a data structure that is initialized with a list of different words.
# Provided a string, you should determine if you can change exactly one
# character in this string to match any word in the data structure.
#
# Implement the MagicDictionary class:
#
#
# MagicDictionary() Initializes the object.
# void buildDict(String[] dictionary) Sets the data structure with an array of
# distinct strings dictionary.
# bool search(String searchWord) Returns true if you can change exactly one
# character in searchWord to match any string in the data structure, otherwise
# returns false.
#
#
#
# Example 1:
#
#
# Input
# ["MagicDictionary", "buildDict", "search", "search", "search", "search"]
# [[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
# Output
# [null, null, false, true, false, false]
#
# Explanation
# MagicDictionary magicDictionary = new MagicDictionary();
# magicDictionary.buildDict(["hello", "leetcode"]);
# magicDictionary.search("hello"); // return False
# magicDictionary.search("hhllo"); // We can change the second 'h' to 'e' to
# match "hello" so we return True
# magicDictionary.search("hell"); // return False
# magicDictionary.search("leetcoded"); // return False
#
#
#
# Constraints:
#
#
# 1 <= dictionary.length <= 100
# 1 <= dictionary[i].length <= 100
# dictionary[i] consists of only lower-case English letters.
# All the strings in dictionary are distinct.
# 1 <= searchWord.length <= 100
# searchWord consists of only lower-case English letters.
# buildDict will be called only once before search.
# At most 100 calls will be made to search.
#
#
#

# @lc tags=hash-table;trie

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定字典，再给定一个字符串，判断改变一个字符后，是否可以改变成字典中的一个字符串。
# 将一个字符串的每一位依次改变为下划线，这样可以生成所有改变一位的结构。
# 使用字典存储每一个结果与原始字符串的应对关系。
# 搜索的字符串同样处理，如果结构相同且存在不是同样的原始字符串，就返回真。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class MagicDictionary:
    def __init__(self):
        self.d = {}

    def buildDict(self, dictionary: List[str]) -> None:
        d = self.d
        for word in dictionary:

            for i in range(len(word)):
                wc = word[:i] + '_' + word[i + 1:]
                if wc in d:
                    d[wc].append(word)
                else:
                    d[wc] = [word]

    def search(self, searchWord: str) -> bool:
        f = False
        for i in range(len(searchWord)):
            wc = searchWord[:i] + '_' + searchWord[i + 1:]
            if wc in self.d:
                if len(self.d[wc]) > 1 or self.d[wc][0] != searchWord:
                    f = True
                    break
        return f


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('')
    print('Exception :')
    print('')
    print('Output :')
    print(str(Solution().__init__()))
    print()

    pass
# @lc main=end