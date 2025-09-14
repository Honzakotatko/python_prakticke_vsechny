# Definice uzlu
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Binární strom
class BinaryTree:
    def __init__(self):
        self.root = None

    # Přidání prvku (rekurzivně)
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(current.right, value)

    # Inorder průchod (levý, kořen, pravý)
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    # Preorder průchod (kořen, levý, pravý)
    def preorder(self, node):
        if node is not None:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # Postorder průchod (levý, pravý, kořen)
    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")
            
strom = BinaryTree()
strom.insert(5)
strom.insert(8)
strom.insert(1)
strom.insert(4)
strom.insert(6)
strom.insert(7)

print("\nInorder")
strom.inorder(strom.root)
print("\nPreorder")
strom.preorder(strom.root)
print("\nPostorder")
strom.postorder(strom.root)