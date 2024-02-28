# program to print triangle
# Date : 24/02/2024
# Name : David Musila

n = int(input("enter the number of rows:"))

for i in range(n):
    for j in range(n - i -1):
        print(" ",end="")
    for j in range(i + 1):
        print("*",end=" ")
    print()        