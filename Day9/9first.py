def area(a, b):
  return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)

coords = []
with open("input.txt") as fIn:
  for line in fIn:
    coords.append(tuple(int(x) for x in line.strip().split(",")))

maxArea = -1
for i in coords:
  for j in coords:
    maxArea = max(maxArea, area(i,j))

print(maxArea)