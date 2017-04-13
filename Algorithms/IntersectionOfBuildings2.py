# Enter your code here. Read input from STDIN. Print output to STDOUT
def sortByLine( alist, k ,e):
    counter = [0] * ( k + 1 )
    for i in alist:
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

n = int(input())
lineList = []
max_val = -1
for i in xrange(n):
    line = map(int,raw_input().strip().split(' '))
    lineList.append(line)
    m = max(line)
    if m > max_val:
        max_val = m
sA = sortByLine(lineList,max_val+1,0)[::-1]
sB = sortByLine(lineList,max_val+1,1)

def binary_search(sB,key):
    low = 0
    high = len(sB)-1
    while (low<=high):
        mid = low + (high - low)/2
        #print mid,low,high
        if sB[mid][1] == key:
            return mid
        elif key < sB[mid][1]:
            high = mid-1
        else:
            low = mid+1
def compute_count(sB,index,line):
    i = index+1
    count = 0
    while(i<len(sB)):
        if sB[i][0] < line[0] and sB[i][1] > line[1]:
            count+=1
        i+=1
    return count
i = 0
count = 0
while (i<len(sA)):
    key = sA[i][1]
    index = binary_search(sB,key)

    count+=compute_count(sB,index,sA[i])
    i=i+1

print count

