def product(list):
  total = 1
  for n in list:
    total *= n
  return total

def myInt(spaced_num):
  spaced_num = spaced_num.strip()
  total = 0
  for i in range(len(spaced_num)):
    if spaced_num[len(spaced_num) - 1 - i] != ' ':
      total += int(spaced_num[len(spaced_num) - 1 - i]) * (10 ** i)
  return total

nums = []
total = 0
with open("input.txt") as fIn:
  for line in fIn:
    line = line.strip("\n")
    if line[0].isdigit() or line[0].isspace():
      nums.append(line)
    else:
      curOp = line[0]
      lineNums = ["".join([row[0] for row in nums])]
      for i in range(1, len(line)):
        if line[i] == ' ':
          lineNums.append("".join([row[i] for row in nums]))
        else:
          if curOp == '*':
            total += product([myInt(x) for x in lineNums[:-1]])
          else:
            total += sum([myInt(x) for x in lineNums[:-1]])
          curOp = line[i]
          lineNums = ["".join([row[i] for row in nums])]
      if curOp == '*':
        total += product([myInt(x) for x in lineNums])
      else:
        total += sum([myInt(x) for x in lineNums])
        pass
        

print(total)