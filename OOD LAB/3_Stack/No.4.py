class Stack:
    def __init__(self,list = None) :
        if list is None:
            self.items = []
        else : 
            self.items = list

    def push(self, i) :
        return self.items.append(i)

    def pop(self) :
            return self.items.pop()
    
    def isEmpty(self):
        return self.items == []
    
    def size(self) :
        return len(self.items)


class StackCalc():
    def __init__(self):
        self.result = 0
    def run(self,inp):
        arg = inp.split()
        self.result = Calculator(arg)
        if self.result == '' :
            self.result = 0
    def getValue(self):
        return self.result


def Calculator(stack):
    S = Stack()
    for i in stack:
        if i == '+':
            x = S.pop()
            y = S.pop()
            result = x+y
            S.push(result)
        elif i == '-':
            x = S.pop()
            y = S.pop()
            result = x-y
            S.push(result)
        elif i == '*':
            x = S.pop()
            y = S.pop()
            result = x*y
            S.push(result)
        elif i == '/':
            x = S.pop()
            y = S.pop()
            result = x/y
            S.push(result)
        elif i == "DUP":
            x = S.pop()
            S.push(x)
            S.push(x)   
        elif i == "POP":
            S.pop()
        elif i == "PSH":
            S.push()
        elif i.isalpha():
            return "Invalid instruction: "+i
        else:
            S.push(int(i))
    if S.isEmpty() is False:
        return int(S.pop())
    else:
        return 0
            


print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())
