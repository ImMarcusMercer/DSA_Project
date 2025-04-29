class Node:
    def __init__(self, data=None):
        self.data = data
        self.next= None

class SLL:
    def __init__(self):
        self.head=Node()
        self.size=0

    def add(self, data):
        new_data = Node(data)
        if self.head is None:
            self.head= new_data
            return
        current= self.head
        while current.next:
            current=current.next
        current.next= new_data
        self.size+=1

    def remove(self):
        if self.size<=0:
            print("Is empty!")
            return
        toPop= None
        curr=self.head
        while curr.next:
            if curr.next.next==None:
                curr=curr
                toPop=curr.next
                break
            curr= curr.next
        curr.next= None
        self.size-=1
        print("Removed: ",toPop.data)
        

    def __str__(self):
        str1="Linked List Stack"
        str1+="\nSize: "+str(self.size)+"\n"
        curr= self.head.next
        while curr:
            str1+="|"+curr.data
            curr=curr.next
        return str1

class Stack:
    def __init__(self, capacity=10):
        """Stack implemented with SLL, default size= 10"""
        self.list=SLL()
        self.capacity=capacity

    def pop(self):
        if self.list.size > 0:
            self.list.remove()
        else:
            print("Stack is already empty!")

    def push(self, data):
        if self.list.size < self.capacity:
            self.list.add(data)
        else:
            print("Failed to push, Stack is full!")

    def peek(self):
        if self.list.size<=0:
            print("Stack is empty!")
            return
        last=None
        curr= self.list.head.next
        while curr.next:
            curr=curr.next
        last= curr
        print("Top element: ",last.data)

    def showList(self):
        print(self.list)

if __name__=="__main__":
    stack= Stack()
    stack.push("Name 1")
    stack.push("Name 2")
    stack.push("Name 3")
    stack.push("Name 4")
    stack.push("Name 5")
    stack.push("Name 6")
    stack.push("Name 7")
    stack.push("Name 8")
    stack.push("Name 9")
    stack.push("Name 10")
    stack.push("Name 1")
    stack.push("Name 2")
    stack.push("Name 3")
    stack.push("Name 4")
    stack.push("Name 5")
    stack.showList()
    stack.peek()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.showList()
    stack.peek()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.showList()