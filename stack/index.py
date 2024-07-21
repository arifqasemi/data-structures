class Stack:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.top = None
        
    def display(self):
        current = self.top
        while current:
            print(current.data,end='->' if current.next else '')
            current = current.next
        

    def push(self, data):
        new_node = self.Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    def peek(self):
        return self.top.data if self.top else None

    def is_empty(self):
        return self.top is None

# Example Usage:
browser_stack = Stack()
browser_stack.push("www.example1.com")
browser_stack.push("www.example2.com")
browser_stack.push("www.example3.com")
browser_stack.display()
# print("Current page:", browser_stack.peek())  
# browser_stack.pop()
# print("Back to:", browser_stack.peek())  
