class ListNode:
    def __init__(self, value: int = 0, next: 'ListNode' = None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def append(self, value: int):
        """Append a value to the end of the linked list."""
        if not self.head:
            self.head = ListNode(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = ListNode(value)

    def reverse(self):
        """Reverse the linked list in place."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        """Sort the linked list using insertion sort algorithm."""
        if not self.head or not self.head.next:
            return

        sorted_head = None
        current = self.head

        while current:
            next_node = current.next
            sorted_head = self._sorted_insert(sorted_head, current)
            current = next_node

        self.head = sorted_head

    def _sorted_insert(self, head: 'ListNode', node: 'ListNode') -> 'ListNode':
        """Helper method to insert a node into the sorted part of the list."""
        if not head or node.value < head.value:
            node.next = head
            return node

        current = head
        while current.next and current.next.value < node.value:
            current = current.next

        node.next = current.next
        current.next = node
        return head

    @staticmethod
    def merge_sorted_lists(list1: 'ListNode', list2: 'ListNode') -> 'ListNode':
        """Merge two sorted linked lists into one sorted linked list."""
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.value < list2.value:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2

        return dummy.next

    def print_list(self):
        """Print the linked list."""
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


linked_list1 = LinkedList()
linked_list1.append(3)
linked_list1.append(4)
linked_list1.append(1)
linked_list1.append(2)
linked_list1.append(5)

print("Initial list:")
linked_list1.print_list()

linked_list1.reverse()
print("Reversed list:")
linked_list1.print_list()

linked_list1.insertion_sort()
print("Sorted list:")
linked_list1.print_list()

linked_list2 = LinkedList()
linked_list2.append(2)
linked_list2.append(7)
linked_list2.append(6)
linked_list2.append(8)

print("Second sorted list:")
linked_list2.print_list()

merged_head = LinkedList.merge_sorted_lists(linked_list1.head, linked_list2.head)

merged_list = LinkedList()
merged_list.head = merged_head
print("Merged two sorted lists:")
merged_list.print_list()