# 앞쪽의 숫자의 부분 수열의 길이에 1을 더한 값이 자신의 부분 수열

N = int(input())
numbers = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if numbers[j] > numbers[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))