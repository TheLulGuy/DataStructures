# My magnum opus of linked list classes

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node #type: ignore


    #! Making an alias for insert_at_end and append to be the same
    insert_at_end = append

    def insert_at_beginning(self, value):
        new_node = Node(value)
        current = self.head
        self.head = new_node
        new_node.next = current

    # Display
    def display(self):
        current = self.head
        while current:
            print(current.value, end='->')
            current = current.next
        print('None')

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return "->".join(values) + '->None'


    def deletion_by_value(self, value):
        # Loop through all the values in the linked list

        current = self.head
        last = None
        while current:
            if current.value == value:
                # Try assigning the last nodes next value to the current values next value(skipping the deleted Node)
                try:
                    last.next = current.next

                # The only time this will cause an error is when last = None
                # This is possible only when the linked list is empty, or the value to be removed is the first value
                except:
                    self.head = current.next


                break

            # Assigning the last variable to lag behind the current variable
            last = current
            current = current.next





    def deletion_by_index(self, index):
        current = self.head
        current_index = 0
        last = None

        while current:
            if current_index == index:
                try:
                    last.next = current.next
                except:
                    self.head = current.next

                break

            current_index += 1

            last = current
            current = current.next


def bubble_sort(linked_list):
    if linked_list.head == None:
        return

    swapped = True
    while swapped:
        swapped = False
        currrent = linked_list.head
        while currrent and currrent.next:
            if currrent.value > currrent.next.value:
                currrent.value, currrent.next.value = currrent.next.value, currrent.value
                swapped = True

            currrent = currrent.next

