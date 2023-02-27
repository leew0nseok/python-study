class Node:
	def __init__(self, key=None, value=None, left=None, right=None):
		self.item = (key, value)
		self.left, self.right = left, right
	
	def key(self):
		return self.item[0]
	
	def value(self):
		return self.item[1]
	
	def set_value(self, value):
		self.item[1] = value

class BinarySearchTree:
	def __init__(self, root=None):
		self.root = root
	
	def search(self, key): # loop version
		root = self.root
		while root is not None:
			if key == root.key():
				break
			elif key < root.key():
				root = root.left
			elif key > root.key():
				root = root.right
		
		return root
	
	def search_p(self, key): 
		root, parent = self.root, None
		while root is not None:
			if key == root.key():
				break
			elif key < root.key():
				parent = root
				root = root.left
			elif key > root.key():
				parent = root
				root = root.right
		
		return root, parent
	
	def insert(self, key, value=None):
		node, p = self.search_p(key)
		if node is not None and k==node.key():
			node.set_value(value)
			return node
		
		new_node = Node(key, value)
		if p is None:
			self.root = new_node
		elif key < p.key():
			p.left = new_node
		else:
			p.right = new_node
		
		return node
	
	""" 
	replace <node> with <rep_node> 
	p: parent of <node>
	rep_p: parent of <rep_node>
	"""
	def replace(self, node, rep_node, p, rep_p): 
		
		# replace p-to-node link
		if p is None: self.root = rep_node
		elif node == p.right: p.right = rep_node
		else: p.left = rep_node
		
		# replace node-to-child(s) link(s)
		if rep_node is not None:
			if rep_p == node:
				if rep_node == node.right and node.left is not None:
					rep_node.left = node.left
			else:
				rep_node.left = node.left
				rep_node.right = node.right
		
		rep_p.left = None
			
	def find_min_p(self, root, p):
		while root.left is not None:
			p = root
			root = root.left
		return root, p
		
	def delete(self, key):
		node, p = self.search_p(key)
		if node is None:
			return node
		# number of children <= 1
		elif node.left is None or node.right is None:
			# determine the child (left or right?)
			child = node.left
			if node.right is not None: child = node.right
			# replace <node> with <child>
			self.replace(node, child, p, node)
		# number of children == 2
		else:
			# find minimum key from the right subtree
			right_min, right_min_p = self.find_min_p(node.right, node)
			# replace <node> with <right_min>
			self.replace(node, right_min, p, right_min_p)
			
		return node
	
	def preorder(self, root):
		if root is not None:
			print(root.key(), end=" ")
			self.preorder(root.left)
			self.preorder(root.right)
	
	def postorder(self, root):
		if root is not None:
			self.postorder(root.left)
			self.postorder(root.right)
			print(root.key(), end=" ")
	
	def inorder(self, root):
		if root is not None:
			self.inorder(root.left)
			print(root.key(), end=" ")
			self.inorder(root.right)
	

T = BinarySearchTree()
while True:
	cmd = input()
	if cmd == 'exit':
		break
	elif cmd == 'print':
		print('preorder:', end=" "); T.preorder(T.root); print();
		print('inorder :', end=" "); T.inorder(T.root); print();
	else:
		cmd = cmd.split()
		cmd, key = cmd[0], int(cmd[1])
		if cmd == 'find':
			node = T.search(key)
			if node is None:
				print('KEY:{} NOT FOUND'.format(key))
			else:
				print('KEY:{} FOUND'.format(key))
		elif cmd == 'in':
			node = T.insert(key)
		elif cmd == 'del':
			node = T.delete(key)

	