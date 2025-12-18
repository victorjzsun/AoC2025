marks = {}
total = 0
with open("input.txt") as fIn:
  line = fIn.readline()
  for i, char in enumerate(line):
    if char == 'S':
      marks[i] = True
  for line in fIn:
    line = line.strip()
    for i, char in enumerate(line):
      if char == '^' and marks.get(i, False):
        total += 1
        if i != 0:
          marks[i-1] = True
        if i != len(line) - 1:
          marks[i+1] = True
        marks.pop(i)
print(total)
