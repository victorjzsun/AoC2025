def product(list):
  total = 1
  for n in list:
    total *= n
  return total

nums = []
total = 0
with open("input.txt") as fIn:
  for line in fIn:
    line = line.strip()
    if line[0].isdigit():
      nums.append([])
      curNum = ""
      for char in line:
        if char.isdigit():
          curNum += char
        else:
          if curNum != "":
            nums[len(nums)-1].append(int(curNum))
            curNum = ""
      if curNum != "":
        nums[len(nums)-1].append(int(curNum))
        curNum = ""
    else:
      counter = 0
      for char in line:
        if char != ' ':
          if char == '*':
            total += product([row[counter] for row in nums])
          else:
            total += sum([row[counter] for row in nums])
          counter += 1

print(total)