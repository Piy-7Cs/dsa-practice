class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
    
class DoublyLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # O(n)
    def __repr__(self):
        if self.head is None:
            return "[]"
        else: 
            temp = self.head
            return_string = "["
            while temp:
                return_string += f"{temp.value} -> "
                temp = temp.next
            return_string += "None ]"

            return return_string


    
    # O(n)
    def __contains__(self, value):
        temp = self.head
        while temp is not None:
            if temp.value == value:
                return True
            temp = temp.next
        return False
    
    # O(n) linear, can be made constant by simple having a size aattribute in the class which is updated on every operation
    def __len__(self):
        counter = 0
        temp = self.head
        while temp is not None:
            counter += 1
            temp = temp.next
        return counter
    
    
    # O(1)
    def append(self, value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
        else:
            new_node = Node(value)
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # O(1)
    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else: 
            first_node = Node(value)
            first_node.next = self.head
            self.head.previous = first_node
            self.head = first_node

    # O(n)
    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
        else : 
            if self.head is None:
                raise ValueError("Index is out of bounds" )
            else: 
                temp = self.head
                for i in range(index-1):
                    if temp.next is None:
                        raise ValueError("Index is out of bounds")
                    temp = temp.next
                    
                new_node = Node(value)
                new_node.next = temp.next
                new_node.previous = temp
                if temp.next:
                    temp.next.previous = new_node
                
                temp.next = new_node

    # O(n)
    def delete(self, value):
        temp = self.head
        if temp is None:
            return
        
        if temp.value == value:
            self.head == temp.next
        
        while temp:
            if temp.value == value:
                temp.previous.next = temp.next
                temp.next.previous = temp.previous
                break
            temp = temp.next

    # O(n) 
    def pop(self, index):
        if self.head ==None:
            raise ValueError("Index out of bounds")
        else: 
            temp = self.head

            for i in range(index):
                if temp is None:
                    raise ValueError("Index out of bounds")
                temp = temp.next
            if temp is None:
                    raise ValueError("Index out of bounds")
            else:
                temp.previous.next = temp.next
                temp.next.previous = temp.previous

    def get(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            temp = self.head
            for i in range(index):
                if temp is None:
                    raise ValueError("Index Out of bounds")
                temp = temp.next
            return temp.value 
    

if __name__ == "__main__":
    ll = DoublyLinkedlist()

    ll.append(10)
    ll.insert(40, 1)
    ll.insert(50,1)
    ll.insert(70,2)
    ll.prepend(1000)

    ll.insert(5656, 3)
    print(ll)

    print(100 in ll)
    print(1000 in ll)