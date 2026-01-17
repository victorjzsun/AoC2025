import re
import functools

def applySwitches(start, switches):
  '''
  XORs all switches with start and checks if result is 0
  '''
  myStart = 0
  for switch in switches:
    myStart ^= switch
  return start == myStart

def checkAll(epoch, start, switches, length):
  """
  Checks all combinations of switches of size epoch to see if any of them when applied to start result in 0.
  If found, returns the epoch and the indices of the switches used.
  If epoch > half of number of switches, checks the combinations of size len(switches)-epoch instead and returns the complement indices. This is to reduce the number of combinations checked.
  
  :param epoch: the number of switches to use
  :param start: the starting configuration
  :param switches: the list of all switches
  :param length: the length of start in bits
  :return: (epoch, list of indices of switches used) if found, else (None, None)
  """
  numSwitches = len(switches)
  flipped = False
  if epoch > (len(switches) // 2):
    flipped = True
    epoch = len(switches) - epoch
  indicesAsNum = -1
  end = len(switches) ** epoch
  while indicesAsNum != end:
    indicesAsNum += 1
    indices = unIntWithPadding(indicesAsNum, numSwitches, epoch)
    # print(indices)
    # print(["".join([str(x) for x in unIntWithPadding(switches[i],2, length)]) for i in range(numSwitches) if i not in indices])
    if applySwitches(start, (
      [switches[i] for i in indices]
      if not flipped else
      [switches[i] for i in range(numSwitches) if i not in indices]
    )):
      resultIndices = indices
      if flipped:
        resultIndices = [i for i in range(numSwitches) if i not in indices]
        epoch = numSwitches - epoch
      return epoch, resultIndices
  return None, None

def unInt(n, base):
  """
  Converts integer n to a list of digits in base 'base'.
  
  :param n: Description
  :param base: Description
  """
  if n < base:
    return [n]
  return unInt(n // base, base) + [n % base]

def unIntWithPadding(n, base, length):
  """
  Converts integer n to a list of digits in base 'base', with padding of 0s on the left to a specific length.
  
  :param n: the integer to convert
  :param base: the base to convert to
  :param length: the desired length of the output list
  :return: list of digits in base 'base' with padding
  """
  s = unInt(n,base)
  if len(s) < length:
    s = [0] * (length - len(s)) + s
  return s

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

    # Try all combinations of switches
    for epoch in range(1, len(switches)):
      result, indices = checkAll(epoch, start, switches, length)
      if result is not None:
        total += result
        break
    else:
      if not applySwitches(start, switches):
        raise Exception("using all switches didn't work")
      else:
        total += len(switches)
    print(f"Line {str(lineCount)} indices {indices}")

print(total)
"""
[0, 1, 2, 3, 4, 5, 7, 8]

(0,1,2,4,5,6,7,8)
(1,2)
(1,4,5)
(0,6)
(0,2,6,8,9)
(0,1,5,7,8)
(3,9)
(1,3,4,5,6,7,8,9)

0123456789
.##.#..#.#
.####..#.#

(0,1,3,4,7,8)
(2,3,4,5,7,8) (0,1,2,5,6,7,8) (0,1,3,4,5,6,8) (0,1,2,4,5,6)
(3,6,7)
..#......
"""