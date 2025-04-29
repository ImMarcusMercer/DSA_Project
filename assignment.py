from collections import deque

queue= deque()


queue.append("1")
queue.append("2")
queue.append("3")
queue.append("4")
queue.append("5")


list1=[]
list1.append("1")
list1.append("2")
list1.append("3")
list1.append("4")
list1.append("5")


def showList(list):
    index=0
    while index < len(list):
        print("Index",index,":",list[index])
        index+=1

def dequeue(list: list):
    # dequeuevalue=list.pop(0)

    #O(n)
    dequeuevalue=None
    index=0
    while index < len(list):
        if list[index] != None:
            dequeuevalue= list[index]
            list[index]= None
            return dequeuevalue
        index+=1
    return dequeuevalue

def enqueue(list1: list, data):
    #O(n)
    index=0
    while index < len(list1):
        if list1[index] == None:
            list1[index]= data
            break
        index+=1 

if __name__=="__main__":
    showList(list1)
    print("Removed:",dequeue(list1))
    print("Removed:",dequeue(list1))
    print("Removed:",dequeue(list1))
    print("Removed:",dequeue(list1))
    print("Removed:",dequeue(list1))
    showList(list1)
    enqueue(list1, "Another")
    enqueue(list1, "Another 1")
    enqueue(list1, "Another 2")
    enqueue(list1, "Another 3")
    enqueue(list1, "Another 4")

    showList(list1)


    # showList(queue)
    # queue.popleft()
    # print()
    # showList(queue)
    # showList(queue)
    # queue.appendleft("Insert")
    # queue.pop()

    # showList(queue)