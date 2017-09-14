class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int

        Memory Limit Exceeded at first
        notice [:]
        AC
        """

        c_count = [0 for i in range(26)]

        for c in tasks:
            c_count[ord(c) - ord('A')] += 1

        c_count[:] = sorted(c_count)
        h = 25
        while h >= 0 and c_count[h] == c_count[25]:
            h -= 1

        return max(len(tasks), (n+1) * (c_count[25]-1) + 25 - h)

    def run(self):
        print(self.leastInterval(
            ['A', 'A', 'A', 'B', 'B', 'B'], 2
        ))


c = Solution()
c.run()

