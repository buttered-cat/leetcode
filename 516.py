class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int

        direction of construction
        TLE, no clue...
        """

        str_len = len(s)
        max_len = [[0] * str_len for x in range(str_len)]
        # max_len = [[0] * str_len] * str_len
        # for i in range(str_len):
        #     max_len[i][i] = 1
        #     if i != str_len - 1:
        #         max_len[i][i+1] = 2 if s[i] == s[i + 1] else 1

        for head in reversed(range(str_len)):
            max_len[head][head] = 1
            for tail in range(head + 1, str_len):
                if s[head] == s[tail]:
                    max_len[head][tail] = max_len[head + 1][tail - 1] + 2
                else:
                    max_len[head][tail] = max(
                        max_len[head + 1][tail], max_len[head][tail - 1]
                    )

        return max(map(max, max_len))

    def run(self):
        # pairs = sys.stdin.readline().split()[0]
        print(self.longestPalindromeSubseq("bbbab"))

c = Solution()
c.run()
