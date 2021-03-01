n = int(input())
space = n-1
star = 1
for i in range(n):
    print(" "*space,end="")
    print("*"*star)
    star+=2
    space-=1