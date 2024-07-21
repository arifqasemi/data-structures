class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
class LinkedList:
    def __init__(self):
        self.head =None
        
    def display(self):
        current = self.head
        
        while current:
            print(current.data, end='->' if current.next else "")
            current = current.next
        print('')
        
        
    def insert_at_begening(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
        
    def insert_at_end(self,data):
        new_node = Node(data)
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    
    def insert_at_specific_position(self,data,position):
        new_node = Node(data)
        selected_element = self.head
        if position ==0:
            new_node.next = self.head
            self.head = new_node
            return
        
        for _ in range(position -1):
            if not selected_element:
                print('index out of band')
            selected_element = selected_element.next
        new_node.next = selected_element.next
        selected_element.next = new_node
        
        
    def delete_node(self,key):
        select_element = self.head
        if select_element.data == key:
            self.head = select_element.next
            select_element = None
            return
        while select_element:
            before_selected_element = select_element
            selected_node = select_element.next
            if selected_node.data == key:
                before_selected_element.next = selected_node.next
                selected_node= None
            select_element = select_element.next
            
    def update_node(self,data,key):
        current = self.head
        while current:
            if current.data == key:
                current.data = data
                return
            current = current.next
            
    def reverse_iterative(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            # print(next_node.data)
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        
         
                
  
        

linkedList = LinkedList()

linkedList.insert_at_begening(1)
linkedList.insert_at_begening(2)
linkedList.insert_at_begening(3)
linkedList.insert_at_begening(4)
# linkedList.insert_at_end(4)
# linkedList.insert_at_specific_position(5,)
# linkedList.delete_node(5) 
# linkedList.delete_node(3)
# linkedList.delete_node(4)
# linkedList.update_node(6,1)
# linkedList.update_node(7,5)
linkedList.display()
linkedList.reverse_iterative()

# linkedList.display()






