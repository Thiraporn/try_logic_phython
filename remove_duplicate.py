class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class RemoveDuplicate:
    # Solution 1.1 Sorted using pointer  time  O(n)  space O(1)✅
    @staticmethod
    def remove_duplicate_sorted(head):
        current = head
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next  # remove dulicate
            else:
                current = current.next  # move current

        return head
    # Solution 1.2  sorted   by using Hashset time  O(n)  space O(n) -------------------> ❌❌❌❌ overkill ❌❌❌❌❌----> not recommended

    # Solution 2.1 Unsorted using pointer  time  O(n²)  space O(1)✅
    @staticmethod
    def remove_duplicate_unsorted(head):
        current = head
        while current:
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next
        return head

    # Solution 2.2  Unsorted   by using Hashset time  O(n)  space O(n)✅
    @staticmethod
    def remove_duplicate_unsorted_with_hashset(head):

        if head == None:
            return None

        seen = set()
        current = head
        prev = None
        while current:

            if current.data in seen:
                prev.next = current.next  # unchain duplicate
            else:
                seen.add(current.data)
                prev = current  # move prev only unique
            current = current.next

        return head

    # def print_nodes(self, node):
    @staticmethod
    def print_nodes(node):
        while node:
            if node.next:
                # print(f'{node.data} ->')   new line
                print(f'{node.data} ->', end="")  # same line

            else:
                print(node.data)
            node = node.next
        # print('None')


print(f'RemoveDuplicate (Sort:Pointer)')
head = Node(1)
n2 = Node(1)
n3 = Node(2)
n4 = Node(3)
n5 = Node(5)
n6 = Node(5)
n7 = Node(6)
n8 = Node(7)
head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
print(f'Before remove : ', end="")
RemoveDuplicate.print_nodes(head)
RemoveDuplicate.remove_duplicate_sorted(head)
print(f'After remove  : ', end="")
RemoveDuplicate.print_nodes(head)
print(f'----------------------------------------------------------------')
print(f'RemoveDuplicate (Unsort:Pointer)')
head2 = Node(1)
m2 = Node(7)
m3 = Node(2)
m4 = Node(1)
m5 = Node(2)
m6 = Node(1)
m7 = Node(3)
m8 = Node(1)
head2.next = m2
m2.next = m3
m3.next = m4
m4.next = m5
m5.next = m6
m6.next = m7
m7.next = m8
print(f'Before remove : ', end="")
RemoveDuplicate.print_nodes(head2)
RemoveDuplicate.remove_duplicate_unsorted(head2)
print(f'After remove  : ', end="")
RemoveDuplicate.print_nodes(head2)
print(f'----------------------------------------------------------------')

print(f'RemoveDuplicate (Unsort:Pointer)')
head3 = Node(1)
p2 = Node(7)
p3 = Node(2)
p4 = Node(1)
p5 = Node(2)
p6 = Node(1)
p7 = Node(3)
p8 = Node(1)
head3.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
p5.next = p6
p6.next = p7
p7.next = p8
print(f'Before remove : ', end="")
RemoveDuplicate.print_nodes(head3)
RemoveDuplicate.remove_duplicate_unsorted_with_hashset(head3)
print(f'After remove  : ', end="")
RemoveDuplicate.print_nodes(head3)
print(f'----------------------------------------------------------------')
