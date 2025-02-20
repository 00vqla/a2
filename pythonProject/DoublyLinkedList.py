class Node:

    def __init__(self, data):
        # To store the value or data
        self.data = data

        # Reference to the previous node
        self.prev = None

        # Reference to the next node
        self.next = None


def Forward_Traversal(head):

    # Start traversal from the head of the list
    curr = head

    # Continue until the current node is null (end of the list)
    while curr is not None:

        # Output the data of current node
        print(curr.data, end="")

        # Move to the next node
        curr = curr.next

    print()


def Backward_Traversal(tail):

    curr = tail

    # Continue until the current node is null (the end of the list)
    while curr is not None:

        # Output data of the current node
        print(curr.data, end="")

        # Move to the previous node
        curr = curr.prev

    # Print newline after traversal
    print()


def find_length(head):
    count = 0
    curr = head
    while curr is not None:
        count += 1
        curr = curr.next
    return count


def InsertBegin(head, data):

    # Create a new node
    new_node = Node(data)

    # Make next of it sa head
    new_node.next = head

    # Set previous of head as new node
    if head is not None:
        head.prev = new_node

    # Return new node as new head
    return new_node

# Sample usage


if __name__ == "__main__":

    # Create a doubly linked list with 3 nodes
    head = Node(1)
    second = Node(2)
    third = Node(3)

    head.next = second
    second.prev = head
    second.next = third
    third.prev = second

    print("Forward Traversal:")
    Forward_Traversal(head)

    print("Backward Traversal:")
    Backward_Traversal(third)

    print("Length of the list: " + str(find_length(head)))

    head = InsertBegin(head, 1)


def insertPos(head, pos, data):
    if pos < 1:
        print("Invalid position")
        return head

    if pos == 1:
        new_node = Node(data)
        new_node.next = head
        return new_node

    # Traverse the list to find the nodes before the insertion point
    prev = head
    count = 1
    while count < pos - 1 and prev is not None:
        prev = prev.next
        count += 1

    # If position > number of nodes
    if prev is None:
        print("Invalid position")
        return head

    # Insert the new node @specific position
    new_node = Node(data)
    new_node.next = prev.next
    prev.next = new_node

    return head


