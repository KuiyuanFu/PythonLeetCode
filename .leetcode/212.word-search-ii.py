# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii/description/
#
# algorithms
# Hard (37.72%)
# Likes:    3882
# Dislikes: 148
# Total Accepted:    311.9K
# Total Submissions: 825.9K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
# '["oath","pea","eat","rain"]'
#
# Given an m x n board of characters and a list of strings words, return all
# words on the board.
#
# Each word must be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once in a word.
#
#
# Example 1:
#
#
# Input: board =
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
#
#
# Example 2:
#
#
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
#
#
#
# Constraints:
#
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 10^4
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.
#
#
#

# @lc tags=backtracking;trie

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个二维棋盘，每个格子是一个字母，判断给定的单词列表中的单词是否可以由相邻字母组成。
# 一棵前缀树，存储所有的单词，之后深度优先遍历棋盘。
# 对于每一个格子，对特定前缀去重。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        rows = len(board)
        cols = len(board[0])
        buffer = [[True for _ in range(cols)] for _ in range(rows)]
        result = set()
        subProblems = set()
        root = {}
        for word in words:
            p = root
            for c in word:
                if c not in p:
                    p[c] = {}
                p = p[c]
            p['#'] = None

        def recur(p, i, j, pre) -> bool:
            if (i, j, pre) in subProblems:
                return
            else:
                subProblems.add((i, j, pre))
            if buffer[i][j]:
                c = board[i][j]

                if c in p:
                    pChild = p[c]
                    if '#' in pChild:
                        result.add(pre + c)
                    buffer[i][j] = False
                    for offsetI, offsetJ in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        if (0 <= i + offsetI < rows
                                and 0 <= j + offsetJ < cols):

                            recur(pChild, i + offsetI, j + offsetJ, pre + c),
                    buffer[i][j] = True

        for i in range(rows):
            for j in range(cols):
                recur(root, i, j, '')

        return list(result)
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(
        str(Solution().findWords(
            [["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"],
             ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
             ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"],
             ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
             ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"],
             ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
             ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"],
             ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
             ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"],
             ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"]], [
                 "ababababaa", "ababababab", "ababababac", "ababababad",
                 "ababababae", "ababababaf", "ababababag", "ababababah",
                 "ababababai", "ababababaj", "ababababak", "ababababal",
                 "ababababam", "ababababan", "ababababao", "ababababap",
                 "ababababaq", "ababababar", "ababababas", "ababababat",
                 "ababababau", "ababababav", "ababababaw", "ababababax",
                 "ababababay", "ababababaz", "ababababba", "ababababbb",
                 "ababababbc", "ababababbd", "ababababbe", "ababababbf",
                 "ababababbg", "ababababbh", "ababababbi", "ababababbj",
                 "ababababbk", "ababababbl", "ababababbm", "ababababbn",
                 "ababababbo", "ababababbp", "ababababbq", "ababababbr",
                 "ababababbs", "ababababbt", "ababababbu", "ababababbv",
                 "ababababbw", "ababababbx", "ababababby", "ababababbz",
                 "ababababca", "ababababcb", "ababababcc", "ababababcd",
                 "ababababce", "ababababcf", "ababababcg", "ababababch",
                 "ababababci", "ababababcj", "ababababck", "ababababcl",
                 "ababababcm", "ababababcn", "ababababco", "ababababcp",
                 "ababababcq", "ababababcr", "ababababcs", "ababababct",
                 "ababababcu", "ababababcv", "ababababcw", "ababababcx",
                 "ababababcy", "ababababcz", "ababababda", "ababababdb",
                 "ababababdc", "ababababdd", "ababababde", "ababababdf",
                 "ababababdg", "ababababdh", "ababababdi", "ababababdj",
                 "ababababdk", "ababababdl", "ababababdm", "ababababdn",
                 "ababababdo", "ababababdp", "ababababdq", "ababababdr",
                 "ababababds", "ababababdt", "ababababdu", "ababababdv",
                 "ababababdw", "ababababdx", "ababababdy", "ababababdz",
                 "ababababea", "ababababeb", "ababababec", "ababababed",
                 "ababababee", "ababababef", "ababababeg", "ababababeh",
                 "ababababei", "ababababej", "ababababek", "ababababel",
                 "ababababem", "ababababen", "ababababeo", "ababababep",
                 "ababababeq", "ababababer", "ababababes", "ababababet",
                 "ababababeu", "ababababev", "ababababew", "ababababex",
                 "ababababey", "ababababez", "ababababfa", "ababababfb",
                 "ababababfc", "ababababfd", "ababababfe", "ababababff",
                 "ababababfg", "ababababfh", "ababababfi", "ababababfj",
                 "ababababfk", "ababababfl", "ababababfm", "ababababfn",
                 "ababababfo", "ababababfp", "ababababfq", "ababababfr",
                 "ababababfs", "ababababft", "ababababfu", "ababababfv",
                 "ababababfw", "ababababfx", "ababababfy", "ababababfz",
                 "ababababga", "ababababgb", "ababababgc", "ababababgd",
                 "ababababge", "ababababgf", "ababababgg", "ababababgh",
                 "ababababgi", "ababababgj", "ababababgk", "ababababgl",
                 "ababababgm", "ababababgn", "ababababgo", "ababababgp",
                 "ababababgq", "ababababgr", "ababababgs", "ababababgt",
                 "ababababgu", "ababababgv", "ababababgw", "ababababgx",
                 "ababababgy", "ababababgz", "ababababha", "ababababhb",
                 "ababababhc", "ababababhd", "ababababhe", "ababababhf",
                 "ababababhg", "ababababhh", "ababababhi", "ababababhj",
                 "ababababhk", "ababababhl", "ababababhm", "ababababhn",
                 "ababababho", "ababababhp", "ababababhq", "ababababhr",
                 "ababababhs", "ababababht", "ababababhu", "ababababhv",
                 "ababababhw", "ababababhx", "ababababhy", "ababababhz",
                 "ababababia", "ababababib", "ababababic", "ababababid",
                 "ababababie", "ababababif", "ababababig", "ababababih",
                 "ababababii", "ababababij", "ababababik", "ababababil",
                 "ababababim", "ababababin", "ababababio", "ababababip",
                 "ababababiq", "ababababir", "ababababis", "ababababit",
                 "ababababiu", "ababababiv", "ababababiw", "ababababix",
                 "ababababiy", "ababababiz", "ababababja", "ababababjb",
                 "ababababjc", "ababababjd", "ababababje", "ababababjf",
                 "ababababjg", "ababababjh", "ababababji", "ababababjj",
                 "ababababjk", "ababababjl", "ababababjm", "ababababjn",
                 "ababababjo", "ababababjp", "ababababjq", "ababababjr",
                 "ababababjs", "ababababjt", "ababababju", "ababababjv",
                 "ababababjw", "ababababjx", "ababababjy", "ababababjz",
                 "ababababka", "ababababkb", "ababababkc", "ababababkd",
                 "ababababke", "ababababkf", "ababababkg", "ababababkh",
                 "ababababki", "ababababkj", "ababababkk", "ababababkl",
                 "ababababkm", "ababababkn", "ababababko", "ababababkp",
                 "ababababkq", "ababababkr", "ababababks", "ababababkt",
                 "ababababku", "ababababkv", "ababababkw", "ababababkx",
                 "ababababky", "ababababkz", "ababababla", "abababablb",
                 "abababablc", "ababababld", "abababable", "abababablf",
                 "abababablg", "abababablh", "ababababli", "abababablj",
                 "abababablk", "ababababll", "abababablm", "ababababln",
                 "abababablo", "abababablp", "abababablq", "abababablr",
                 "ababababls", "abababablt", "abababablu", "abababablv",
                 "abababablw", "abababablx", "abababably", "abababablz",
                 "ababababma", "ababababmb", "ababababmc", "ababababmd",
                 "ababababme", "ababababmf", "ababababmg", "ababababmh",
                 "ababababmi", "ababababmj", "ababababmk", "ababababml",
                 "ababababmm", "ababababmn", "ababababmo", "ababababmp",
                 "ababababmq", "ababababmr", "ababababms", "ababababmt",
                 "ababababmu", "ababababmv", "ababababmw", "ababababmx",
                 "ababababmy", "ababababmz", "ababababna", "ababababnb",
                 "ababababnc", "ababababnd", "ababababne", "ababababnf",
                 "ababababng", "ababababnh", "ababababni", "ababababnj",
                 "ababababnk", "ababababnl", "ababababnm", "ababababnn",
                 "ababababno", "ababababnp", "ababababnq", "ababababnr",
                 "ababababns", "ababababnt", "ababababnu", "ababababnv",
                 "ababababnw", "ababababnx", "ababababny", "ababababnz",
                 "ababababoa", "ababababob", "ababababoc", "ababababod",
                 "ababababoe", "ababababof", "ababababog", "ababababoh",
                 "ababababoi", "ababababoj", "ababababok", "ababababol",
                 "ababababom", "ababababon", "ababababoo", "ababababop",
                 "ababababoq", "ababababor", "ababababos", "ababababot",
                 "ababababou", "ababababov", "ababababow", "ababababox",
                 "ababababoy", "ababababoz", "ababababpa", "ababababpb",
                 "ababababpc", "ababababpd", "ababababpe", "ababababpf",
                 "ababababpg", "ababababph", "ababababpi", "ababababpj",
                 "ababababpk", "ababababpl", "ababababpm", "ababababpn",
                 "ababababpo", "ababababpp", "ababababpq", "ababababpr",
                 "ababababps", "ababababpt", "ababababpu", "ababababpv",
                 "ababababpw", "ababababpx", "ababababpy", "ababababpz",
                 "ababababqa", "ababababqb", "ababababqc", "ababababqd",
                 "ababababqe", "ababababqf", "ababababqg", "ababababqh",
                 "ababababqi", "ababababqj", "ababababqk", "ababababql",
                 "ababababqm", "ababababqn", "ababababqo", "ababababqp",
                 "ababababqq", "ababababqr", "ababababqs", "ababababqt",
                 "ababababqu", "ababababqv", "ababababqw", "ababababqx",
                 "ababababqy", "ababababqz", "ababababra", "ababababrb",
                 "ababababrc", "ababababrd", "ababababre", "ababababrf",
                 "ababababrg", "ababababrh", "ababababri", "ababababrj",
                 "ababababrk", "ababababrl", "ababababrm", "ababababrn",
                 "ababababro", "ababababrp", "ababababrq", "ababababrr",
                 "ababababrs", "ababababrt", "ababababru", "ababababrv",
                 "ababababrw", "ababababrx", "ababababry", "ababababrz",
                 "ababababsa", "ababababsb", "ababababsc", "ababababsd",
                 "ababababse", "ababababsf", "ababababsg", "ababababsh",
                 "ababababsi", "ababababsj", "ababababsk", "ababababsl",
                 "ababababsm", "ababababsn", "ababababso", "ababababsp",
                 "ababababsq", "ababababsr", "ababababss", "ababababst",
                 "ababababsu", "ababababsv", "ababababsw", "ababababsx",
                 "ababababsy", "ababababsz", "ababababta", "ababababtb",
                 "ababababtc", "ababababtd", "ababababte", "ababababtf",
                 "ababababtg", "ababababth", "ababababti", "ababababtj",
                 "ababababtk", "ababababtl", "ababababtm", "ababababtn",
                 "ababababto", "ababababtp", "ababababtq", "ababababtr",
                 "ababababts", "ababababtt", "ababababtu", "ababababtv",
                 "ababababtw", "ababababtx", "ababababty", "ababababtz",
                 "ababababua", "ababababub", "ababababuc", "ababababud",
                 "ababababue", "ababababuf", "ababababug", "ababababuh",
                 "ababababui", "ababababuj", "ababababuk", "ababababul",
                 "ababababum", "ababababun", "ababababuo", "ababababup",
                 "ababababuq", "ababababur", "ababababus", "ababababut",
                 "ababababuu", "ababababuv", "ababababuw", "ababababux",
                 "ababababuy", "ababababuz", "ababababva", "ababababvb",
                 "ababababvc", "ababababvd", "ababababve", "ababababvf",
                 "ababababvg", "ababababvh", "ababababvi", "ababababvj",
                 "ababababvk", "ababababvl", "ababababvm", "ababababvn",
                 "ababababvo", "ababababvp", "ababababvq", "ababababvr",
                 "ababababvs", "ababababvt", "ababababvu", "ababababvv",
                 "ababababvw", "ababababvx", "ababababvy", "ababababvz",
                 "ababababwa", "ababababwb", "ababababwc", "ababababwd",
                 "ababababwe", "ababababwf", "ababababwg", "ababababwh",
                 "ababababwi", "ababababwj", "ababababwk", "ababababwl",
                 "ababababwm", "ababababwn", "ababababwo", "ababababwp",
                 "ababababwq", "ababababwr", "ababababws", "ababababwt",
                 "ababababwu", "ababababwv", "ababababww", "ababababwx",
                 "ababababwy", "ababababwz", "ababababxa", "ababababxb",
                 "ababababxc", "ababababxd", "ababababxe", "ababababxf",
                 "ababababxg", "ababababxh", "ababababxi", "ababababxj",
                 "ababababxk", "ababababxl", "ababababxm", "ababababxn",
                 "ababababxo", "ababababxp", "ababababxq", "ababababxr",
                 "ababababxs", "ababababxt", "ababababxu", "ababababxv",
                 "ababababxw", "ababababxx", "ababababxy", "ababababxz",
                 "ababababya", "ababababyb", "ababababyc", "ababababyd",
                 "ababababye", "ababababyf", "ababababyg", "ababababyh",
                 "ababababyi", "ababababyj", "ababababyk", "ababababyl",
                 "ababababym", "ababababyn", "ababababyo", "ababababyp",
                 "ababababyq", "ababababyr", "ababababys", "ababababyt",
                 "ababababyu", "ababababyv", "ababababyw", "ababababyx",
                 "ababababyy", "ababababyz", "ababababza", "ababababzb",
                 "ababababzc", "ababababzd", "ababababze", "ababababzf",
                 "ababababzg", "ababababzh", "ababababzi", "ababababzj",
                 "ababababzk", "ababababzl", "ababababzm", "ababababzn",
                 "ababababzo", "ababababzp", "ababababzq", "ababababzr",
                 "ababababzs", "ababababzt", "ababababzu", "ababababzv",
                 "ababababzw", "ababababzx", "ababababzy", "ababababzz"
             ])))

    print('Example 1:')
    print('Input : ')
    print(
        'board =[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],words = ["oath","pea","eat","rain"]'
    )
    print('Exception :')
    print('["eat","oath"]')
    print('Output :')
    print(
        str(Solution().findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"],
                                  ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                                 ["oath", "pea", "eat", "rain"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('board = [["a","b"],["c","d"]], words = ["abcb"]')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().findWords([["a", "b"], ["c", "d"]], ["abcb"])))
    print()

    pass
# @lc main=end