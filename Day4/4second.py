from queue import Queue
total = 0
queue = Queue()
with open("input.txt") as fIn:
  text = [[[cell, -1] for cell in list(row.strip())] for row in fIn.read().split("\n")]
  rowI = 0
  while rowI < len(text):
    columnI = 0
    while columnI < len(text[rowI]):
      count = 0
      if text[rowI][columnI][0] == '@':
        for i in range(-1,2):
          for j in range(-1,2):
            # Centre
            if i == 0 and j == 0:
              continue
            # Offgrid
            if rowI + i < 0 or rowI + i >= len(text) or columnI + j < 0 or columnI + j >= len(text[rowI]):
              continue
            # Valid neighbour
            if text[rowI + i][columnI + j][0] == '@':
              count += 1
            text[rowI][columnI][1] = count
        if count < 4:
          queue.put((rowI, columnI))
      columnI += 1
    rowI += 1
  counter = 0
  while not queue.empty():
    rowI, columnI = queue.get()
    if text[rowI][columnI][0] != "@":
      continue
    text[rowI][columnI][0] = '.'
    total += 1
    if counter < 40:
      counter += 1
    for i in range(-1,2):
      for j in range(-1,2):
        # Centre
        if i == 0 and j == 0:
          continue
        # Offgrid
        if rowI + i < 0 or rowI + i >= len(text) or columnI + j < 0 or columnI + j >= len(text[rowI]):
          continue
        if text[rowI + i][columnI + j][0] == "@":
          text[rowI + i][columnI + j][1] -= 1
          if text[rowI + i][columnI + j][1] < 4:
            queue.put((rowI + i, columnI + j))
print(total)