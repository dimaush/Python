print('������� ������� ���� ����� ������:')
X = list(map(int, input().split()))
print('������� ���������� ����� �����:')
A = list(map(int, input().split()))
for i in range (A[1] - 1):
    print('.' * X[0])
print('.' * (A[0] - 1), end = '')
print('a' * (A[2] - A[0] + 1), end = '')
print('.' * (X[0] - A[2]))
for i in range (A[3] - A[1] - 1):
    print('.' * (A[0] - 1), end = '')
    print('a', end = '')
    print('.' * (A[2] - A[0] - 1), end = '')
    print('a', end = '')
    print('.' * (X[0] - A[2]))
print('.' * (A[0] - 1), end = '')
print('a' * (A[2] - A[0] + 1), end = '')
print('.' * (X[0] - A[2]))
for i in range (X[1] - A[3]):
    print('.' * X[0])