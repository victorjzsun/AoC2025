import math
import heapq
from functools import reduce

def distance(node1, node2):
  return math.sqrt((node1[0]-node2[0])**2 + (node1[1]-node2[1])**2 + (node1[2]-node2[2])**2)

circuitCount = 0
circuits = {}
nodeToCircuits = {}
nodes = []
with open("input.txt") as fIn:
  for line in fIn:
    nodes.append(tuple(map(int, line.strip().split(","))))

distances = []
for i in range(len(nodes)):
  for j in range(i + 1, len(nodes)):
    distances.append((distance(nodes[i], nodes[j]), (i, j)))

distances.sort(key=lambda x: x[0])

distancesToConsider = 1000
heap = []
for nextDistance in distances:
  if len(heap) < distancesToConsider:
    heapq.heappush(heap, (-nextDistance[0], nextDistance[1]))
  elif nextDistance < heap[0]:
    heapq.heappush(heap, (-nextDistance[0], nextDistance[1]))
    heapq.heappop(heap)

heap = [(-x[0], x[1]) for x in heap]
heapq.heapify(heap)
while len(heap) > 0:
  nextDistance = heapq.heappop(heap)
  nextNodes = nextDistance[1]
  if nextNodes[0] in nodeToCircuits:
    if nextNodes[1] in nodeToCircuits:
      firstNodeCircuitNum = nodeToCircuits[nextNodes[0]]
      secondNodeCircuitNum = nodeToCircuits[nextNodes[1]]
      if (firstNodeCircuitNum == secondNodeCircuitNum):
        continue
      firstNodeCircuit = circuits[firstNodeCircuitNum]
      secondNodeCircuit = circuits[secondNodeCircuitNum]
      for node in secondNodeCircuit:
        nodeToCircuits[node] = firstNodeCircuitNum
      firstNodeCircuit += secondNodeCircuit
      del circuits[secondNodeCircuitNum]
    else:
      firstNodeCircuitNum = nodeToCircuits[nextNodes[0]]
      firstNodeCircuit = circuits[firstNodeCircuitNum]
      nodeToCircuits[nextNodes[1]] = firstNodeCircuitNum
      firstNodeCircuit.append(nextNodes[1])
  else:
    if nextNodes[1] in nodeToCircuits:
      secondNodeCircuitNum = nodeToCircuits[nextNodes[1]]
      secondNodeCircuit = circuits[secondNodeCircuitNum]
      nodeToCircuits[nextNodes[0]] = secondNodeCircuitNum
      secondNodeCircuit.append(nextNodes[0])
    else:
      circuits[circuitCount] = [nextNodes[0], nextNodes[1]]
      nodeToCircuits[nextNodes[0]] = circuitCount
      nodeToCircuits[nextNodes[1]] = circuitCount
      circuitCount += 1

totals = []
for key in circuits.keys():
  totals.append(len(circuits[key]))

totals.sort()

print(reduce(lambda x,y: x*y, totals[-3:]))
  


