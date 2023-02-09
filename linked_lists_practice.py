import time


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        # self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None :
            print("empty list")
            return

        list_object = self.head
        ll = ''
        while list_object :
            ll += str(list_object.data) + '-->'
            list_object = list_object.next
        print(ll)

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    #
    # def insert_at_end(self, data):
    #     node = Node(data, None)
    #     head = self.head
    #     if not head :
    #         self.head = node
    #
    #     while head :
    #         next = head.next
    #         if next :
    #             head = next
    #         else :
    #             head.next = node
    #             break

    def insert_at_end(self, data):
        print('new one')
        node = Node(data, None)
        if self.head is None :
            self.head = node
            return

        head = self.head
        while head.next is not None:
            head = head.next

        head.next = node


    def insert_elements(self, list):
        print('bp-1')
        first_node = Node(list[0], None)
        if self.head is None :
            self.head = first_node
            print('bp-2')
            return

        else :
            print('bp-3')

            head = self.head
            while head.next :
                head = head.next
            head.next = first_node
            # 3 ways of defining head
            # head = head.next
            print('bp-4')
            # head = first_node
            new_head = first_node
            head = new_head
        for i in list[1:]:
            node = Node(i, None)
            head.next = node
            #can be done in 3 ways
            # head = head.next
            # head = node
            new_head = node
            head = new_head


    def length(self):
        count = 0
        head = self.head
        if head :
            count = 1
        else :
            count = 0
            return count

        while head.next :
            count += 1
            head = head.next
        return count


    def insert_at_index(self, index, data):
        l = self.length()
        if index > l :
            print("List index out of range")
            return

        head = self.head

        for i in range(1, index):
            head = head.next

        print('now at head ', head.data)
        # prev_head = head
        # next_head = head.next
        new_node = Node(data, head.next)
        # new_head = new_node
        # prev_head.next = new_head
        # new_head.next = next_head

        head.next = new_node
        print(f"successfully added {data}")


    def insert_after_val(self, val, data):
        if self.head is None :
            print("Empty List")
            return

        head = self.head

        l = self.length()
        found_val = False

        for i in range(l):
            head_val =head.data
            if head_val == val :
                found_val = True
                new_node = Node(data, head.next)
                head.next = new_node
                break
            else:
                head = head.next

        if not found_val :
            print("Val not found!!!")
        else:
            print(f"successfully added {val}")

    def pop_last_element(self):
        if self.head is None :
            print("empty list")
            return

        head = self.head
        while head.next.next :
            head = head.next

        print('head', head, 'data', head.data, head.next)
        # del head
        head.next = None

    def delete_element_at_index(self, index):
        if self.head is None :
            print("empty List")
            return
        head = self.head
        # removed = False
        l = self.length()
        if index > l-1 :
            print("list index out of range")
            return
        elif index == 0:
            self.head = head.next

        for i in range(1, index):
            head = head.next

        if head.next.next :
            head.next = head.next.next
        else:
            head.next = None

        print(f"removed element at {index}")

    def delete_element(self, val):
        print(f"remove element {val}")
        if self.head is None :
            print("empty List")
            return
        head = self.head
        data_found = False

        l=self.length()

        if head.data == val :
            if self.head.next :
                self.head = self.head.next
            else:
                self.head = None
            data_found = True

        for i in range(1,l):
            if head.next:
                data = head.next.data
                if data == val :
                    data_found = True
                    head.next = head.next.next
                head=head.next
        if not data_found:
            print("Val not found")


# case 1 : single element
# case 2 :




try:
    l = LinkedList()
    l.insert_at_beginning(12)
    l.insert_at_beginning(22)
    l.insert_at_beginning(13)
    l.print()
    l.insert_at_end(33)
    l.print()
    l.insert_elements([1,2,3,4,5,6,7])
    l.insert_at_beginning(29)
    l.print()
    l.insert_at_index(4, 67)
    print('length of the iterm is ', l.length())
    l.print()
    l.insert_after_val(67,68)
    l.print()
    l.insert_after_val(69,68)
    l.print()
    l.pop_last_element()
    l.print()
    l.delete_element_at_index(4)
    l.print()
    l.delete_element_at_index(1)
    l.print()
    l.delete_element_at_index(0)
    l.print()
    l.delete_element_at_index(9)
    l.print()
    l.delete_element(22)
    l.print()
    l.delete_element(1)
    l.print()



    # print('l.head', l.head.data, l.head.next)
except Exception as e:
    print(e)
    print("Error Occurred!!!")
    
    
    
    
    
    
    
    

    # def insert_at_end(self, data):
    #     if self.head is None:
    #         self.insert_at_beginning(data)
    # 
    #     nxt = self.head
    #     while nxt.next :
    #         nxt = nxt.next
    #     nxt.next = Node(data, None)



        # while nxt :
        #     time.sleep(1)
        #     print('head data', nxt.data)
        #     nxt1 = nxt
        #     nxt = nxt.next
        #     if not nxt :
        #         print('nxt obj', nxt)
        #         node = Node(data, None)
        #         nxt1.next = node
        #         break
        # nxt = node

        # nxt = self.head.next
        # while nxt.next :
        #     nxt = nxt.next
        # node = Node(data, None)
        # nxt.next = node

    # def insert_items(self, items):
    #     hd = self.head
    #
    #     while hd :
    #         hd = self.head.next
    #
    #
    #     for i in items :
    #         node = Node(i, )


