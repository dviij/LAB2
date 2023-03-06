class Bintree:
	def __init__(self, x):
		self.left = None
		self.right = None
		self.data = x

	def insert(self, x):
		if self.data:
			if x < self.data:
				if self.left is None:
					self.left = Bintree(x)
				else:
					self.left.insert(x)
			elif x > self.data:
				if self.right is None:
					self.right = Bintree(x)
				else:
					self.right.insert(x)
			else:
				self.data = x

def Inorder(root):
	if root:
		Inorder(root.left)
		print(root.data, end=" ")
		Inorder(root.right)

def Preorder(root):
	if root:
		print(root.data, end=" ")
		Preorder(root.left)
		Preorder(root.right)

def Postorder(root):
	if root:
		Postorder(root.left)
		Postorder(root.right)
		print(root.data, end=" ")

if __name__ == "__main__":
	root = Bintree(25)
	root.insert(15)
	root.insert(10)
	root.insert(4)
	root.insert(12)
	root.insert(22)
	root.insert(18)
	root.insert(24)
	root.insert(35)
	root.insert(31)
	root.insert(44)
	root.insert(50)
	root.insert(70)
	root.insert(66)
	root.insert(90)

	print("inorder", end=" ")
	Inorder(root)
	print("\nPreorder", end=" ")
	Preorder(root)
	print("\nPostorder", end=" ")
	Postorder(root)
