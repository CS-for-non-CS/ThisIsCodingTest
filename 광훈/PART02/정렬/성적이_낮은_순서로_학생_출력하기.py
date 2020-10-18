"""
2
홍길동 95
이순신 77
"""

N = int(input())
students = [input().split() for _ in range(N)]

for student in sorted(students, key=lambda x: int(x[1])):
    print(student[0], end=' ')
