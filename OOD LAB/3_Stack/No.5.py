class Stack:
    def __init__(self,list = None) :
        if list is None:
            self.items = []
        else : 
            self.items = list
    
    def __str__(self) :
        return str(self.items)

    def push(self, i) :
        return self.items.append(i)

    def pop(self) :
            return self.items.pop()
    
    def isEmpty(self):
        return self.items == []
    
    def size(self) :
        return len(self.items)

    def val(self):
        return self.items

print("******** Parking Lot ********")
m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
m,n = int(m),int(n)

suntoiA = Stack()
suntoiB = Stack()

if len(s) == 1 and s[0] == '0':
    s=[]
else :
    s = s.split(',')
    for i in s:
        i = int(i)
        suntoiA.push(i)

if(o == "arrive"):
    if(suntoiA.size() >= m):
        print("car",n,"cannot arrive : Soi Full")
    elif(n in suntoiA.val()):
        print("car",n,"already in soi")
    else:
        suntoiA.push(n)
        print("car",n,"arrive! : Add Car",n)

elif(o == "depart"):
    if(suntoiA.isEmpty() is True):
        print("car",n,"cannot depart : Soi Empty")
    elif(n not in suntoiA.val()):
        print("car",n,"cannot depart : Dont Have Car",n)
    else:
        Dcar =- 1
        while(Dcar != n):
            if suntoiA.isEmpty() is False:
                Dcar = suntoiA.pop()
                if(Dcar == n):
                    print("car",n,"depart ! : Car",n,"was remove")
                    while(suntoiB.isEmpty() is False):
                        suntoiA.push(suntoiB.pop())
                else:
                    suntoiB.push(Dcar)

print(suntoiA)

