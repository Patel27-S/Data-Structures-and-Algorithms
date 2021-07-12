class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head_ptr = None


    # The below method's Time Complexity is O(1).
    def insert_at_beginning(self, data):
        '''
        This function adds the feature of adding a node
        at the beginning of the LinkedList.
        '''
        # First of all, I will create a new node.
        node = Node(data)
        node.next = self.head_ptr
        self.head_ptr = node
        # Time Complexity = O(1).


    # The below method's Time Complexity is O(n).
    # Since, we need to traverse through all the
    # elements of the Linked list.
    def display(self):
        '''
        This function serves the feature for the user to
        view the Linked List.'''
        # Now, we want to display the linkedlist.
        # Let us checkout the base case first :-
        if self.head_ptr == None:
            print('Linked List is empty!')
            return
        # Now, let's suppose the linkedlist is
        # not empty.
        temp_ptr = self.head_ptr
        while temp_ptr:
            print(temp_ptr.data,'->', end = '')
            temp_ptr = temp_ptr.next
        # Time Complexity = O(n).


    def insert_at_end(self, data):
        '''
        This function will add the data, a user
        would want to; at the end of Linked List.
        '''
        # First, we create a node to add to linkedlist.
        node_at_end = Node(data)

        # Base Case :- (If, LinkedList is empty!)
        if self.head_ptr == None:
            self.head_ptr = node_at_end
            return
        # If, otherwise :-
        temp_ptr = self.head_ptr
        while temp_ptr.next:
            temp_ptr = temp_ptr.next
        temp_ptr.next = node_at_end
        # Time Complexity = O(n).


    def insert_at_position(self, position, data):
        '''
        This function provides the feature of adding data to
        a particular position in LinkedList.
        '''
        # First of all, as always we'll create a node with input data.
        node_at_position = Node(data)

        # We need to traverse until the (pos-1)th node
        # and, then the temp_ptr.next will have to be
        # the (pos-1)th node's next, and its next as the node to be inserted.
        temp_ptr = self.head_ptr
        before_insertion_position = position-2
        while before_insertion_position:
            temp_ptr = temp_ptr.next
            before_insertion_position -= 1
        node_at_position.next = temp_ptr.next
        temp_ptr.next = node_at_position
        # Time Complexity is O(n).


    def insert_values(self, data_list):
        '''
        This function performs the feature of forming a refreshed linkedlist
        with all the values in list.
        '''
        self.head_ptr = None
        for data in data_list:
            self.insert_at_end(data)


    def delete_at_end(self):
        '''
        This function provides the feature of deleting
        the node at end of LinkedList.
        '''
        # For deleting the node at end, we need to take
        # a temp_ptr at the node before the end node.
        # And, then set its next as 'None'.
        temp_ptr = self.head_ptr
        position_at_end = 0

        # The below loop will tell us LinkedList's Length.
        # The loop will run until the next is 'None'.
        while temp_ptr.next:
            temp_ptr = temp_ptr.next
            position_at_end += 1

        # We are bringing the temp_ptr back to head_ptr.
        # And, then after taking it to (position_at_end - 1)
        # We can set its next to 'None'
        temp_ptr = self.head_ptr
        second_last_node = position_at_end-1
        while second_last_node:
            second_last_node -= 1
            temp_ptr = temp_ptr.next
        temp_ptr.next = None



    def length(self):
        '''
        This function returns the print of length of LinkedList.
        '''
        len = 0
        temp_ptr = self.head_ptr
        while temp_ptr:
            temp_ptr = temp_ptr.next
            len += 1
        return len


    def delete_at_position(self, position):

        temp_ptr = self.head_ptr

        if position == 1:
            self.head_ptr = self.head_ptr.next
            temp_ptr = None
        else:
            before_deletion_stop = position-2
            while before_deletion_stop:
                before_deletion_stop -= 1
                temp_ptr = temp_ptr.next
            temp_ptr.next = temp_ptr.next.next
            temp_ptr.next = None

    def sort(self):
        '''
        This method is used to sort a LinkedList.
        '''
        # The below method is not correct and I have to improve it.
        first_ptr = self.head_ptr
        second_ptr = self.head_ptr.next

        while second_ptr != None:
            if first_ptr.data < second_ptr.data:
                first_ptr.data, second_ptr.data = second_ptr.data, first_ptr.data
            first_ptr = first_ptr.next
            second_ptr = second_ptr.next




# Testing :-

l1 = LinkedList()

l1.insert_at_beginning(1)
l1.insert_at_end(2)
l1.insert_at_end(3)
l1.insert_at_end(4)
l1.insert_at_end(5)
#l1.delete_at_position(1)

l1.sort()
l1.display()

print()
print()
print('The length of LinkedList is : {}'.format(l1.length()))