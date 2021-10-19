N = int(input())

list = []

for i in range(0, N):
    ip = input().split()
    if ip[0] == "print":
        print(list)
    else:
        break
