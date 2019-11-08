N = int(input())

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]


swpCnt = 0
for i in range(N-1):
    score = 0
    if A[i+1] > A[i]:
        score += 1
    if A[i+1] > B[i]:
        score += 1
    if B[i+1] > A[i]:
        score += 1
    if B[i+1] > B[i]:
        score += 1
    if score < 2:
        print(-1) # cannot solve
        exit()

    if A[i+1] <= A[i] or B[i+1] <= B[i]:
        tmp = A[i+1]
        A[i+1] = B[i+1]
        B[i+1] = tmp
        swpCnt += 1

print(min(swpCnt, N-swpCnt))

# Extra test cases
# Sample Input:
# 4
# 1 3 4 9
# 2 3 5 10
# 4
# 1 4 4 9
# 2 3 5 10
# 5
# 2 1 6 5 8
# 0 3 4 7 9
# 7
# 8 9 10 11 9 10 15
# 3 4 7 8 12 15 16
# 7
# 8 9 10 11 9 10 15
# 3 4 7 8 12 15 10
# 7
# 1 1 3 4 5 6 8
# 0 2 4 5 6 7 7
# Sample Output:
# 0
# 1
# 2
# 3
# -1
# 2