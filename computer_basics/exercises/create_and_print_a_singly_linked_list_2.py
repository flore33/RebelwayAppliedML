class Node:
    def __init__(self, data=None, next=None):
        #  set data and next
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        #initialize head
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count


    def remove_at_index(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head

        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at_index(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, after_value, insert_value):
        if self.head is None:
            raise Exception("Linked list is empty")
        
        itr = self.head

        while itr:
            if itr.data == after_value:
                node = Node(insert_value, itr.next)
                itr.next = node
                return
            itr= itr.next
        raise Exception(f"value {after_value} is not in the list")
    
    def remove_by_value(self, data):
        if self.head is None:
            raise Exception("Linked list is empty")
        
        if self.head and self.head.data == data:
            self.head = self.head.next

        
        previous = None
        itr = self.head

        while itr:

            if itr.data == data:

                previous.next = itr.next
                return
            
            previous = itr
            itr = itr.next

    def remove_by_value_duplicate(self, data):
        if self.head is None:
            raise Exception("Linked list is empty")
        
        while self.head and self.head.data == data:
            self.head = self.head.next

        
        previous = None
        itr = self.head

        #traverse the list delete all occurences
        while itr is not None:

            if itr.data == data:

                    previous.next = itr.next# unlink
                #move to next node
                    itr = itr.next

            else:
                previous = itr
                itr = itr.next
        return itr
    
    def reverse_linked_list(self):
        if self.head is None:
            raise Exception("Linked list is empty")
        if self.head.next is None:
            return self.head    
        
        itr = self.head
        previous = None
        while itr:
            
            #store next
            nextNode = itr.next
            # reverse current next pointer
            itr.next = previous
            #move pointer one ahead
            previous = itr
            itr = nextNode
        self.head = previous
        return previous



          # Create a hard-coded linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    #head = Node(1)
    #nexNode:head.next = Node(2) 
   # head.next.next = Node(3)
    #head.next.next.next = Node(4)
    #head.next.next.next.next = Node(5)

#list = [2,3,2,5]
#node = Node(2)
#node.next = Node(3)
#node.next.next = Node(2)

    def find_middle_element(self):

        index = 0
        itr = self.head
        half = self.get_length() // 2
        while index < half:
            #itr = itr.next
            itr = itr.next
            index += 1    
             
        return itr.data
    

    def if_detect_loop(self):

        set_list = set()
        itr = self.head

        while itr is not None:
            if itr in set_list:

                return True
            
            set_list.add(itr)
            
            itr = itr.next    
        return False

    def detect_loop_floyd(self):

        slow = self.head
        fast = self.head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False
    
    def remove_nth_from_end(self, n):

        if n < 0 or n > self.get_length():
            raise Exception("n is not valid")
        


        itr = self.head
        index = n
        count = 0
        length_list = self.get_length()
        target_length  = length_list - n
        
        if n == target_length:
            self.head = self.head.next
            return

        while itr is not None:
            if count == target_length - 1:
                

                itr.next = itr.next.next #break link
                break

            itr = itr.next
            count +=1
        return
            
    def ll_reversing_portion(self, m, n):

        if self.head.next is None:
            return self.head
        
        itr = self.head
        dummy = Node(0, itr)
        left_previous = None
        left = m
        right = n
        count = 0
        previous = None

        if m == 1:
            self.head = previous
    
        for i in range(left - 1):
            # node from we start reverse
            left_previous = itr
            itr = itr.next

        start_sublist = itr
        for i in range(right - left + 1):
              
            nextNode = itr.next
            itr.next = previous
            previous = itr
            itr = nextNode

        left_previous.next = previous
        start_sublist.next = itr

        print("CURRENT itr:", itr.data if itr else None)
        print("→ nextNode:", nextNode.data if isinstance(nextNode, Node) else None)
        print("← left_previous:", left_previous.data if isinstance(left_previous, Node) else left_previous)
        print("← previous:", previous.data if isinstance(previous, Node) else previous)
        print("← start_sublist:", start_sublist.data if isinstance(start_sublist, Node) else start_sublist)
            
           
        #self.head = previous
    
        #print(itr.data) 
        
        return(previous)
            

        
    #ll=[1, 2, 3, 4, 5]


    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        llstr = ''

        while itr:    
            llstr += str(itr.data) + '--→'
            itr = itr.next

        print(llstr)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["apple", "prune", "grapes", "melon", "amamde","noix", "dates", "lemon", "peach", "ginger"])
    #ll.remove_at_index(2)
    #ll.insert_at_index(1, "noix")
    
    #ll.insert_after_value("apple", "ananas")
    #ll.remove_by_value("prune")
    #ll.remove_by_value_duplicate("melon")
    #ll.reverse_linked_list()
    #ll.head.next.next.next.next = ll.head.next
    #if ll.detect_loop_floyd():
    #    print(True)
    #else:
    #    print(False)
    #ll.remove_nth_from_end(4)
    ll.ll_reversing_portion(4, 7)

    #print(ll.find_middle_element())
    ll.print()
    #print('length linked link:', ll.get_length())

