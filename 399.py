class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]

        graph: tuple as key
        dictionary changed size during iteration: list(G) force copy
        """

        # closure
        G = dict()
        for eqn in range(len(equations)):
            forward_val = values[eqn]
            backward_val = 1/values[eqn]
            numerator = equations[eqn][0]
            denominator = equations[eqn][1]

            G[(numerator, denominator)] = forward_val
            G[(denominator, numerator)] = backward_val
            G[(numerator, numerator)] = 1.
            G[(denominator, denominator)] = 1.

            for edge in list(G):
                if edge[0] != edge[1]:
                    if edge[0] == numerator and edge[1] != denominator:
                        G[(denominator, edge[1])] = G[edge] * backward_val
                        G[(edge[1], denominator)] = G[(edge[1], edge[0])] * forward_val
                    elif edge[0] == denominator and edge[1] != numerator:
                        G[(numerator, edge[1])] = G[edge] * forward_val
                        G[(edge[1], numerator)] = G[(edge[1], edge[0])] * backward_val

        ans = []
        for q in queries:
            try:
                ans.append(G[tuple(q)])
            except Exception:
                ans.append(-1.0)

        return ans


    def run(self):
        print(self.calcEquation(
            [ ["a", "b"], ["b", "c"] ],
            [2.0, 3.0],
            [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])
        )

c = Solution()
c.run()
