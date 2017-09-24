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
            # TODO

    def right_rotate(self, parent, child):
        """ 15
           /
          10
         /   \
        /     12
      9     /   \
          11    14


        """
        right = child.right
        child.right = right.left
        if parent.right == child:
            parent.right = right
        elif parent.left == child:
            parent.left = right
        right.left = child

    def left_rotate(self, parent, child):
        """
            15
            /
         10
        /  \
    7      11
  / \
 6   9
      """
        left = child.left
        child.left = left.right
        if parent.right == child:
            parent.right = left
        elif parent.left == child:
            parent.left = child
        left.right = child

    def find(self, node):
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
        if self.root.find(value):
            # TODO
            return True
        return False


def from_sorted_list_to_balanced_tree(array):
    array_len = len(array)
    parent = AVLNode(array[array_len // 2])
    if array_len // 2 > 0:
        parent.left = from_sorted_list_to_balanced_tree(array[:array_len // 2])
    if array_len - (array_len // 2 + 1) > 0:
        parent.right = from_sorted_list_to_balanced_tree(array[array_len // 2 + 1:])
    return parent
