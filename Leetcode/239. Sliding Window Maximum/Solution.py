# Sliding Window Maximum

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # 값이 아닌 인덱스를 저장
        answer = []

        for i in range(len(nums)):
            # 1. 현재 윈도우에서 벗어난 인덱스 제거
            if dq and dq[0] <= i - k:
                dq.popleft()

            # 2. 현재 값보다 작거나 같은 값의 인덱스 제거
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            # 3. 현재 인덱스 추가
            dq.append(i)

            # 4. 크기가 k인 윈도우가 완성되면 최댓값 저장
            if i >= k - 1:
                answer.append(nums[dq[0]])

        return answer
