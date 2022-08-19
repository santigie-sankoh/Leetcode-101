class LinkedList():
    def __init__(self):
        self.start_node = None
        #this is for traversing
        
    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
        return
    else:
        n = self.start_node
        while n is not None:
            print(n.item , " ")
            n = n.ref
