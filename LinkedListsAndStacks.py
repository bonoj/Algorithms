class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def getLastElem(self):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            return current

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        i = 1
        if position < 1:
            return None
        if self.head:
            while current.next and i < position:
                current = current.next
                i += 1
            if i == position:
                return current
            else:
                return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head
        i = 1
        if position > 1:
            while current and i < position:
                if i == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                i += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def insert_first(self, new_element):
        # current = self.head
        # while current:
        # current.next = current
        # current = new_element
        new_element.next = self.head
        self.head = new_element

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

    # def delete_first(self):
    #     "Delete the first (head) element in the LinkedList and return it"
    #     oldHead = self.head
    #     current = self.head
    #     self.head = current.next
    #     while current:
    #         if (current.next != None):
    #             current = current.next
    #     return oldHead

    # def delete_first(self):
    #     if self.head:
    #         deleted_element = self.head
    #         temp = deleted_element.next
    #         self.head = temp
    #         return deleted_element
    #     else:
    #         return None

    def delete_first(self):
        deleted = self.head
        if self.head:
            self.head = self.head.next
            deleted.next = None
        return deleted

# # print(linkedList.head.value)
# #
# # print(linkedList.getLastElem().value)
# # print(linkedList.get_position(4).value)
# #
# # linkedList.delete(5)
# # print(linkedList.get_position(5).next)
# # print(linkedList.get_position(5).value)
#
# headElem = Element(1)
# linkedList = LinkedList(headElem)
#
# linkedList.append(Element(3))
# linkedList.append(Element(4))
# linkedList.append(Element(5))
# linkedList.insert(Element(2), 2)
#
# i = 1
# while i <= 5:
#     print(linkedList.get_position(i).value)
#     i += 1

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(5)
e6 = Element(6)
e7 = Element(7)

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()

stack = Stack(e1)
# print(stack.ll.head.value)
stack.push(e2)
# print(stack.ll.head.value)
stack.push(e3)
# print(stack.ll.head.value)
stack.push(e4)
stack.push(e5)
stack.push(e6)
stack.push(e7)



# poppedElem = stack.pop()
# print(poppedElem.value)
# poppedElem = stack.pop()
# print(poppedElem.value)
# poppedElem = stack.pop()
# print(poppedElem.value)
# poppedElem = stack.pop()
# print(poppedElem.value)
# poppedElem = stack.pop()
# print(poppedElem.value)
# poppedElem = stack.pop()
# print(poppedElem.value)
# poppedElem = stack.pop()
# print(poppedElem.value)


i = 1
while i <= 7:
    print(stack.ll.get_position(i).value)
    i += 1

