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

with open("input.txt") as fIn:
  for line in fIn:
    line = line.strip()
    nodeName, outputs = line.split(": ")
    outputs = outputs.split(' ')
    nodes[nodeName] = Node(outputs)

svr = nodes["svr"]
dac = nodes["dac"]
fft = nodes["fft"]
out = Node([])
out.setPathsToOut(1)
nodes["out"] = out

def calcPaths(start, end):
  stack = [start]
  paths = {end: 1}
  while len(stack) > 0:
    node = stack.pop()
    if node in paths:
      continue
    # Recheck after children have been checked
    stack.append(node)
    # Check all children
    children = node.getChildren()
    numPaths = 0
    uncheckedChild = False
    for child in children:
      if child not in paths:
        # Add child to be checked
        stack.append(child)
        uncheckedChild = True
      else:
        # Child has num paths to out already
        numPaths += paths[child]
    if not uncheckedChild:
      paths[node] = numPaths
  return paths[start]

total = 0
part1 = calcPaths(svr, dac)
part2 = calcPaths(dac, fft)
part3 = calcPaths(fft, out)
if part1 and part2 and part3:
  total += part1 * part2 * part3

part1 = calcPaths(svr, fft)
part2 = calcPaths(fft, dac)
part3 = calcPaths(dac, out)
if part1 and part2 and part3:
  total += part1 * part2 * part3
print(total)

