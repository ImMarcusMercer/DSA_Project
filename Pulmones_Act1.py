class Node:
    def __init__(self, data= None):
        self.data= data
        self.next= None

class LinkedList:    
    """Singly Linked List"""
    def __init__(self):
        self.head= Node()

    def add(self, data):
        new_data = Node(data)
        if self.head is None:
            self.head= new_data
            return
        current= self.head
        while current.next:
            current=current.next
        current.next= new_data

class Stack:
    """Stack implemented using LinkedList"""
    def __init__(self, capacity=10):
        self.size= 0
        self.capacity=capacity
        self.LList= LinkedList()

    def push(self, data):
        """Add data to Stack w/ LinkedList"""
        l=self.LList
        l.add(data)
        self.size+=1

    def showStack(self):
        """Show List in a horizontal view"""
        if self.size<=0:
            print("No elements in stack!")
            return
        l=self.LList
        current= l.head.next
        while current:
            print("| ",current.data, end=" ")
            current=current.next
        print()

    def pop(self):
        """Remove the last item"""
        if self.size<=0:
            print("Stack is empty!")
            return
        l= self.LList
        curr= l.head
        while curr.next:
            if curr.next.next==None:
                curr=curr
                toPop=curr.next
                break
            curr= curr.next
        curr.next= None
        print("Removed: ", toPop.data)
        self.size-=1

    def peek(self):
        last=None
        curr= self.head.next
        while curr.next:
            curr=curr.next
        last= curr
        # print("Top: ",last.data)
        return last
    
class Arraylist:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, data):
        #Manually
        # index=0
        # while index < len(self.stack):
        #     if self.stack[index] is None:
        #         self.stack[index] = data
        #     index+=1
        # self.size+=1

        #Using built in functions
        self.stack.append(data)
        self.size+=1

    def showStack(self):
        if self.size==0:
            print("Stack is empty!")
            return
        index=0
        last= -len(self.stack)
        while index > last:
            print("|"+self.stack[index-1]+"|")
            index-=1
        print("-"*9)

    def getSize(self):
        print("Stack size: ",self.size,"\n")

    def pop(self):
        if self.size<=0:
            print("Stack is empty")
            return
        popped=self.stack.pop()
        self.size-=1
        print("Popped: ", popped)


    



if __name__=="__main__":
    print("Linked List Stack")
    stack1= Stack()
    stack1.push("Value 1")
    stack1.push("Value 2")
    stack1.push("Value 3")
    stack1.push("Value 4")
    stack1.push("Value 5")
    stack1.showStack()
    stack1.pop()
    stack1.pop()
    stack1.pop()
    stack1.pop()
    stack1.pop()
    stack1.pop()
    stack1.pop()
    stack1.pop()
    stack1.showStack()
    stack1.push("Value 1")
    stack1.push("Value 2")
    stack1.push("Value 3")
    stack1.push("Value 4")
    stack1.push("Value 5")
    stack1.showStack()
    # print(list1.head.next.data)



    #Arraylist
    print("\nAraylist Stacks")
    stack2= Arraylist()
    stack2.push("Value 1")
    stack2.push("Value 2")
    stack2.push("Value 3")
    stack2.push("Value 4")
    stack2.push("Value 5")

    stack2.showStack()
    stack2.getSize()
    stack2.pop()
    stack2.pop()
    stack2.pop()
    stack2.showStack()
    stack2.getSize()
    stack2.pop()
    stack2.pop()
    stack2.pop()
    stack2.pop()
    stack2.pop()
    stack2.pop()


#Pulmones, Janmarc D.
#BSIT 2C
#Friday 1-4