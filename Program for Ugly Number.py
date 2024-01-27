def is_ugly(N):
    while N % 2 == 0:
        N = N // 2
    if N == 1:
        return True
    while N % 3 == 0:
        N = N // 3
    if N == 1:
        return True
    while N % 5 == 0:
        N = N // 5
    if N == 1:
        return True
    return False

input_number = int(input())
output = is_ugly(input_number)
print("{} is an ugly number:{}".format(input_number, output))
