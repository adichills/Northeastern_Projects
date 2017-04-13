alist = [[2, 3], [3, 1], [1, 2]]
def sortByLine( aList, k ,e):
    counter = [0] * ( k + 1 )
    for i in aList:
      counter[i[e]] += 1
    # print counter
    for i in xrange(1,k):
        counter[i] = counter[i] + counter[i-1]
    # print counter
    output = [None for x in alist]
    for i in xrange(len(alist)-1,-1,-1):
        # print counter[alist[i]]
        # print i
        output[counter[alist[i][e]]-1] = alist[i]
        counter[alist[i][e]] -= 1
    return output



def countingsort( aList, k ):
    counter = [0] * ( k + 1 )
    for i in aList:
      counter[i] += 1

    for i in xrange(1,k):
        counter[i] = counter[i] + counter[i-1]

    output = [None for x in alist]

    for i in xrange(len(alist)-1,-1,-1):
        # print counter[alist[i]]
        # print i
        output[counter[alist[i]]-1] = alist[i]
        counter[alist[i]] -= 1
    return output
    # ndx = 0;
    # for i in range( len( counter ) ):
    #   while 0 < counter[i]:
    #     aList[ndx] = i
    #     ndx += 1
    #     counter[i] -= 1


#alist = [[2, 3], [3, 1], [1, 2]]
#alist = [[2, 0], [3, 1], [5, 10], [4, 8]]
#alist = [[1, 4], [2, 2], [3, 3], [4, 1]]
alist = [[1, 5], [3, 4], [5, 1], [2, 6]]
sA = sortByLine(alist,11,0)
sB = sortByLine(alist,11,1)

count = 0
print sA
print sB


# def mergeSort(arr,low,high):
#     count = 0
#     if low <=high:
#         mid = low + (high - low) / 2
#         count += mergeSort(arr,low,mid)
#         count += mergeSort(arr,mid+1,high)
#         count += merge(arr,low,mid,high)
#     return count
#
# def merge(arr,low,mid,high):
#     left = low
#     right = mid+1
#     while left<=mid and right <=high:
#         if a[left] <= a[right]:
#

def merge(lefthalf,righthalf,alist):
    i = 0
    j = 0
    k = 0
    count = 0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            alist[k] = lefthalf[i]
            i = i + 1
        else:
            count += len(lefthalf) -i
            alist[k] = righthalf[j]
            j = j + 1
        k = k + 1

    while i < len(lefthalf):
        alist[k] = lefthalf[i]
        i = i + 1
        k = k + 1

    while j < len(righthalf):
        alist[k] = righthalf[j]
        j = j + 1
        k = k + 1
    return count

def mergeSort(alist):
    # print("Splitting ",alist)
    count = 0
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        count+=mergeSort(lefthalf)
        count+=mergeSort(righthalf)
        count+=merge(lefthalf,righthalf,alist)

    return count
    # print("Merging ",alist)

alist = [1, 1, 1 ,2 ,2]
count = mergeSort(alist)
print count
print(alist)


# def binary_search(sB,key):
#     low = 0
#     high = len(sB)-1
#     while (low<=high):
#         mid = low + (high - low)/2
#         #print mid,low,high
#         if sB[mid][1] == key:
#             return mid
#         elif key < sB[mid][1]:
#             high = mid-1
#         else:
#             low = mid+1
# #print binary_search(sB,1)
#
# def compute_count(sB,index,line):
#     i = index+1
#     count = 0
#     while(i<len(sB)):
#         if sB[i][0] < line[0] and sB[i][1] > line[1]:
#             count+=1
#         i+=1
#     return count
#
# i = 0
# count = 0
# while (i<len(sA)):
#     key = sA[i][1]
#     index = binary_search(sB,key)
#
#     count+=compute_count(sB,index,sA[i])
#     i=i+1
#
# print count

# for i in xrange(len(sA)-1,-1,-1):
#     for j in xrange(len(sB)-1,-1,-1):
#         if sA[i][1] < sB[j][1] and sA[i][0] > sB[j][0]:
#             count+=1
#         if sA[i][0] == sB[j][0] and sA[i][1] == sA[j][1]:
#             break
# print count


# alist = [3,4,5,2,0,7,5]
# alist = [2,3,1]
# print countingsort(alist,4)
