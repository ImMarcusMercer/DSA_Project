class ArrayList:
    def __init__(self):
        self.data=[]
        self.size= 0

    def add(self, data):
        """Add item to the list"""
        pass
    def remove(self):
        """Remove item from the list"""
        pass
    
    def __str__(self):
        """Show the list"""
        return None
    
class Queue:
    def __init__(self, capacity=10):
        self.queue=ArrayList()
        self.capacity=capacity

    def enqueue(self, data):
        """Add new item at the back of the Queue(List)"""

    def dequeue(self):
        """Remove and return item from the start of Queue(Lis)"""

    def showQueue(self):
        """Show all items in the Queue"""

if __name__=="__main__":
    queue=Queue()