# How to make node 
class Node : 
    # constructor 
    def __init__(self,data):
        self.data= data
        self.next = None


class LinkedList : 

    def __init__(self) : 
        self.head = None

    # insert at End 
    def append(self,newValue) :
        new_Node = Node(newValue)  #[data,None]

        if self.head is None :   
            self.head = new_Node   #akhn newNode Hocce Head .. 
            return 

        current = self.head  #1st node ta k nilam 

        while current.next : 
            current = current.next 

        current.next = new_Node #new node ar ref rekhe disi 
    # 0     1    2    3
    # 10 -> 20 -> 30 -> 40 -> none
    # position-> 2 insert data 25




    def insert_at_position(self,position,new_value):

        new_node = Node(new_value) #create new node 


        if position == 0 :
            new_node.next = self.head 
            self.head = new_node
            return 


        current = self.head 

        for _ in range(position-1):
            current = current.next

        
        new_node.next = current.next 
        current.next = new_node


    def display(self):
        current = self.head 

        while current : 
            print(current.data , end=" -> ")
            current = current.next


ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)

ll.insert_at_position(1,11)

ll.display()
