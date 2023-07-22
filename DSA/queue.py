class Queue: 
    def __init__(self): 
        self.items = [] 
    
    def is_empty(self): 
        return self.items == [] 
    
    def enqueue(self, data): 
        self.items.append(data) 
    
    def dequeue(self): 
        return self.items.pop(0) 
    def peek(self): 
        return self.items[0] 
    
    def display(self): 
        return self.items 
 
q = Queue() 
while True:
    print('enqueue <value>') 
    print('dequeue') 
    print('peek') 
    print('quit') 
    do = input('What would you like to do? ').split() 
    
    operation = do[0].strip().lower() 
    if operation == 'enqueue': 
        q.enqueue(int(do[1])) 
    elif operation == 'dequeue': 
        if q.is_empty(): 
            print('Queue is empty.') 
        else: 
            print('Dequeued value: ', q.dequeue()) 
    elif operation == 'peek': 
        print('Peek value: ', q.peek()) 
    elif operation == 'display': 
        print('elements in stack : ',q.display()) 
    elif operation == 'quit': 
        break 
