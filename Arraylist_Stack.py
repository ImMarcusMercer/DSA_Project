class Arraylist:
    def __init__(self):
        self.data=[]
        self.size=0
    
    def add(self, data):
        self.data.append(data)
        self.size+=1

    def remove(self):
        if self.size <= 0:
            print("Is Empty")
            return 
        popped =self.data.pop()
        self.size-=1
        return popped
    

    def __str__(self):
        String1= "Arraylist Stack:\nSize: "
        String1+=str(self.size)+"\n"
        if self.size==0:
            String1+="Empty"
            return String1
        for items in self.data:
            String1+="| "+items
        return String1


class Stack:
    def __init__(self, capacity=10):
        self.list= Arraylist()
        self.capacity=capacity

    def push(self, data):
        if self.list.size < self.capacity:
            self.list.add(data)
        else:
            print("Failed to push, Stack is full!")

    def pop(self):
        if self.capacity > 0:
            popped=self.list.remove()
            print("Removed: ", popped)

    def peek(self):
        print("Top Element: ",self.list.data[self.list.size-1])

    def is_empty(self):
        pass

    def showStack(self):
        print(self.list)

if __name__=="__main__":

    stack= Stack()
    stack.push("value 1")
    stack.push("value 2")
    stack.push("value 3")
    stack.push("value 4")
    stack.push("value 5")
    stack.push("value 6")
    stack.push("value 7")
    stack.push("value 8")
    stack.push("value 9")
    stack.push("value 10")
    
    stack.showStack()
    stack.push("value 1")
    stack.push("value 2")
    stack.push("value 3")
    stack.push("value 4")
    stack.push("value 5")
    stack.peek()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.showStack()