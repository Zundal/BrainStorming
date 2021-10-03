# 앞쪽의 숫자의 부분 수열의 길이에 1을 더한 값이 자신의 부분 수열

cnt = int(input())
inputNum = list(map(int, input().split()))

arr = [1] * cnt

for i in range(1, cnt):
    for j in range(i):
        if inputNum[j] > inputNum[i]:
            arr[i] = max(arr[i], arr[j] + 1)

print(max(arr))
