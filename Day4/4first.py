
total = 0
with open("input.txt") as fIn:
  text = [row.strip() for row in fIn.read().split("\n")]
  rowI = 0
  while rowI < len(text):
    row = text[rowI].strip()
    columnI = 0
    while columnI < len(row):
      count = 0
      if text[rowI][columnI] == '@':
        for i in range(-1,2):
          for j in range(-1,2):
            # Centre
            if i == 0 and j == 0:
              continue
            # Offgrid
            if rowI + i < 0 or rowI + i >= len(text) or columnI + j < 0 or columnI + j >= len(row):
              continue
            # Valid neighbour
            if text[rowI + i][columnI + j] == '@':
              count += 1
        if count < 4:
          total += 1
      columnI += 1
    rowI += 1
print(total)