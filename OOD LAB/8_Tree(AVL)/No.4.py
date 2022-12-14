class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def knightArrange(self,rank,data):
        if self.root == None :
            self.root = Node(data)
        else :
            now = self.root

            cheif = [rank]
            
            while cheif[0] > 2 :
                cheif.insert(0,int((cheif[0]-1)/2 if cheif[0]%2==1 else (cheif[0]-2)/2))
            
            for c in cheif[:-1] :
                if c % 2 == 1 :
                    now = now.left
                else :
                    now = now.right
            
            if cheif[-1] % 2 == 1 :
                now.left = Node(data)
            else :
                now.right = Node(data)

        return self.root

    def SumofPower(self,node) :
        if node == None :
            return 0
        return self.SumofPower(node.left) + node.data + self.SumofPower(node.right)

    def search(self,rank) :
        if rank == 0 :
            return self.root
        else :
            now = self.root
            cheif = [rank]
            
            while cheif[0] > 2 :
                cheif.insert(0,int((cheif[0]-1)/2 if cheif[0]%2==1 else (cheif[0]-2)/2))

        for c in cheif :
                if c % 2 == 1 :
                    now = now.left
                else :
                    now = now.right

        return now 

    def compare(self,f1,f2) :
        if self.SumofPower(self.search(f1)) > self.SumofPower(self.search(f2)) :
            print(f1,">",f2,sep="")
        elif self.SumofPower(self.search(f1)) == self.SumofPower(self.search(f2)) :
            print(f1,"=",f2,sep="")
        else :
            print(f1,"<",f2,sep="")

Power = BST()
Strength,Rank = input('Enter Input : ').split("/")

Strength = [int(i) for i in Strength.split()]
Rank = [ list( int(i) for i in x.split()) for x in Rank.split(",")]

for i in range(len(Strength)):
    root = Power.knightArrange(i,Strength[i])

print(Power.SumofPower(Power.root))

for i in Rank :
    Power.compare(i[0],i[1])