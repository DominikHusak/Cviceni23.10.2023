class Node:
    def __init__(self, data):
        self.data = data  # Hodnota uložená ve frontě
        self.next = None  # Následující prvek
        self.prev = None  # Předchozí prvek

class Queue:
    def __init__(self):
        self.head = None  # Vrchol fronty
        self.tail = None  # Spodek fronty
        self.size = 0  # Velikost fronty

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def pop(self):
        if self.head is None:
            raise Exception("Fronta je prázdná.")
        data = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        self.size -= 1
        return data

    def count(self):
        return self.size

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def popAll(self):
        elements = []
        while self.head is not None:
            elements.append(self.pop())
        return elements

    def __contains__(self, item):
        current_node = self.head
        while current_node:
            if current_node.data == item:
                return True
            current_node = current_node.next
        return False

queue = Queue()
queue.add(1)
queue.add(2)
queue.add(3)

if 2 in queue:
    print("2 je v seznamu")
else:
    print("2 není v seznamu")

if 4 in queue:
    print("4 je v seznamu")
else:
    print("4 není v seznamu")
