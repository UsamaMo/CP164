"""
-------------------------------------------------------
Linked version of the BST ADT - Exam
-------------------------------------------------------

-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from copy import deepcopy


class BST:

    def total_height(self):
        """
        ---------------------------------------------------------
        Returns the total heights of a bst.
        ---------------------------------------------------------
        Returns:
            the total height count - i.e. the sum of all the node heights
            in the tree (int)
        ---------------------------------------------------------
        """
        # the height is not needed, only total height is needed from the auxilary function of total height
        # total_height gives parent node to total_height_aux
        # thats why there is self._root is there below, because total height
        # has given parent node to total height aux
        _, total_height = self._total_height_aux(self._root)

        # return total height from auxilary method
        return total_height

    def _total_height_aux(self, node):
        """
        ---------------------------------------------------------
        Returns the total heights of a bst.
        ---------------------------------------------------------
        Parameters:
            node - a BST node (_BST_Node)
        Returns:
            total_height - the total height count - i.e. the sum of all the
            node heights in the tree (int)
        ---------------------------------------------------------
        """
        # initialize total height as 0 since BST is empty
        total_height = 0

        # if the parent node is none
        if node is None:
            # height is equal to 0 sinze the BST is empty
            height = 0
            # total height will also be 0 as there is no node in the BST
            total_height = 0

        else:
            # otherwise if the BST is not empty
            # uses a recursion here
            # height 1 and total height 1 are to the node on the left
            h1, th1 = self._total_height_aux(node._left)
            # height 2 and total height 2 are to the node at the right
            h2, th2 = self._total_height_aux(node._right)
            # height basically equals the height of the parent node
            # height equals the maximum between (height 1 and height 2) +1
            height = max(h1, h2) + 1
            # total height is equal to total height + th1 + th2 + height
            total_height += th1 + th2 + height

        # return both height and total_height
        return height, total_height

    def mirror(self):
        """
        ---------------------------------------------------------
        Changes the current BST into a mirror image of itself. All nodes
        are swapped with nodes on the other side of a tree. Nodes may take
        the place of an empty spot. The resulting tree is a mirror image
        of the original tree. (Note that the mirrored tree is not a BST.)
        Use: bst.mirror()
        ---------------------------------------------------------
        Returns​​‌‌​‌​​:
            None
        ---------------------------------------------------------
        """
        # tree variable is a BST
        tree = BST()

        # tree._root is a variable and it calls the auxilary function for
        # mirror, while using parent node
        tree._root = self._mirror_aux(self._root)
        return

    def _mirror_aux(self, N):
        """
        ---------------------------------------------------------
        Changes the current subtree into a mirror image of itself. All nodes
        are swapped with nodes on the other side of a tree. Nodes may take
        the place of an empty spot. The resulting subtree is a mirror image
        of the original subtree.
        Use: # your code here
        ---------------------------------------------------------
        Parameters:
            N
        Returns:
            N
        ---------------------------------------------------------
        """

        # when you do call a recursive function
        # it does the whole method

        # original mirror passes in parent node
        # so N = parent node at first case

        # if N is not empty (None)
        # if N exists
        if N != None:

            # if left node of N is not empty(None)
            # if left node exists

            # use this recursion
            # if left node is equal to None,stop loop,  goto to the next line
            if N._left != None:
                # call this axiliry function for just that left node
                # start this method again with left node
                # if left node exists, N will be this value
                self._mirror_aux(N._left)

            # if right node exists
            # if right node is equal to None ,stop loop,  goto the next line
            if N._right != None:
                # call this axuliary function for just that right node
                # start this method again with right node
                # if right node exists, N will be this value
                self._mirror_aux(N._right)

            # DO SWAP ALGORITHM:
                # STEPS for algorithm:
                # 1.set left node to temp
                # 2.put value of left node into temp
                # 3.put value of right node into left
                # 4. put value of temp into right node

            # set temperorary to left node
            temp = N._left
            # set left node to right node
            N._left = N._right
            # set right node to temp
            N._right = temp

        # algorithm for this method:
        # 1.insert parent node into this method
        # if parent node exists, goto the left node
        return N

    def _rotate_left(self, parent):
        """
        -------------------------------------------------------
        Rotates the parent node to its left around its right child.
        Updates the heights of the rotated nodes.
        Use: parent = self._rotate_left(parent)
        -------------------------------------------------------
        Parameters:
            parent - the pivot node to rotate around (_BST_Node)
        Returns​​‌‌​‌​​:
            updated - the node that replaces the parent node (_BST_Node)
        -------------------------------------------------------
        """

        if parent is None or parent._right is None:
            updated = self.parent
        else:
            temp = parent._right._left
            parent._right._left = None
            temp2 = parent
            parent = parent._right
            parent._left = temp2
            parent._left._right = temp
            updated = parent

        return updated

# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty BST.
        Use: bst = BST()
        -------------------------------------------------------
        Returns​​‌‌​‌​​:
            A BST object (BST)
        -------------------------------------------------------
        """
        self._root = None
        self._count = 0

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into bst. Values may appear
        only once in a tree.
        Use: b = bst.insert(value)
        -------------------------------------------------------
        Parameters:
            value - data to be inserted into bst (?)
        Returns​​‌‌​‌​​:
            inserted - True if value is inserted into bst,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        self._root, inserted = self._insert_aux(self._root, value)
        return inserted

    def _insert_aux(self, node, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into node.
        Private recursive operation called only by insert.
        Use: node, inserted = self._insert_aux(node, value)
        -------------------------------------------------------
        Parameters:
            node - a bst node (_BST_Node)
            value - data to be inserted into the node (?)
        Returns​​‌‌​‌​​:
            node - the current node (_BST_Node)
            inserted - True if value is inserted into node,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        if node is None:
            # Base case: add a new node containing the value.
            node = _BST_Node(value)
            self._count += 1
            inserted = True
        elif value < node._value:
            # General case: check the left subtree.
            node._left, inserted = self._insert_aux(node._left, value)
        elif value > node._value:
            # General case: check the right subtree.
            node._right, inserted = self._insert_aux(node._right, value)
        else:
            # Base case: value is already in the BST.
            inserted = False

        if inserted:
            # Update the node height if any of its children have been changed.
            node._update_height()
        return node, inserted

    def retrieve(self, key):
        """
        -------------------------------------------------------
        Retrieves a copy of a value matching key in bst. (Iterative)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns​​‌‌​‌​​:
            value - value in the node containing key, otherwise None (?)
        -------------------------------------------------------
        """
        node = self._root
        value = None

        while node is not None and value is None:

            if node._value > key:
                node = node._left
            elif node._value < key:
                node = node._right
            elif node._value == key:
                # for comparison counting
                value = deepcopy(node._value)
        return value

    def inorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in inorder order.
        Use: a = bst.inorder()
        -------------------------------------------------------
        Returns​​‌‌​‌​​:
            a - copy of the contents of the tree in inorder (list of ?)
        -------------------------------------------------------
        """
        a = []
        self._inorder_aux(self._root, a)
        return a

    def _inorder_aux(self, node, a):
        """
        ---------------------------------------------------------
        Traverses node subtree in inorder. a contains the contents of
        node and its children in inorder.
        Private recursive operation called only by inorder.
        Use: self._inorder_aux(node, a)
        ---------------------------------------------------------
        Parameters:
            node - an BST node (_BST_Node)
            a - target list of data (list of ?)
        Returns​​‌‌​‌​​:
            None
        ---------------------------------------------------------
        """
        if node is not None:
            self._inorder_aux(node._left, a)
            a.append(deepcopy(node._value))
            self._inorder_aux(node._right, a)
        return

    def preorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in preorder order.
        Use: a = bst.preorder()
        -------------------------------------------------------
        Returns​​‌‌​‌​​:
            a - copy of the contents of the tree in preorder (list of ?)
        -------------------------------------------------------
        """
        a = []
        self._preorder_aux(self._root, a)
        return a

    def _preorder_aux(self, node, a):
        """
        ---------------------------------------------------------
        Traverses node subtree in preorder. a contains the contents of
        node and its children in preorder.
        Private recursive operation called only by preorder.
        Use: self._preorder_aux(node, a)
        ---------------------------------------------------------
        Parameters:
            node - an BST node (_BST_Node)
            a - target of data (list of ?)
        Returns​​‌‌​‌​​:
            None
        ---------------------------------------------------------
        """
        if node is not None:
            a.append(deepcopy(node._value))
            self._preorder_aux(node._left, a)
            self._preorder_aux(node._right, a)
        return

    def _node_height(self, node):
        """
        ---------------------------------------------------------
        Helper function to determine the height of node - handles empty node.
        Private operation called only by _is_valid_aux.
        Use: h = self._node_height(node)
        ---------------------------------------------------------
        Parameters:
            node - the node to get the height of (_BST_Node)
        Returns​​‌‌​‌​​:
            height - 0 if node is None, node._height otherwise (int)
        ---------------------------------------------------------
        """
        if node is None:
            height = 0
        else:
            height = node._height
        return height

    def is_valid(self):
        """
        ---------------------------------------------------------
        Determines if a tree is a is_valid BST, i.e. the values in all left nodes
        are smaller than their parent, and the values in all right nodes are
        larger than their parent, and height of any node is 1 + max height of
        its children.
        Use: b = bst.is_valid()
        ---------------------------------------------------------
        Returns​​‌‌​‌​​:
            valid - True if tree is a BST, False otherwise (boolean)
        ---------------------------------------------------------
        """
        valid = self._is_valid_aux(self._root, None, None)
        return valid

    def _is_valid_aux(self, node, min_node, max_node):
        """
        ---------------------------------------------------------
        Private recursive method to determine the BST validity of node,
        used only by is_valid.
        Use: valid = self._is_valid_aux(node, min_node, max_node)
        ---------------------------------------------------------
        Parameters:
            node - a binary tree node (_BST_Node)
            min_node - the node with the minimum value for the current tree (_BST_Node)
            max_node - the node with the maximum value for the current tree (_BST_Node)
        Returns​​‌‌​‌​​:
            valid - True if node is root of a valid BST, False otherwise (boolean)
        ---------------------------------------------------------
        """
        if node is None:
            valid = True
        elif min_node is not None and node._value <= min_node._value:
            # print("BST left value violation at value: {}".format(node._value))
            valid = False
        elif max_node is not None and node._value >= max_node._value:
            # print("BST right value violation at value: {}".format(node._value))
            valid = False
        elif node._height != max(self._node_height(node._left), self._node_height(node._right)) + 1:
            # print("BST height violation at value: {}".format(node._value))
            valid = False
        else:
            # node becomes max node of left tree, min node of right tree
            valid = self._is_valid_aux(node._left, min_node, node) \
                and self._is_valid_aux(node._right, node, max_node)
        return valid


class _BST_Node:

    def __init__(self, value):
        """
        -------------------------------------------------------
        Initializes a BST node containing value. Child pointers
        are None, height is 1.
        Use: node = _BST_Node(value)
        -------------------------------------------------------
        Parameters:
            value - value for the node (?)
        Returns​​‌‌​‌​​:
            A _BST_Node object (_BST_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._left = None
        self._right = None
        self._height = 1
        self._count = 0

    def _update_height(self):
        """
        -------------------------------------------------------
        Updates the height of the current node. _height is 1 plus
        the maximum of the node's (up to) two child heights.
        Use: node._update_height()
        -------------------------------------------------------
        Returns​​‌‌​‌​​:
            None
        -------------------------------------------------------
        """
        if self._left is None:
            left_height = 0
        else:
            left_height = self._left._height

        if self._right is None:
            right_height = 0
        else:
            right_height = self._right._height

        self._height = max(left_height, right_height) + 1
        return

    def __str__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Returns node height and value as a string - for debugging.
        -------------------------------------------------------
        """
        return f"h: {self._height}, v: {self._value}"
