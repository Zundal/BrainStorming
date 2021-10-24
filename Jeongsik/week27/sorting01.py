# limit = int(input())

# inputList = []
# for x in range(limit):
#     inputList.append(int(input()))
    
# safeCnt = 0
# def half(iList):    
#     num=len(iList)/2
#     safeCnt += 1
#     if safeCnt == 5:
#         return 1
#     return half(num)

# print(half(inputList))

# 배열을 나누는 함수
# def splitArray(array):
#     if len(array) <= 1:
#         return array
    
#     length = len(array)//2
    
#     array = array[length:]
#     print(array)
#     # array[:length]
#     # print(array)
    
#     return splitArray(array)

# # 가장 작은 단위로 나뉠때 돌아감
# def sortingArray(listA, listB):
#     innerStack = []
#     if listA[0]<listB[0]:
#         innerStack.append(listA[0])
#         innerStack.append(listB[0])
#     else :
#         innerStack.append(listB[0])
#         innerStack.append(listA[0])
#     return innerStack

# splitArray(inputList)
# print(splitArray(inputList))

def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    
    mid = len(unsorted_list)//2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]
    
    left1 = merge_sort(left)
    right1 = merge_sort(right)
    
    return merge(left1, right1)

def merge(left, right):
    print(left, right)
    i = 0
    j = 0
    sorted_list = []
    
    while (i<len(left)) & (j<len(right)):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i+=1
        else :
            sorted_list.append(right[j])
            j+=1
            
    while (i < len(left)):
        sorted_list.append(left[i])
        i+=1
        
    while (j < len(right)):
        sorted_list.append(right[j])
        j+=1
        
    return sorted_list
print(merge_sort([7,4,6,2,1]))