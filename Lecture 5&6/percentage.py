n = int(input())

while n < 2 or n > 10:
    print("Unvalid")
    n = int(input())

d = {}
for i in range(0, n):
    invalid_grade = 3

    while invalid_grade != 0:
        details = input()
        details = details.split(" ")
