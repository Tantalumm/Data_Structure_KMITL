class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class Stack:
    def __init__(self) -> None:
        self.items = []

    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.size)
    def push(self,data):
        return self.items.append(data)
    def pop(self):
        return self.items.pop(0)


class Binarysearchtree:
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
    
    def pre_order(self, node):
        if node :
            s = str(node.data) + ' '\
                + self.pre_order(node.left)\
                    + self.pre_order(node.right)

        else : return ''

        return s

    def in_order(self, node):
        if node:
            s = self.in_order(node.left)\
                + str(node.data) + ' '\
                    + self.in_order(node.right)
        else : return ''

        return s

    def post_order(self, node):
        if node:
            s = self.post_order(node.left)\
                + self.post_order(node.right)\
                    + str(node.data) + ' '
        else : return ''

        return s

    def BFS(self): 
        q = Stack()
        q.push(self.root)
        s = "Breadth : "
        while not q.isEmpty():
            node = q.pop()
            s += str(node.data) + ' '
            if node.left is not None:
                q.push(node.left)
            if node.right is not None:
                q.push(node.right)
        return s

T = Binarysearchtree()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
    
print('Preorder :',T.pre_order(root))
print('Inorder :',T.in_order(root))
print('Postorder :',T.post_order(root))
print(T.BFS())