from typing import List


class Solution:
    def backtrack(ans: List[str], cur: str, _open: int, close: int, max: int):
        if (cur.length() == max * 2):
            ans.append(cur)
            return
        if (_open < max):
            backtrack(ans, cur + "(", _open + 1, close, max)
        if (close < _open):
            backtrack(ans, cur + ")", _open, close + 1, max)

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        backtrack(ans, "", 0, 0, n)
        return ans
