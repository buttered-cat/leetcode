import sys


class Solution(object):
    MAX_N = 10000*10000
    par = [n for n in range(MAX_N)]
    M = 0
    N = 0
    visited = []

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if not any(board):
            return

        for b in board:
            m, n = len(b), len(b[0])

            save = [ij for k in range(m+n) for ij in ((0, k), (k, 0), (m-1, k), (k, n-1))]

            while save:
                i, j = save.pop()
                if 0 <= i < m and 0 <= j < n and b[i][j] == 'O':
                    b[i][j] = 'S'
                    save += (i+1, j), (i-1, j), (i, j-1), (i, j+1)

            b[:] = [['XO'[c == 'S'] for c in b[i]] for i in range(m)]

            for i in range(m):
                print(b[i])



    def run(self):
        # pairs = sys.stdin.readline().split()[0]
        self.solve([['XXXX', 'XOOX', 'XXOX', 'XOXX']])

c = Solution()
c.run()

