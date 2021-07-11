'''
    An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, 
    and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] 
    (elements are shifted right by one index and 6 is moved to the first place).

    The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

    Write a function:

    class Solution { public int[] solution(int[] A, int K); }

    that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

    For example, given
        A = [3, 8, 9, 7, 6]
        K = 3

    the function should return [9, 7, 6, 3, 8]. Three rotations were made:
        [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
        [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
        [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]

    For another example, given
        A = [0, 0, 0]
        K = 1
    the function should return [0, 0, 0]

    Given
        A = [1, 2, 3, 4]
        K = 4
    the function should return [1, 2, 3, 4]

    Assume that:
        N and K are integers within the range [0..100];
        each element of array A is an integer within the range [−1,000..1,000].
'''

'''
    N개의 정수로 구성된 배열 A가 주어집니다. 어레이의 회전은 각 요소가 한 인덱스씩 오른쪽으로 이동함을 의미합니다. 
    어레이의 마지막 요소가 첫 번째 위치로 이동됩니다. 예를 들어 어레이 A = [3, 8, 9, 7, 6]의 회전은 [6, 3, 8, 9, 7]입니다. 
    (점수가 한 지수씩 오른쪽으로 이동되고 6이 1위로 이동됩니다.)

    목표는 어레이 AK회 회전입니다. 즉, A의 각 요소가 오른쪽 K회 회전합니다.

    함수 쓰기:

    클래스 솔루션 {public int[] 용액(int[] A, int K); }

    즉, N개의 정수와 정수 K로 구성된 배열 A가 주어진 경우 배열 A가 K번 회전합니다.

    예를 들어, 주어진
        A = [3, 8, 9, 7, 6]
        K = 3

    함수는 [9, 7, 6, 3, 8]을 반환해야 합니다. 다음 세 가지 회전이 이루어졌습니다.
        [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
        [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
        [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]

    또 다른 예로, 주어진
        A = [0, 0, 0]
        K = 1
    함수는 [0, 0, 0]을 반환해야 합니다.

    기븐
        A = [1, 2, 3, 4]
        K = 4
    함수는 [1, 2, 3, 4]를 반환해야 합니다.

    다음과 같이 가정합니다.
        N과 K는 [0..] 범위의 정수입니다.100];
        어레이 A의 각 요소는 [-1,000..1,000] 범위의 정수입니다.
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import deque
def solution(A, K):
    d_list = deque(A)
    for cycle in range(K):
        if d_list :
            d_list.appendleft(d_list.pop())
        else :
            d_list
    return list(d_list)

#solution([3, 8, 9, 7, 6],3)
#solution([0, 0, 0],1)
#print(solution([],4))
#print(solution([],0))