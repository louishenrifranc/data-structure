class AVLNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.max_depth = 0

    def insert(self, value):
        insert_leaf = False
        # Insert node
        if self.value > value:
            if self.left is None:
                self.left = AVLNode(value)
                insert_leaf = True
            else:
                self.left.insert(value)
        elif self.value < value:
            if self.right is None:
                self.right = AVLNode(value)
                insert_leaf = True
            else:
                self.right.insert(value)

        # Update max_depth
        if insert_leaf:
            self.max_depth = max(self.max_depth, 1)
        else:
            max_depth = self.max_depth
            if self.right is not None:
                max_depth = max(max_depth, self.right.max_depth + 1)
            if self.left is not None:
                max_depth = max(max_depth, self.left.max_depth + 1)
            self.max_depth = max_depth

        # Balance tree

    def right_rotate(self, parent, child):
        

    def left_rotate(self, parent, child):
        pass

    def find(self, node) -> AVLNode:
        pass


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # Check if node is empty
        # Add value to the root node
        if self.root is None:
            self.root = AVLNode(value)
        else:
            if self.root.find(value) is None:
                self.root.insert(value)

    def remove(self, value):
        # Check if node is empty
        # Remove value from the root node
        pass
