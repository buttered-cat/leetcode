import sys


class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int

        HUMILIATION!
        """


        pairs.sort(key=lambda x: x[1])
        last = [-0x7FFFFFFF, -0x7FFFFFFF]
        ans = 0
        for p in pairs:
            if p[0] > last[1]:
                ans += 1
                last = p
        return ans

        # from operator import itemgetter
        #
        # pairs = sorted(pairs)
        # pair_len = len(pairs)
        #
        # interval_list = [None] * pair_len
        # length = 0
        # interval_list[0] = [pairs[0]]
        # for pair_idx in range(1, pair_len):
        #     for interval in interval_list[length]:
        #
        #
        #
        #
        #
        #
        #
        #
        # max_second_elem = max(pairs, key=itemgetter(1))
        # max_val = pairs[-1][0] if pairs[-1][0] > max_second_elem[1] else max_second_elem[1]
        # chain_len = [[0 for y in range(pair_len)] for x in range(pair_len)]
        # chain_tail_val = [[max_val for y in range(pair_len)] for x in range(pair_len)]
        # chain_len[0][0] = 1
        # chain_tail_val[0][0] = pairs[0][1]
        # best_len = 1
        #
        # for seq_tail in range(1, pair_len):
        #     # chain_tail_val[seq_tail][seq_tail] = pairs[seq_tail][0] - 1   # workaround
        #     for subseq_idx in reversed(range(seq_tail)):
        #         for chain_head in range(subseq_idx+1):
        #             if pairs[seq_tail][0] > chain_tail_val[subseq_idx][chain_head]:
        #                 # extend chain
        #                 length = chain_len[subseq_idx][chain_head] + 1
        #                 if length < best_len - 1:
        #                     continue
        #                 if length >= chain_len[seq_tail][chain_head]:
        #                     # better chain?
        #                     if pairs[seq_tail][1] <= chain_tail_val[seq_tail][chain_head]:
        #                         chain_tail_val[seq_tail][chain_head] = pairs[seq_tail][1]
        #                         chain_len[seq_tail][chain_head] = length
        #                         if length > best_len:
        #                             best_len = length
        #
        #     chain_tail_val[seq_tail][seq_tail] = pairs[seq_tail][1]
        #     chain_len[seq_tail][seq_tail] = 1
        #
        # return max(chain_len[pair_len - 1])


    def run(self):
        # pairs = sys.stdin.readline().split()[0]
        print(self.findLongestChain([[-1,5],[-10,-7],[-6,6],[0,3],[5,8]]))

c = Solution()
c.run()

