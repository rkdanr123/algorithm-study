# Linked List

- **Big O Analysis: Array vs (Singly) Linked List**
    - Indexing
        - Array: O(1)
        - Linked List: O(n)
    - Searching
        - Array: Linear Search O(n) / Binary Search O(log n) (cf. Binary Search: In case of sorted array.)
        - Linked List: O(n)
    - Insert/Delete element at start
        - Array: O(n)
        - ***** Linked List: O(1) *****
    - Insert/Delete element at end
        - Array: Usually O(1)  (But if array is already full, it needs to be resized. So the worst-case is O(n).)
        - Linked List: O(n)
    - Insert element in Middle
        - Array: O(n)
        - Linked List: O(n)  (Actual insertion is O(1), but Searching process requires O(n).)

- Code: **Node** Class
    - How to make Node and How to Add Nodes
        
        ```python
        # How to Implement Node Class
        class Node:
            def __init__(self, data):
                self.data = data
                self.next = None
        
        # How to Add Nodes
        
        # Sol 1
        head = Node(2)
        head.next = Node(6)
        head.next.next = Node(7)
        
        # Sol 2 (recommended)
        node = head
        while node.next:
            node = node.next
        
        node.next = Node(4)
        ```
        
    - How to print elements
        
        ```python
        # with above code
        
        node = head
        while node:
            print(node.data, "   ")
            node = node.next
        ```
        
    - To Add a New Node in front of Linked List
        
        ```python
        """
        1. Create a New Node. Its 'next' will be None.
        2. Make new node's 'next' point to head node.
        3. Change head from original head to new node.
        """
        
        NewNode = Node(4)
        NewNode.next = head
        head = NewNode
        ```
        
- Code: **LinkedList** Class
    
    ```python
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    class LinkedList:
        def __init__(self):
            self.head = None
            self.length = 0
    
    ```
    
    ```python
        def GetLength(self):
            return self.length
           
        def AppendLeft(self, data):
            if self.head is None:
                self.head = Node(data)
            else:
                node = Node(data)
                node.next = self.head
                self.head = node
              
            self.length += 1
        
        def AppendEnd(self, data):
            if self.head is None:
                self.head = Node(data)
            
            else:
                node = self.head
                while node.next:
                    node = node.next
                
                node.next = Node(data)
            
            self.length += 1
            
    
        def PrintElements(self):
            if self.head is None:
                return "Linked List is empty now."
            
            Elements = ""
            
            node = self.head
            while node:
                Elements += str(node.data) + " -> "
                node = node.next
            
            return Elements
            
        def TargetExist(self, target):
            if self.head is None:
                return False
            
            node = self.head
    
            while node:
                if node.data == target:
                    return True
                
                node = node.next
            
            return False
            
            
        def PopLeft(self):
            if self.head is None:
                return
            
            node = self.head
    
            self.head = self.head.next
            self.length -= 1
    
            return node.data
    
        
        def PopEnd(self):
            if self.head is None:
                return
            
            node = self.head
            prev = None
    
            if node.next is None:  # Case: The length of linked list is equal to 1.
                self.head = None
                self.length -= 1
                return node.data
    
            while node.next:
                prev = node
                node = node.next
            
            prev.next = None
            self.length -= 1
    
            return node.data
     
     
         def remove(self, target):
            node = self.head
            while node is not None and node.data != target:
                prev = node
                node = node.next
    
            if node is None:   # Case: There is no target in linked list.
                return False
            
            if node == self.head:   # Case: Target is at the first place of linked list.
                self.head = node.next
            else:   # Case: Target exists in linked list, but not the first place.
                prev.next = node.next
            self.length -= 1
            return True
      
          def InsertAt(self, i, data):
            if i < 0 or i > self.GetLength():
                raise Exception("Invalid Index")
            
            if i == 0:
                self.AppendLeft(data)
                return
            
            for _ in range(i - 1):
                node = node.next
            
            NewNode = Node(data)
            NewNode.next = node.next
            node.next = NewNode
            self.length += 1
      
    ```