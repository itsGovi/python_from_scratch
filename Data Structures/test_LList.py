from Linked_list import LinkedList

if __name__ == "__main__":
    
    my_list = LinkedList()
    
    my_list.add('amma')
    my_list.add('nanna')
    my_list.add('akka')
    
    print("Linked list after adding nodes:")
    my_list.traverse()
    
    
    my_list.remove('nanna')
    
    print("Linked list after removing node with data 'nanna':")
    my_list.traverse()
    
    # Attempt to remove a node not in list
    my_list.remove('govi') # Expected error: node with data 'govi' not found
    
    print("Linked list after attempting to remove a non-existing node:")
    my_list.traverse()