import sys

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        # construct table subdiagonal-wise (by length)

        str_len = len(s)
        substr_num = [[0 for y in range(str_len)]for x in range(str_len)]
        for i in range(str_len):
            substr_num[i][i] = 1

        for idx_span in range(1, str_len):
            head = 0
            while head+idx_span < str_len:
                if s[head] == s[head + idx_span]:
                    if idx_span > 1:
                        if substr_num[head+1][head + idx_span - 1] != 0:
                            substr_num[head][head + idx_span] = 1
                    else:
                        substr_num[head][head + idx_span] = 1

                head += 1

        return sum(map(sum, substr_num))


    def run(self):
        # pairs = sys.stdin.readline().split()[0]
        print(self.countSubstrings("abc"))

c = Solution()
c.run()


