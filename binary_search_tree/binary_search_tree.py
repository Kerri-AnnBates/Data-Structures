from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.root = None

    # Insert the given value into the tree
    def insert(self, value):

        # Check if node is empty
        if self.value is None:
            self.value = value
        else:
            # check if value is less than node
            if value < self.value:
                # set the current node to the left node
                if self.left is None:
                    self.left = BinarySearchTree(value)
                else:
                    # repeat
                    self.left.insert(value)
            elif value >= self.value:
                # set the current node to the right node
                if self.right is None:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if node is none
        if self.value is None:
            # return false
            return False

        # if node.value == findvalue
        if self.value == target:
            # return true
            return True
        # else
        else:
            # if find <  node.value
            if target < self.value:
                # find on left node
                if self.left is not None:
                    return self.left.contains(target)
                else:
                    return False
            # else
            else:
                # find on right node
                if self.right is not None:
                    return self.right.contains(target)
                else:
                    return False

    # Return the maximum value found in the tree
    def get_max(self):
        max_val = self.value

        # if there's a right:
        if self.right is None:
            return max_val

        # get max on right
        max_val = self.right.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        # 1. Visit the root.
        # # run the cb function on the value
        cb(self.value)

        # 2. Traverse the left subtree
        if self.left:
            self.left.for_each(cb)
        # 3. Traverse the right subtree
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
