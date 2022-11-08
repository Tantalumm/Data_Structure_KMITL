def Fac(n):
    if n <= 1:
        return 1
    else :
        return Fac(n-1) * n

num = input("Enter Number : ")
print(str(num)+"!","=",Fac(int(num)))