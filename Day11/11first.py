nodes = {}

class Node:
  def __init__(self, childrenNames):
    self.children = childrenNames
    self.pathsToOut = -1

  def getChildren(self):
    return [nodes[childName] for childName in self.children]
  
  def setPathsToOut(self, pathsToOut):
    self.pathsToOut = pathsToOut

  def getPathsToOut(self):
    return self.pathsToOut

you = None
out = Node([])
out.setPathsToOut(1)
nodes["out"] = out
with open("input.txt") as fIn:
  for line in fIn:
    line = line.strip()
    nodeName, outputs = line.split(": ")
    outputs = outputs.split(' ')
    nodes[nodeName] = Node(outputs)
    if nodeName == "you":
      you = nodes[nodeName]

stack = [you]
while len(stack) > 0:
  node = stack.pop()
  if node.getPathsToOut() != -1:
    continue
  # Recheck after children have been checked
  stack.append(node)
  # Check all children
  children = node.getChildren()
  numPaths = 0
  uncheckedChild = False
  for child in children:
    if child.getPathsToOut() == -1:
      # Add child to be checked
      stack.append(child)
      uncheckedChild = True
    else:
      # Child has num paths to out already
      numPaths += child.getPathsToOut()
  if not uncheckedChild:
    node.setPathsToOut(numPaths)

print(you.getPathsToOut())

