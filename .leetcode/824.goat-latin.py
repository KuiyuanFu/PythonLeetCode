# @lc app=leetcode id=824 lang=python3
#
# [824] Goat Latin
#

# @lc tags=Unknown

# @lc imports=start
from ntpath import join
from imports import *

# @lc imports=end

# @lc idea=start
#
# 转化字符串
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        s = set('aeiouAEIOU')
        return ' '.join(
            (w if w[0] in s else w[1:] + w[0]) + 'ma' + 'a' * (i + 1)
            for i, w in enumerate(sentence.split()))


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('sentence = "I speak Goat Latin"')
    print('Exception :')
    print('"Imaa peaksmaaa oatGmaaaa atinLmaaaaa"')
    print('Output :')
    print(str(Solution().toGoatLatin("I speak Goat Latin")))
    print()

    print('Example 2:')
    print('Input : ')
    print('sentence = "The quick brown fox jumped over the lazy dog"')
    print('Exception :')
    print(
        '"heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaahetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"'
    )
    print('Output :')
    print(
        str(Solution().toGoatLatin(
            "The quick brown fox jumped over the lazy dog")))
    print()

    pass
# @lc main=end