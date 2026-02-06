class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __len__(self):
        return self.size

    def __repr__(self):
        items = []
        current_item = self.top

        while current_item:
            items.append(str(current_item.data))           
            current_item = current_item.next
        
        return ", ".join(items)
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

        self.size += 1 

    def pop(self):
        if self.top is None:
            raise ValueError("Stack is empty")
        else: 
            popval = self.top.data
            self.top = self.top.next

            self.size +=1 
            return popval

    def peek(self):
        if self.top is None:
            raise ValueError("Stack is empty")
        else:
            return self.top.data
    def is_empty(self):
        return self.top is None
    

if __name__ == "__main__":
    stack = Stack()

    stack.push(65)
    stack.push("John")
    stack.push({
        "hello" : "world",
        "lang": "python"
    })
    stack.push(1)

    print(stack.peek())
    stack.pop()

    print(stack)
