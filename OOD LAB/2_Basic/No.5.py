class gameword :
        def __init__(self,command = None):
                if(command == None):
                        self.items = []
                else:
                        self.items = command
             
        def __str__(self):
               return str(command)

        def push(self, i):
                self.items.append(i)

                               
print("*** TorKham HanSaa ***")
command = list(input("Enter Input : ").split(","))

Gword = gameword()

t = None

for i in command:
        Coms = i.split(' ')[0]
        
        if Coms == 'R':
                print("game restarted")
                Gword.items = []
                t = None

        elif Coms == 'P':
                word = i.split()[1]
                print("'"+ word + "'" ,'-> ',end ='')
                F = word[:2].lower()
                if F == t or t == None:
                        Gword.items.append(word)
                        t = word[-2:].lower()
                        print(Gword.items)
                else:
                        print("game over") 
                        break

        elif Coms == 'X':
                break

        else : 
                print("'"+i+"'"+" is Invalid Input !!!")
                break






                