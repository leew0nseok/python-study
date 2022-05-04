class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item, self.left, self.right = item, left, right


def preorder(root):
    if root is not None:
        print(root.item, end=" ")
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    pass


def postorder(root):
    pass


def search(root, x):
    if root is None:
        return None
    if root.item == x:
        return root
    node = None
    if root.left:
        node = search(root.left, x)
    if node is not None:
        return node
    if root.right:
        node = search(root.right, x)
        return node


def insert_simple(p, side, x):
    global root
    if root is None:
        root = Node(x)
    else:
        node_p = search(root, p)
        if node_p is None:
            return None
        if side == 'left':
            node_p.left = Node(x)
        else:
            node_p.right = Node(x)


def size(root):
    if root is None:
        return 0
    else:
        return 1 + size(root.left) + size(root.right)


def height(root):
    return 0


root = None

while True:
    cmd = input()
    if cmd == 'exit':
        break
    elif cmd == 'preorder':
        preorder(root)
        print()
    elif cmd == 'postorder':
        postorder(root)
        print()
    elif cmd == 'inorder':
        inorder(root)
        print()
    elif cmd == 'size':
        print(size(root))
    elif cmd == 'height':
        print(height(root))
    else:
        cmd = cmd.split()
        if cmd[0] == 'search':
            val = cmd[1]
            node = search(root, int(val))
            if node is None:
                print(val+' not found')
            else:
                print(val+' found')
        elif cmd[0] == 'insert':
            p, side, val = cmd[1:]
            insert_simple(int(p), side, int(val))
