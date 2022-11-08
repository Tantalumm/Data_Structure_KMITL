class Node():
    def __init__(self, data, left= None, right = None):
        self.data = data
        self.right = right 
        self.left = left 
    
    def __str__(self):
        return str(self.data)

class BST():
    def __init__(self):
        self.root = None
    
    def insertPostfix(self, data):
        List = []
        for x in data:
            if x in '+-*/':
                op1 = List.pop(-1)
                op2 = List.pop(-1)
                List.append(Node(x, op1, op2))
            else:
                List.append(Node(x))
        self.root = List.pop()
        return self.root
    
    
    def printTree(self, node, level = 0):
        if node:
            self.printTree(node.left, level+1)
            print('     ' * level, node)
            self.printTree(node.right, level+1)
    
def Infix(node):
    if node:
        if node.left and node.right:
            print('(', end='')
        Infix(node.right)
        print(node, end='')
        Infix(node.left)
        if node.left and node.right:
            print(')', end='')

def Prefix(node):
    if node:
        print(node, end='')
        Prefix(node.right)
        Prefix(node.left)



T = BST()
inp = input("Enter Postfix : ")
root = T.insertPostfix(inp)
print("Tree : ");T.printTree(root, 0)
print('--------------------------------------------------')
print("Infix : ",end="");Infix(root);
print("\nPrefix : ",end="");Prefix(root);