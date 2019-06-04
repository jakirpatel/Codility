# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(N):
    # write your code in Python 3.6
    result = 0
    li = [int(i) for i in str(bin(N))[2:]]
    count = 0
    a = len(li)
    for i in range(a):
        count = 0
        if not li[i]==1:
            continue
        for j in range(i+1,a):
            if li[j]==0:
                count += 1
            if li[j]==1:
                i=j
                result = max(result, count)
                break
    return result
    pass