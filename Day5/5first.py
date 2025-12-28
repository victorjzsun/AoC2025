ranges = []
toCheck = []
rangesComplete = False
with open("input.txt") as fIn:
  for line in fIn:
    if not rangesComplete:
      if line.strip() == "":
        rangesComplete = True
        continue
      ranges.append(tuple(map(int, line.strip().split("-"))))
    else:
      toCheck.append(int(line.strip()))

ranges.sort()
toCheck.sort()
rangeToCheck = 0
count = 0
for id in toCheck:
  while id > ranges[rangeToCheck][1]:
    if rangeToCheck + 1 >= len(ranges):
      break
    rangeToCheck += 1
  else:
    if id >= ranges[rangeToCheck][0] and id <= ranges[rangeToCheck][1]:
      count += 1
    continue
  break
print(count)



