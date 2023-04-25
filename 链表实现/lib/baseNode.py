class node:
    def __init__(self, payload, next=None):
        self.data = payload
        self.next = next

def reversed(head):
    if head is None or head.next is None:
        return head
    pre = None
    cur = head
    h = head
    while cur:
        h = cur
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return h

def myprint(header):
    while header != None:
        print(header.data)
        header = header.next

header = None
for i in range(7):
    header = node(i, header)

myprint(header)
print('\n反转后的\n')
myprint(reversed(header))

