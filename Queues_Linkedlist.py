class Node:

    def __init__(self, data=None):
        self.data=data
        self.prev= None
        self.next= None

class SLL:
    def __init__(self):
        self.head= Node()

    def add(self, data):
        """Add data at the end"""
        new_data=Node(data)
        if self.head is None:
            self.head=new_data

        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next= new_data

    def remove(self):
        """Remove item. Default last item."""

    def show(self):
        curr= self.head.next
        while curr:
            print(curr.data)
            curr=curr.next

if __name__=="__main__":
    sll=SLL()
    sll.add("data1")
    sll.add("data2")
    sll.add("data3")
    sll.show()