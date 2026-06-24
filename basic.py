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

        if position == 0 : # jodi position zero hoi .. amader newNode ar next a amader current node ar ref rekhe dibo .. 
            new_node.next = self.head  # None -> newNode ar next akhn None hoye jabe  
            self.head = new_node # ai khane amar head ar modde newNode store kore dilam
            return 


        current = self.head   #jodi age theke node thake .... tah hole amra linked list ar 1st node k nilam . mane head ta k 

        for _ in range(position-1):  # je position a insert korbo oi node ar age porjontto jabo
            current = current.next

        
        new_node.next = current.next  # newNode ar next a current node ar next a Store kora Address k rekhe dilam
        current.next = new_node # and current node ar next a amra newNode ar address rekhe dilam


    def display(self):
        current = self.head 

        while current : 
            print(current.data , end=" -> ")
            current = current.next


    def delete_head(self):
        if self.head is None : 
            print('Head is Empty')
            return

        #supposed
        # head = [10,#1#1]
        # [10,#1#1],[20,None]
        
        self.head = self.head.next
        # head = #1#1
        # head = [20,None]
    

    def delete_end(self):


        if self.head is None:
            return
        

        if self.head.next is None:
            #head =  [10,None]
            self.head = None
            #head = None
            return


        temp = self.head
        while temp.next.next : 
            temp = temp.next 

        temp.next = None

    
    def remove_duplicate(self):

        current = self.head

        while current and  current.next : 

            if current.data == current.next.data : 
                current.next = current.next.next 
            else : 
                current = current.next 









ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(20)
ll.append(20)
ll.append(30)



ll.display()

ll.remove_duplicate()
print("unique list: ", end="")
ll.display()