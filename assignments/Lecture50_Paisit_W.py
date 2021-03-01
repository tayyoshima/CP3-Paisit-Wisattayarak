def plusNumber(x,y):
    print(str(x)+" + "+str(y)+" = "+str(x+y))
def minusNumber(x,y):
    print(str(x)+" - "+str(y)+" = "+str(x-y))
def multiNumber(x,y):
    print(str(x)+" x "+str(y)+" = "+str(x*y))
def divNumber(x,y):
    print(str(x)+" / "+str(y)+" = "+str(int(x/y)))

x = int(input())
y = int(input())
plusNumber(x,y)
minusNumber(x,y)
multiNumber(x,y)
divNumber(x,y)