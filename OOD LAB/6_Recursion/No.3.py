def pow(m,n):
    if m == 0:
        return 0
    elif n == 0:
        return 1
    else :
        return (pow(m,n-1)*m)


a,b = input("Enter Input a b : ").split()

print(pow(int(a),int(b)))
