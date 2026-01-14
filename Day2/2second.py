sum = 0
with open("input.txt") as fIn:
  for line in fIn:
    for numRange in line.strip().split(","):
      start_str, end_str = numRange.split("-", 1)
      start, end = int(start_str), int(end_str)
      for i in range(start, end + 1):
        num = str(i)
        invalids = {}
        for j in range(0, len(num) // 2):
          if len(num) % (j + 1) == 0 and num[:j+1] * (len(num) // (j + 1)) == num and num[:j+1] * (len(num) // (j + 1)) not in invalids:
            invalids[num[:j+1] * (len(num) // (j + 1))] = True
            sum += int(num[:j+1] * (len(num) // (j + 1)))
            print(num[:j+1] * (len(num) // (j + 1)))
print(sum)