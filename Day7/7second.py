class Node:
  # left: Node
  # right: Node
  # paths: int

  def __init__(self):
    self.left = None
    self.right = None
    self.paths = None

  def getLeft(self):
    return self.left
  
  def getRight(self):
    return self.right

  def setLeft(self, other):
    self.left = other

  def setRight(self, other):
    self.right = other

  def setPaths(self, paths):
    self.paths = paths

  def getPaths(self):
    return self.paths

tree: Node = None
marks: dict[int, Node] = {}
total = 0
with open("input.txt") as fIn:
  line: str = fIn.readline()
  for i, char in enumerate(line):
    if char == 'S':
      tree = Node()
      marks[i] = tree
  for line in fIn:
    line = line.strip()
    for i, char in enumerate(line):
      if char == '^' and marks.get(i, False):
        if i != 0:
          if marks.get(i-1, False):
            marks[i].setLeft(marks[i-1])
          else:
            leftNode = Node()
            marks[i-1] = leftNode
            marks[i].setLeft(leftNode)
        if i != len(line) - 1:
          if marks.get(i+1, False):
            marks[i].setRight(marks[i+1])
          else:
            rightNode = Node()
            marks[i+1] = rightNode
            marks[i].setRight(rightNode)
        marks.pop(i)

stack = [tree]
while len(stack) != 0:
  node = stack.pop()
  if (node.getLeft() is not None and node.getLeft().getPaths() is None) or (node.getRight() is not None and node.getRight().getPaths() is None):
    stack.append(node)
    if (node.getLeft() is not None and node.getLeft().getPaths() is None):
      stack.append(node.getLeft())
    if (node.getRight() is not None and node.getRight().getPaths() is None):
      stack.append(node.getRight())
  else:
    if (node.getLeft() is None and node.getRight() is None):
      node.setPaths(1)
    else:
      paths = 0
      if (node.getLeft() is not None):
        paths += node.getLeft().getPaths()
      if (node.getRight() is not None):
        paths += node.getRight().getPaths()
      node.setPaths(paths)
  
print(tree.getPaths())
