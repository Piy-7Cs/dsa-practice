class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None
    
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
    
    
    # O(n) liner time
    def append(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(value)

    # O(1) Constant time
    def prepend(self, value):
        first_node = Node(value)
        first_node.next = self.head
        self.head = first_node

    # O(n) Linear time
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
                temp.next = new_node

    # O(n) Linear time
    def delete(self, value):
        temp = self.head
        if temp is None:
            return
        
        if temp.value == value:
            self.head == temp.next
        
        while temp.next:
            if temp.next.value == value:
                temp.next = temp.next.next
                break
            temp = temp.next

    # O(n) linear time
    def pop(self, index):
        if self.head ==None:
            raise ValueError("Index out of bounds")
        else: 
            temp = self.head

            for i in range(index-1):
                if temp.next is None:
                    raise ValueError("Index out of bounds")
                temp = temp.next
            if temp.next is None:
                    raise ValueError("Index out of bounds")
            else:
                temp.next = temp.next.next


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
    ll = Linkedlist()

    ll.append(10)
    ll.append(40)
    ll.append(73)
    ll.append(12)
    ll.append(1)
    ll.prepend(1000)

    ll.insert(66, 3)
    ll.delete(12)
    print(ll.get(5))

    ll.pop(3)

    print(ll)

    print(100 in ll)
    print(1000 in ll)