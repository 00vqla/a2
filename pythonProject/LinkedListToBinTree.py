class Conversion:

    # Storing head of linked list and root for the Bin tree
    def __init__(self, data = None):
        self.head = None
        self.root = None

    def push(self, new_data):

        # New linked list node and storing data
        new_node = ListNode(new_data)

        # Next of new node as head
        new_node.next = self.head

        # Move the head to point tot new node
        self.head = new_node

    def convertList2Binary(self):

        # Queue to store the parent nodes
        q = []

        # Base C