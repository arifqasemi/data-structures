class Queue:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = self.Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        dequeued_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_node.data

    def peek(self):
        return self.front.data if self.front else None

    def is_empty(self):
        return self.front is None

# Example Usage:
printer_queue = Queue()
printer_queue.enqueue("Print job 1")
printer_queue.enqueue("Print job 2")
printer_queue.enqueue("Print job 3")

print("Next job to print:", printer_queue.peek())  # Output: Print job 1
printer_queue.dequeue()
print("Next job to print:", printer_queue.peek())  # Output: Print job 2
