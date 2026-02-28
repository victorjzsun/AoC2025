import re
import functools

def make_dp_array(num_buttons):
  if num_buttons == 0:
    return None
  return [make_dp_array(num_buttons) for _ in range(2)]

def get_value_at_button_index(index, dp_array):
  if len(index) == 0:
    return dp_array
  if index[0] == "0":
    return get_value_at_button_index[index[1:], dp_array[0]]
  else:
    return get_value_at_button_index[index[1:], dp_array[1]]

def set_value_at_button_index(index, dp_array, val):
  if len(index) == 1:
    if index[0] == "0":
      dp_array[0] = val
    else:
      dp_array[1] = val
    return
  if index[0] == "0":
    return set_value_at_button_index[index[1:], dp_array[0], val]
  else:
    return set_value_at_button_index[index[1:], dp_array[1], val]

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
  
def populate_dp_array(length, dp_array, switches):
  for i in range(2 ** length):
    index = unIntWithPadding(i, 2, length)
    val = get_value_at_button_index(index, dp_array)
    for switch in switches:
      nextIndex = unIntWithPadding(i ^ switch)
      origVal = get_value_at_button_index(nextIndex, dp_array)
      set_value_at_button_index(nextIndex, dp_array, min(origVal, val + 1))

# def populate_dp_array(length, dp_array, switches, queue: list = [0]):
#   while len(queue):
#     i = queue.pop()
#     index = unIntWithPadding(i, 2, length)
#     val = get_value_at_button_index(index, dp_array)
#     for switch in switches:
#       nextIndex = unIntWithPadding(i ^ switch)
#       origVal = get_value_at_button_index(nextIndex, dp_array)
#       if (origVal is None):
#         set_value_at_button_index(nextIndex, dp_array, val + 1)
#         queue.append(i ^ switch)
#       elif (origVal > val + 1):
#         set_value_at_button_index(nextIndex, dp_array, val + 1)
#         queue.append(i ^ switch)

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
    # start = int(start, 2)
    # print("Start in indices: " + str([i for i in range(length) if bin(start)[2:].rjust(length, "0")[i]=="1"]))

    dp_array = make_dp_array(length)
    set_value_at_button_index("0" * length, dp_array, 0)

    # Get switches
    switches = [functools.reduce(lambda acc,ele: (acc[:int(ele)] + "1" + acc[int(ele)+1:]), re.findall("\d+", x), "0"*length) for x in re.findall("\([\d,]+\)", line)]
    # print("switches as binary strings: " + str(switches))
    switches = [int(x, 2) for x in switches]
    # print("switches as indices: " + " ".join([str(tuple([i for i in range(length) if bin(switches[j])[2:].rjust(length, "0")[i]=="1"])) for j in range(len(switches))]))
    
    populate_dp_array(length, dp_array, switches)

    # Get min path
    total += get_value_at_button_index(start, dp_array)

print(total)

'''
[...###]
[...#..]
[....#.]
[.#...#]
[..#..#]
[..#...]

[......] 0
[...###] 1
[....##] 2
[.....#] 3 -> 2
[.#....] 4
[..#..#] 1
'''
