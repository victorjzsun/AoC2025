import re
import functools
import math

def switchesToString(switches):
  return ",".join(str(x) for x in switches)

def checkSwitches(start, switches, memo={}):
  if (start, switchesToString(switches)) in memo:
    return memo[(start, switchesToString(switches))]
  if start == 0:
    return 0
  if len(switches) == 0:
    return None
  minPath = math.inf
  for i in range(len(switches)):
    newStart = start ^ switches[i]
    newPath = checkSwitches(newStart, switches[:i] + switches[i+1:], memo)
    if newPath is not None and newPath + 1 < minPath:
      minPath = newPath + 1
  memo[(start, switchesToString(switches))] = minPath
  return minPath

total = 0
lineCount = 0
with open("input.txt") as fIn:
  for line in fIn:
    lineCount += 1
    line = line.strip()

    # Get start
    match = re.match("\[((\.|#)+)\]", line)
    start = "".join(["1" if x == "#" else "0" for x in match.group(1)])
    # print("Start in binary string: " + start)
    length = len(start)
    start = int(start, 2)
    # print("Start in indices: " + str([i for i in range(length) if bin(start)[2:].rjust(length, "0")[i]=="1"]))

    # Get switches
    switches = [functools.reduce(lambda acc,ele: (acc[:int(ele)] + "1" + acc[int(ele)+1:]), re.findall("\d+", x), "0"*length) for x in re.findall("\([\d,]+\)", line)]
    # print("switches as binary strings: " + str(switches))
    switches = [int(x, 2) for x in switches]
    # print("switches as indices: " + " ".join([str(tuple([i for i in range(length) if bin(switches[j])[2:].rjust(length, "0")[i]=="1"])) for j in range(len(switches))]))

    # Get min path
    total += checkSwitches(start, switches)

print(total)