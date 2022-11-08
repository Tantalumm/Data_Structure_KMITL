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

    def insert(self, data):
        if self.root is None :
            self.root = Node(data)

        else :
            now = self.root
            while True:
                if data > now.data :
                    if now.right is None:
                        now.right = Node(data)
                        break
                    else:
                        now = now.right
                else :
                    if now.left is None:
                        now.left = Node(data)
                        break
                    else:
                        now = now.left
        return self.root

    def printRoot(self, node, level = 0):
        if node :
            self.printRoot(node.right, level + 1)
            print('     ' * level, node)
            self.printRoot(node.left, level + 1)
    
    def closestValue(self,root,value):
        if root :
            diff = abs(value - root.data)
            ans = 0
            List.append(root)
            while len(List) > 0:
                temp = List[0]
                List.pop(0)
                if abs(value - temp.data) < diff:
                    diff = abs(value - temp.data)
                    ans = temp.data
                elif abs(value - temp.data) == diff:
                    if ans<temp.data:
                        ans = temp.data
                if temp.left :
                     List.append(temp.left)
                if temp.right :
                     List.append(temp.right)
        return ans

T = BST()
List = []
Diff = 0
V,Cv = input("Enter Input : ").split("/")
Cv = int(Cv)
tree = [int(i) for i in V.split()]
for i in tree:
    if abs(Cv - i) <= abs(Diff):
        Diff = Cv - i
    root = T.insert(i)
    T.printRoot(T.root)
    print('--------------------------------------------------')

print("Closest value of" , Cv ,":" , T.closestValue(T.root,Cv))
