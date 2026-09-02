class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        prefix = [0] * (n + 1)
        for i, value in enumerate(stoneValue):
            prefix[i + 1] = prefix[i] + value

        # dp[left][right]:
        # stoneValue[left:right+1]에서 얻을 수 있는 최대 점수
        dp = [[0] * n for _ in range(n)]

        # best_left[left][right]:
        # max(dp[left][k] + sum(left, k)), left <= k <= right
        best_left = [[0] * n for _ in range(n)]

        # best_right[left][right]:
        # max(dp[k][right] + sum(k, right)), left <= k <= right
        best_right = [[0] * n for _ in range(n)]

        for i, value in enumerate(stoneValue):
            best_left[i][i] = value
            best_right[i][i] = value

        # dp[mid + 1][right]를 먼저 계산해야 하므로 left를 역순으로 처리
        for left in range(n - 1, -1, -1):
            boundary = left - 1

            for right in range(left + 1, n):
                # left_sum <= right_sum인 마지막 분할점을 찾는다.
                while boundary + 1 < right:
                    next_mid = boundary + 1

                    left_sum = (
                        prefix[next_mid + 1] - prefix[left]
                    )
                    right_sum = (
                        prefix[right + 1] - prefix[next_mid + 1]
                    )

                    if left_sum <= right_sum:
                        boundary += 1
                    else:
                        break

                # 왼쪽 부분을 남길 수 있는 모든 분할점 처리
                if boundary >= left:
                    dp[left][right] = best_left[left][boundary]

                # 오른쪽 부분을 남길 수 있는 최초 위치 계산
                if boundary >= left:
                    left_sum = prefix[boundary + 1] - prefix[left]
                    right_sum = prefix[right + 1] - prefix[boundary + 1]

                    if left_sum == right_sum:
                        first_right = boundary + 1
                    else:
                        first_right = boundary + 2
                else:
                    first_right = left + 1

                if first_right <= right:
                    dp[left][right] = max(
                        dp[left][right],
                        best_right[first_right][right]
                    )

                interval_sum = prefix[right + 1] - prefix[left]

                best_left[left][right] = max(
                    best_left[left][right - 1],
                    dp[left][right] + interval_sum
                )

                best_right[left][right] = max(
                    best_right[left + 1][right],
                    dp[left][right] + interval_sum
                )

        return dp[0][n - 1]
    '''
    구간 경계 단조성, Monotonous를 활용한 DP
    1. dp[i][j] = i~j 구간에서 얻을 수 있는 최대 점수
    2. dp[i][j] = max(dp[i][k] + left_sum, dp[k+1][j] + right_sum) for k in range(i, j)
    3. left_sum = prefix_sum[k+1] - prefix_sum[i]
    4. right_sum = prefix_sum[j+1] - prefix_sum[k+1]
    5. left_sum < right_sum -> dp[i][j] = dp[i][k] + left_sum
    6. left_sum > right_sum -> dp[i][j] = dp[k+1][j] + right_sum
    7. left_sum == right_sum -> dp[i][j] = max(dp[i][k] + left_sum, dp[k+1][j] + right_sum)
    8. dp[i][j] = max(dp[i][j], dp[i][k] + left_sum, dp[k+1][j] + right_sum) for k in range(i, j)
    9. dp[i][j] = max(dp[i][j], dp[i][k] + left_sum, dp[k+1][j] + right_sum) for k in range(i, j)
    '''


    '''
    Was Wrong: 
        
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                total_sum = prefix_sum[right + 1] - prefix_sum[left]
                for mid in range(left, right):
                    left_sum = prefix_sum[mid + 1] - prefix_sum[left]
                    right_sum = total_sum - left_sum
                    if left_sum < right_sum:
                        dp[left][right] = max(dp[left][right], dp[left][mid] + left_sum)
                    elif left_sum > right_sum:
                        dp[left][right] = max(dp[left][right], dp[mid + 1][right] + right_sum)
                    else:
                        dp[left][right] = max(dp[left][right], dp[left][mid] + left_sum, dp[mid + 1][right] + right_sum)

        return dp[0][n - 1]
    '''    