class Node:  
      
    def __init__(self, data):  
        self.data = data  
        self.next = None
  

def arrange( head): 
  
    temp = head 
      
    
    d = [] 
      
  
    while (temp != None) : 
        d.append(temp.data) 
        temp = temp.next
      
    
    i = 0
    temp = head 
    while (len(d) > 0) : 
        if (i % 2 == 0) : 
            temp.data = d[0] 
            d.pop(0) 
          
        else : 
            temp.data = d[-1]  
            d.pop()  
          
        i = i + 1
  
        temp = temp.next
          
    return head 
      

def push( head_ref, new_data): 
  
    
    new_node = Node(0) 
  
    
    new_node.data = new_data 
  
     
    new_node.next = (head_ref) 
  
   
    (head_ref) = new_node 
    return head_ref 
  

def printList( head): 
  
    temp = head 
    while (temp != None) : 
        print( temp.data,end=" ") 
        temp = temp.next
  

  

head = None
  
head = push(head, 5) 
head = push(head, 4) 
head = push(head, 3) 
head = push(head, 2) 
head = push(head, 1) 
print("Given linked list\t") 
printList(head) 
head = arrange(head) 
print( "\nAfter rearrangement\t") 
printList(head)
