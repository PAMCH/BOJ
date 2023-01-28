# N과 M (2)
# 문제
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.
# 입력
# 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

# 출력
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

# 예제 입력 1 
# 3 1
# 예제 출력 1 
# 1
# 2
# 3
# 예제 입력 2 
# 4 2
# 예제 출력 2 
# 1 2
# 1 3
# 1 4
# 2 3
# 2 4
# 3 4
# 예제 입력 3 
# 4 4
# 예제 출력 3 
# 1 2 3 4

# import sys
# import collections
# input = sys.stdin.readline
# sys.setrecursionlimit(100000)

# def f(i):
#     if len(s) == m:
#         print(*s)
#         return
#     for j in range(i, n + 1):
#         s.append(j)
#         f(j + 1)
#         s.pop()
# n, m = map(int, input().split())
# s = collections.deque()

# f(1)

import sys
import itertools

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(range(1, n + 1))

for x in itertools.combinations(a, m):
    print(*x)