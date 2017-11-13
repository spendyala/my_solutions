class Node(object):
    def __init__(self, data=None, next=None, random=None):
        self.data = data
        self.next = next
        self.random = random
    def __repr__(self):
        str((self.data, self.next, self.random))

head = Node(10)
head.next = Node(5)
head.next.next = Node(3)
head.random = head.next.next
head.next.random = head
head.next.next.random = head.next

temp = head
while temp:
    new_node = Node(temp.data+100, temp.next)
    temp.next = new_node
    temp = new_node.next

temp = head
while temp:
    temp.next.random = temp.random.next
    temp = temp.next.next


temp = head
head_copy = head.next
temp_copy = head_copy
import pdb; pdb.set_trace()
while temp:
    print(temp.__dict__)
    print(temp_copy.__dict__)
    temp.next = temp_copy.next
    temp = temp.next
    temp_copy.next = temp.next
    temp_copy = temp_copy.next
    if not (temp and temp_copy):
        break

# O(N^2)
# O(N) + O(N) = 2*O(N)

temp = head
while temp:
    print('Node')
    print('Node.data: %s' % temp.data)
    print('Node.next: %s' % (temp.next.data if temp.next else None))
    print('Node.random: %s' % (temp.random.data if temp.random else None))
    temp = temp.next

temp = head_copy
while temp:
    print('Node')
    print('Node.data: %s' % temp.data)
    print('Node.next: %s' % (temp.next.data if temp.next else None))
    print('Node.random: %s' % (temp.random.data if temp.random else None))
    temp = temp.next

# data: 10
# next: -> data: 5
#          next: -> data: 3
#                   next: -> None
