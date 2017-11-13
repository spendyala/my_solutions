class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


def runner_techinque_recursive(pointer_1, pointer_2):
    if not pointer_1:
        return pointer_2.next

    pointer_1 = pointer_1.next
    if pointer_1 and pointer_1.next:
        pointer_2 = pointer_2.next
        pointer_1 = pointer_1.next
    return runner_techinque_recursive(pointer_1, pointer_2)

def runner_techinque_iterative(head):
    pointer_1 = head
    pointer_2 = head
    while pointer_2.next:
        pointer_2 = pointer_2.next
        if pointer_2.next:
            pointer_2 = pointer_2.next
            pointer_1 = pointer_1.next
    return pointer_1


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
print(runner_techinque_recursive(head.next.next, head).__dict__)
print(runner_techinque_iterative(head).__dict__)

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)
print(runner_techinque_recursive(head.next.next, head).__dict__)
print(runner_techinque_iterative(head).__dict__)


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
# head.next.next.next.next.next.next.next = Node(8)
print(runner_techinque_iterative(head).__dict__)
