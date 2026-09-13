from bisect import bisect_left
from typing import List


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        ordered = sorted(
            (r, l, w, idx)
            for idx, (l, r, w) in enumerate(intervals)
        )
        n = len(ordered)
        ends = [r for r, l, w, idx in ordered]

        # compatible[i]: number of intervals ending before interval i starts.
        compatible = [
            bisect_left(ends, l)
            for r, l, w, idx in ordered
        ]

        # State: (total weight, sorted tuple of original indices).
        prev = [(0, ())] * (n + 1)

        for k in range(1, 5):
            curr = [(0, ())] * (n + 1)

            for i, (r, l, w, idx) in enumerate(ordered, start=1):
                skip = curr[i - 1]

                weight, indices = prev[compatible[i - 1]]
                take = (
                    weight + w,
                    tuple(sorted(indices + (idx,))),
                )

                if (
                    take[0] > skip[0]
                    or (take[0] == skip[0] and take[1] < skip[1])
                ):
                    curr[i] = take
                else:
                    curr[i] = skip

            prev = curr

        return list(prev[n][1])