# 최소, 최대
# 문제
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

# 출력
# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

# 예제 입력 1 
# 5
# 20 10 35 30 7

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

a.sort()

print(a[0], a[-1])
#############################################################
# n = int(input())
# a = list(map(int,input().split()))

# res1, res2 = a[0], a[0]

# for x in a[1:]:
#     if x < res1:
#         res1 = x
        
#     if res2 < x:
#         res2 = x
 
# print(res1, res2)
#############################################################
# count = int(input())
# num_list = list(map(int, input().split()))

# print(min(num_list), max(num_list))