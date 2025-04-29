myList=[]


# for items in myList:
#     print(items)

def showList(list:list):
    index=0
    while index < len(list):
        print(list[index])
        index +=1

def enqueue(list1:list,data):
    list1[len(list1)-1]=data
    # index=0
    # while index < len(list1):
    #     if index==len(list1)-1:
    #         list1[index]=data
    #     index+=1

def dequeue(listname: list):
    temp = listname[len(listname)-1]
    listname[len(listname)-1]=None
    print(temp)

# myList.append("Nigger")
# print("1")
# showList(myList)
# enqueue(myList,"Negro")
# print("2")
# showList(myList)
# # print("Dequeued")
# # dequeue(myList)
# print("3")
# showList(myList)





class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty! Cannot pop.")
            return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def size(self):
        return len(self.items)


s = Stack()
s.push(1)
s.push(2)
s.push(3)

print(s.pop()) 
print(s.pop()) 
print(s.pop()) 
print(s.pop()) 