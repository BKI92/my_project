class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        found_nodes_list = []
        while node:
            if node.value == val:
                found_nodes_list.append(node.value)
            node = node.next
        return found_nodes_list

    def delete(self, val, all=False):
        if self.head is None:
            return
        old = node = self.head
        while node:
            if node.value is val:
                if node.next is None:
                    node = node.next
                    old.next = node
                    break
            old = node
            node = node.next

                # else:
                #     node = node.next.next.next
            node = node.next

    def clean(self):
        self.__init__()

    def len(self):
        length = 0
        if not self.head:
            return print(f'Длина списка - {length}')
        node = self.head
        while node:
            length += 1
            node = node.next
        return length

    def insert(self, afterNode, newNode):
        if self.head is None:
            return
        node = self.head
        while node:
            value = node.value
            if value is afterNode:
                if not node.next:
                    if value is afterNode:
                        node.next = Node(newNode)
                else:
                    next_node = node.next
                    node.next = Node(newNode)
                    node.next.next = next_node
                    Node(newNode).next = node.next.next
            node = node.next


s_list = LinkedList()
n1 = Node(12)
n2 = Node(55)
n1.next = n2
s_list.add_in_tail(Node(128))
s_list.add_in_tail(Node(128))
s_list.add_in_tail(n1)
s_list.add_in_tail(Node(128))
s_list.add_in_tail(n2)
s_list.add_in_tail(Node(128))
s_list.add_in_tail(Node(128))
s_list.add_in_tail(Node(7))
s_list.add_in_tail(Node(12))
s_list.add_in_tail(Node(5))
s_list.add_in_tail(Node(128))
s_list.add_in_tail(Node(77))
s_list.add_in_tail(Node(128))
s_list.print_all_nodes()
print('*'*20)
s_list.delete(128, all=True)
# s_list.insert(77, 25)
# s_list.print_all_nodes()
# s_list.insert(12, 111)
# s_list.insert(111, 8)
# s_list.insert(128, 3)
# print('*'*20)
s_list.print_all_nodes()
