#list=[1,2,3,4,5,6,7]
#list.insert(3,100)

#print(list)

#search : O(1)
#insertion : O(n)
#deletion : O(n)


#Node: value, next-pointer
#[1]->[2]->[3]->[4]->[5]->[6]->[7]->None

class Node():
    def __init__(self,value):
        self.val = value
        self.next = None


Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node5 = Node(5)
Node6 = Node(6)
Node7 = Node(7)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5
Node5.next = Node6
Node6.next = Node7

def show(node):
    cur = Node1
    while cur:      #while cur != None:
        print(cur.val)
        cur=cur.next

show(1)