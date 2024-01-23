from collections import deque

class BSTNode:
    def __init__(self, key, left=None, right=None):
        self._key = key
        self._left = left
        self._right = right

class BST:
    def __init__(self):
        self._root = None
        self._count = 0
    
    def insert(self, key):
        newNode = BSTNode(key)
        if self._root is None:
            self._root = newNode
        else:
            self._insert(key, self._root)
        self._count += 1
    
    def _insert(self, key, root:BSTNode):
        if key < root._key:
            if root._left:
                self._insert(key, root._left)
            else:
                root._left = BSTNode(key)
        else:
            if root._right:
                self._insert(key, root._right)
            else:
                root._right = BSTNode(key)

    def get_height(self):
        if self._root is None:
            return 0
        return self._get_height(self._root)

    def _get_height(self, node:BSTNode):
        if node is None:
            return 0
        else:
            return 1 + max(self._get_height(node._left),self._get_height(node._right))

    def get_min(self):
        curr = self._root
        while curr._left is not None:
            curr = curr._left
        return curr._key
    
    def get_max(self):
        curr = self._root
        while curr._right is not None:
            curr = curr._right
        return curr._key

    def print_values(self):
        if self._root is None:
            return
        
        Queue = deque()
        Queue.append(self._root)
        
        while len(Queue) > 0:
            current_node = Queue.popleft()
            print(current_node._key, end=' ')
            
            if current_node._left:
                Queue.append(current_node._left)
            
            if current_node._right:
                Queue.append(current_node._right)
        print('')

    def get_count(self):
        return self._count
    
    def delete_value(self, value):
        if self._root:
            self._root = self._delete_value(value, self._root)
            self._count -= 1
        else:
            return -1
    
        """
        The function `_delete_value` is used to delete a node with a specific value from a binary search
        tree.
        
        :param value: The value is the key of the node that needs to be deleted from the binary search
        tree
        :param node: The parameter "node" represents a node in a binary search tree (BST)
        :type node: BSTNode
        :return: the updated node after deleting the specified value from the binary search tree.
        """
    def _delete_value(self, value, node:BSTNode):
        if node is None:
            return None
        if value < node._key:
            node._left=self._delete_value(value, self._node._left)
        elif value > node._key:
            node._right = self._delete_value(value, self._node._right)
        else:
            if node._left is None:
                return node._right
            elif node._right is None:
                return node._left
              # Case 2: Node with two children
            # Find the inorder successor (smallest node in the right subtree)
            successor = self._find_min(node._right)
            
            # Copy the inorder successor's key to this node
            node._key = successor._key
            
            # Delete the inorder successor
            node._right = self._delete_value(successor._key, node._right)
        
        return node

    def _find_min(self, node: BSTNode):
        while node._left:
            node = node._left
        return node

tree = BST()
tree.insert(5)
tree.insert(4)
tree.insert(6)
tree.insert(1)
print(tree.get_height())
    