import sys


class Solution(object):
    def __init__(self):
        self.MAX_N = 200
        self.par = [i for i in range(self.MAX_N)]
        self.rank = [0 for i in range(self.MAX_N)]

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int

        本机正确提交不正确？
        USE __init__ !
        AC
        """

        N = len(M)
        for i in range(N):
            for j in range(i+1):
                if M[i][j] == 1:
                    self.unite(i, j)

        ans = 0
        for i in range(N):
            if self.par[i] == i:
               ans += 1

        return ans


    def find(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)


    def run(self):
        # print(self.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
        print(self.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))


c = Solution()
c.run()
