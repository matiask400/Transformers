def generateParenthesis(self, n: int) -> List[str]:
    def backtrack(S: str, left: int, right: int) -> int:
        if len(S) == n * 2:
            result.append(S)
            return
        if left < n:
            backtrack(S + '(', left + 1, right)
        if right < left:
            backtrack(S + ')', left, right + 1)

    result = []
    backtrack('', 0, 0)
    return result
