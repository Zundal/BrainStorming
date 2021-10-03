# a,b,c = map(int, input().split())
# a,b,c = map(int, input().split())
# a,b,c = map(int, input().split())
# a,b,c = map(int, input().split())
# a,b,c = map(int, input().split())
# a,b,c = map(int, input().split())

a, b, c = 1, 1, 1
# a, b, c = 2 2 2
# a, b, c = 10 4 6
# a, b, c = 50 50 50
# a, b, c = -1 7 18
# a, b, c = -1 -1 -1

# 1. 로직 실행
# 2. maximum recursion depth exceeded in comparison 에러발생
# 3. 파이썬 재귀호출 제한 횟수 에러
# 4. 메모이 제이션으로 저장값 위치를 넣어주고 풀어야 한다.


def w(a, b, c):
    if a<=0 or b <=0 or c<=0 :
        return 1
    
    if a>20 or b<20 or c>20 :
        return w(20, 20, 20)
    
    if a<b and b<c :
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    
print(w(a, b, c))