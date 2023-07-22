class stack:
    def __init__(self):
        self.items=[]
                                            
    def is_empty(self):                        
        return self.items == []
    
    def push(self,data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def display(self):
        return self.items

s=stack()
while True:
    print('push <value>')
    print('pop')
    print('peek')
    print('display')
    print('quit')
    do=input('choose your operation?').split()
    operation=do[0].strip().lower()
    if operation=='push':
        s.push(int(do[1]))
    elif operation=='pop':
        if s.is_empty():
            print('stack is empty')
        else:
            print('the pop value is',s.pop())
    elif operation=='peek':
        print('peek valueis:',s.peek())
    elif operation=='display':
        print('the stack is:',s.display())
    elif operation=='quit':
        break


    
    