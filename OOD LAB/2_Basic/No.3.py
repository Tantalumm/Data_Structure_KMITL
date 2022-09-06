print("*** Odd Even ***")
def odd_even(type,data,mode):
    result = []
    if(type == 'S'):
        x = data
        if(mode == "Odd"):
            for n in x:
                if(x.index(n) % 2 == 0):
                    result = print('%s' % n,end='')
        elif(mode == "Even"):
            for n in x:
                if(x.index(n) % 2 != 0):
                    result = print('%s' % n,end='')
        return result
             
    elif(type == 'L'):
        y = list(str(data).split(' '))
        if(mode == "Odd"):
            t = 0
            for  i in range(t, len(y), 2):
                result.append(y[i])
        elif(mode == "Even"):
            t = 1
            for i in range(t, len(y), 2):
                result.append(y[i])
        return print(result)
        
        
        
iptype,ipdata,ipmode = str(input("Enter Input : ")).split(",")

odd_even(iptype,ipdata,ipmode)
