import traceback

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None :
            print("empty list")
            return

        head = self.head
        ll = []
        while head:
            temp = f'{head.data} --> '
            # print(head.data, "-->")
            head = head.next
            ll.append(temp)
        print("Linked List ===> ", ll)


    def add_item_to_list_at_end(self, data):
        if self.head is None :
            node = Node(data, None, None)
            self.head = node
            return

        head = self.head
        while head.next.next :
            head = head.next

        node = Node(data=data, prev=head, next=None)
        head.next.next = node

    def add_items_to_list(self, list):
        if self.head is None :
            node = Node(data=list[0], prev=None, next=None)
            self.head = node
            head = self.head
        else :
            head = self.head
            while head.next :
                head = head.next

        print('current_head=', head, head.data, head.prev, head.next)
        for i in list[1:]:
            new_node = Node(data=i, prev=head, next=None)
            head.next = new_node
            head = new_node

    def print_backwards(self):
        if self.head is None :
            print("empty list")
            return


        head = self.head
        while head.next :
            head = head.next

        while head.prev:
            print(head.data, '-->')
            head = head.prev
        print(head.data, '-->')





if __name__=='__main__':
    try:
        ll = LinkedList()
        ll.print()
        ll.add_item_to_list_at_end(12)
        list = [1,2,3,4,55,33,21,23,13,12]
        ll.add_items_to_list(list)
        ll.print()
        ll.print_backwards()
    except:
        print("Error Occurred!!!")
        traceback.print_exc()


