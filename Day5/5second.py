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
count = 0
lastCheck = -1
for range in ranges:
  if range[0] > lastCheck:
    lastCheck = range[0] - 1
  if range[1] > lastCheck:
    count += range[1] - lastCheck
    lastCheck = range[1]
print(count)



