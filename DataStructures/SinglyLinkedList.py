class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def addNodeAtEnd(self, data):
        new_node = Node(data)
        if(self.head == None):
            self.head = new_node
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node
    
    def addNodeAtStart(self,data):
        new_node = Node(data)
        if(self.head):
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
        

    def addNodeAtPosition(self,data,pos):
        new_node = Node(data)
        if(pos == 0):
            new_node.next = self.head
            self.head = new_node
        elif(pos > 0):
            prev = self.head
            for i in range(pos-1):
                prev = prev.next
            temp = prev.next
            prev.next = new_node
            new_node.next = temp
    
    def deleteNodeWithValue(self,value):
        if(self.head.data == value):
            self.head = self.head.next
        else:
            temp = self.head
            prev = None
            while(temp):
                if(temp.data == value):
                    break
                prev = temp
                temp = temp.next
            prev.next = temp.next
            temp = None

    def deleteNodeAtPosition(self,pos):
        if(pos == 0):
            self.head = self.head.next
        elif(pos > 0):
            temp = self.head
            prev = None
            count = 0
            while(temp and count != pos):
                prev = temp
                temp=temp.next
                count+=1
            if(temp == None):
                return
            else:
                prev.next = temp.next
                temp = None

    def deleteList(self):
        self.head = None
    
    def printList(self):
        if(self.head == None):
            print('Empty list')
            return
        temp = self.head
        while(temp != None):
            print(temp.data)
            temp = temp.next

llist = LinkedList()
query = 0

while(query != 8):
    print('Available Commands:\n\t1. Print List\n\t2. Insert At End\n\t3. Insert At Start\n\t4. Insert At Position\n\t5. Delete Value\n\t6. Delete At Position\n\t7. Delete List\n\t8. Exit')
    query = int(input('Select Command: '))
    
    if(query == 1):
        llist.printList()
    elif(query == 2):
        data = int(input('Enter data: '))
        llist.addNodeAtEnd(data)
    elif(query == 3):
        data = int(input('Enter data: '))
        llist.addNodeAtStart(data)
    elif(query == 4):
        data = int(input('Enter data: '))
        pos = int(input('Enter position: '))
        llist.addNodeAtPosition(data,pos)
    elif(query == 5):
        val = int(input('Enter deletion value: '))
        llist.deleteNodeWithValue(val)
    elif(query == 6):
        pos = int(input('Enter deletion position: '))
        llist.deleteNodeAtPosition(pos)
    elif(query == 7):
        llist.deleteList()
    
    
    
    
    


