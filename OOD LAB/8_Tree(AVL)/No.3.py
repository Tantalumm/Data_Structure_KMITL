N,val = input("Enter Input : ").split('/')
N = int(N)
val = val.split()
val = list(map(int, val))
print(val)

if (N+1)//2 >= len(val) and N >= 3:

    while N > len(val):
        val.insert(0, -999)

    
    def cal(cur):
        if val[cur] != -999:
            return
        pos1 = 2*cur+1
        pos2 = 2*cur+2
        
        cal(pos1)
        cal(pos2)

        x = min(val[pos2], val[pos1])

        val[cur] = x
        val[pos1] -= x
        val[pos2] -= x

    cal(0)
    print(sum(val))

else:
    print("Incorrect Input")
