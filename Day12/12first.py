total = 0
with open("input.txt") as fIn:
  for line in fIn:
    line = line.strip()
    area, counts = line.split(": ")
    x, y = tuple(map(int, area.split("x")))
    counts = tuple(map(int, counts.split(" ")))
    areaNeeded = 0
    areaNeeded += (counts[0] // 2) * 4 * 4 + (counts[0] % 2) * 9
    areaNeeded += counts[1] * 9
    areaNeeded += (counts[2] // 2) * 3 * 4 + (counts[2] % 2) * 9
    areaNeeded += counts[3] * 9
    areaNeeded += (counts[4] // 2) * 3 * 3 + (counts[4] % 2) * 9
    areaNeeded += (counts[5] // 2) * 5 * 3 + (counts[5] % 2) * 9
    print(areaNeeded - (x * y))
    if areaNeeded < (x * y):
      total += 1
print(total)