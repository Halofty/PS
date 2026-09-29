from functools import cache

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        # 경로 길이가 홀수면 올바른 괄호 문자열을 만들 수 없음
        if (m + n - 1) % 2 == 1:
            return False

        # 올바른 괄호 문자열은 반드시 '('로 시작해야 함
        if grid[0][0] == ')':
            return False

        # 올바른 괄호 문자열은 반드시 ')'로 끝나야 함
        if grid[m - 1][n - 1] == '(':
            return False

        @cache
        def dfs(r, c, balance):
            # 현재 칸의 괄호를 balance에 반영
            if grid[r][c] == '(':
                balance += 1
            else:
                balance -= 1

            # 닫는 괄호가 더 많아지는 순간 실패
            if balance < 0:
                return False

            # 마지막 칸에 도착
            if r == m - 1 and c == n - 1:
                return balance == 0

            # 아래쪽으로 이동
            if r + 1 < m:
                if dfs(r + 1, c, balance):
                    return True

            # 오른쪽으로 이동
            if c + 1 < n:
                if dfs(r, c + 1, balance):
                    return True

            return False

        return dfs(0, 0, 0)