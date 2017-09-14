class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        AC
        be careful with reversed
        """

        for i in range(len(Profits)):
            Profits[i] = (Profits[i], -Capital[i])
        Profits[:] = sorted(Profits)
        # not reversed, hurts performance

        num_proj = len(Profits)
        for i in range(k):
            p = num_proj - 1
            # no range, unsure if it hurs performance too? No
            # https://stackoverflow.com/questions/869229/why-is-looping-over-range-in-python-faster-than-using-a-while-loop
            while p >= 0:
                if -Profits[p][1] <= W:
                    W = W + Profits[p][0]
                    Profits.pop(p)
                    break
                p -= 1
            num_proj -= 1

        return W


    def run(self):
        print(self.findMaximizedCapital(2, 0, [1,2,3], [0,1,1]))

c = Solution()
c.run()
