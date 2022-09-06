input = int(input("Enter Input : "))
x = input-(input -1)

for i in range(0,(6 * x)+2*(input-1),1):
    for j in range(i,input+1,1):
        print(".",end='')
    for j in range(0,i+1,1):
        if(j>=input+2) : break
        if(i>=input+3 and i < input+input+3) : 
            print("#",end='')
            for k in range(input):
                print("+",end='')
            print("#",end='')
            break
        print("#",end='')
    for j in range((input*x)+3,i+1,-1):
        if(i==input+1):break
        print("+",end='')
        if(i>=1 and i<=input) :
            for k in range(input):
                print("#",end='')
            print("+",end='') 
            break
    if(i==input+1):
        for j in range(0,input+(2*x),1):
            print("+",end='')
    elif (i > input+1):
        for j in range((6*x)+2*(input-1),i,-1):
            print("+",end='')
        for j in range(input+(2*x),i,1):
            print(".",end='')
    print()
            