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
    
    def __str__(self):
        return str(self.root)

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
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def Order(self,root,data):
        if root != None:
            self.Order(root.left,data)
            if int(root.data) < int(data):
                print(root.data,end=" ")
            self.Order(root.right,data)

    def Min(self,root):
        root = self.root
        while(root.left is not None):
            root= root.left
        return root.data
    
    def PrintOrder(self,root,item):
        if self.Min(root) < int(item):
            self.Order(self.root,item)
        else: print("Not have")

        


T = BST()
inp,item = input('Enter Input : ').split("|")
inp = [int(i) for i in inp.split()]
for i in inp:
    root = T.insert(i)
    
T.printTree(root)
print("--------------------------------------------------")
print("Below",item,":",end=" ")
T.PrintOrder(T.root,item)