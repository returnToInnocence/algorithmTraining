from lib import baseNode

class LinkList:
    def __init__(self, lst):
        self.head = baseNode.node(lst[0])
        p = self.head
        for i in lst[1:]:
            self.head = baseNode.node(i,self.head)
        print('反转前')
        baseNode.myprint(self.head)

    def reverse(self):
        p = self.head.next
        self.head.next = None
        while p is not None:
            q = p
            p = p.next
            q.next = self.head
            self.head = q
        return self.head

header = [1,2,3,4,5,6,7,8,9]

linkList = LinkList(header)
print('\n反转后的\n')
baseNode.myprint(linkList.reverse())