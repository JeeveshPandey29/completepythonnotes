# A Linked List is a collection of nodes. Each node contains:  Data (value) and Address of next node (pointer/reference)

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = Node(15)
node2 = Node(20)
node3 = Node(50)
node4 = Node(90)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1

current = head
while current:
    print (current.data, end="->")
    current = current.next
print("None")

#length of linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1

current = head
count = 0

while current:
    count+= 1
    current = current.next
print (count)


#search in a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1

current = head


target = 20

while current:
    if current.data == target:
        print("found")
        break
    current = current.next


#MIDDLE OF A LINKED LIST
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

#traversal of singly linked list 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traversal(head):
    while head is not None:
        print(head.data, end = "")
        if head.next is not None:
            print("->", end="")
        head = head.next
    print()

if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(10)
    head.next.next.next = Node(40)

    traversal(head)


#insettion of node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to insert at start
def insert_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node 

# Create linked list manually
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1

# Insert new node at start
head = insert_beginning(head, 5)

# Print the list to check insertion
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")


#insert node at the end of linkedlist

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to insert at end
def insert_end(head, data):
    new_node = Node(data)
    if head is None:   # if list is empty
        return new_node
    
    current = head
    while current.next:   # move till last node
        current = current.next
    current.next = new_node
    return head

# Create linked list manually
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1

# Insert new node at end
head = insert_end(head, 60)

# Print the list to check insertion
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")


#insert node at speicific position

class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

def insertPos(head, pos, val):
    if pos < 1:   # invalid position
        return head
    if pos == 1:  # insert at front
        newNode = Node(val)
        newNode.next = head
        return newNode
    
    curr = head
    for i in range(1, pos - 1):   # move to (pos-1)th node
        if curr is None:
            return head
        curr = curr.next
    
    if curr is None:   # position out of range
        return head
    
    newNode = Node(val)
    newNode.next = curr.next
    curr.next = newNode
    return head

def printList(head):
    curr = head
    while curr is not None:
        print(curr.val, end="")
        if curr.next is not None:
            print("->", end="")
        curr = curr.next
    print()

if __name__ == "__main__":
    # Initial list: 10->20->30->40->60
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(60)

    # Insert 50 at position 5 (before 60)
    head = insertPos(head, 5, 50)

    printList(head)

# Delete 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Delete first node
def delete_beginning(head):
    if head is None:   # empty list
        return None
    return head.next   # new head is the second node

# Delete last node
def delete_end(head):
    if head is None or head.next is None:
        return None    # empty list or single node
    current = head
    while current.next.next:   # stop at second last node
        current = current.next
    current.next = None        # remove last node
    return head

# Delete node at specific position (1-based index)
def delete_at_position(head, pos):
    if head is None:
        return None
    if pos == 1:   # delete head
        return head.next
    
    current = head
    for i in range(1, pos-1):
        if current is None or current.next is None:
            return head   # position out of range
        current = current.next
    
    # current is at (pos-1)th node
    if current.next:
        current.next = current.next.next
    return head

# --------------------------
# Create linked list manually
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1

# Delete first node
head = delete_beginning(head)

# Delete last node
head = delete_end(head)

# Delete node at position 2 (originally 30)
head = delete_at_position(head, 2)

# Print final list
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

'''
Remove Linked List Elements
'''
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        curr = dummy

        while curr.next:

            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next
            
# REVERSE A LINKED LIST
def reverseList(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev

'''
CYCLE IN LINKEDLIST: Store nodes in set.
visited = set()
If node repeats: return True 
Space = O(n)

FLOYD CYCLE DETECTION: SLOW FAST = 1, SLOW BY 1 AND FAST BY 2 IF THEY MEET ON SAME NODE CYCLE DETECTED.
'''

class Solution:
    def hasCycle(head) -> bool:
        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

'''
WHENEVER YOU SEE SLOW = HEAD AND FAST = HEAD THEN REMEMBER
Middle Node
Cycle Detection
Palindrome
Cycle Length
Cycle Start
'''

''' REMOVE DUPLICATES FROM SORTED LIST '''
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next

            else:
                current = current.next

        return head

# COUNT LENGTH OF CYCLE IN LINKEDLIST
def count_cycle_length(head):
    slow = head
    fast = head

    # Step 1: Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:  # cycle detected
            # Step 2: Count cycle length
            count = 1
            temp = slow.next
            while temp != slow:
                count += 1
                temp = temp.next
            return count
    return 0  # no cycle


# FIND STARTING POINT OF LOOOP IN LINKED LIST 142
def detectCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:   # cycle detected
            ptr1 = head
            ptr2 = slow

            while ptr1 != ptr2:
                ptr1 = ptr1.next
                ptr2 = ptr2.next

            return ptr1    # start of cycle

    return None            # no cycle


# palindrome linked list: middle find karo then middle sai half krdo left and rpev initialize kro dono values compare karo
class Solution:
    def isPalindrome(self, head):
        slow = head
        fast = head

        # Step 1: Find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # Step 3: Compare halves
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True


# REMOVE NTH NODE FROM END
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  
        fast = dummy
        slow = dummy

        for i in range(n+1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next
    
#INTERSECTION OF TWO LNKED LIST 
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()

        while headA:
            seen.add(headA)
            headA = headA.next

        while headB:
            if headB in seen:
                return headB
            headB = headB.next

        return None
    

