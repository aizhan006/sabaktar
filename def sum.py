def sum (a,b):
    return a+b
def minuse(a,b):
    return a-b
def  multiple (a,b):
    return a*b
def divide (a,b):
    return a/b
a,b=map(int,input().split())
s=input()
if s=="+":
    print(minuse(a,b))
elif s=="-":
    print(minuse(a,b))
elif s=="*":
    print(multiple(a,b))
else:
    print(divide(a,b))