import math

def length(part):
  return math.floor(math.log10(part))

def duplicate(part):
  return part * (10 ** (length(part) + 1)) + part

sum = 0
with open("input.txt") as fIn:
  for line in fIn:
    for range in line.strip().split(","):
      start_str, end_str = range.split("-", 1)
      start, end = int(start_str), int(end_str)
      # set part = first half
      # 0-9 case
      beginning = 1
      if start >= 10:
        # even length of start:
          # start with part
        beginning = int(start_str[:(len(start_str) // 2)])
        # odd length of start:
          # start with 1000... (length num of zeros)
        if len(start_str) % 2 != 0:
          beginning = 10 ** (length(beginning) + 1)
        # partpart < start
        elif duplicate(beginning) < start:
          beginning += 1
      while duplicate(beginning) <= end:
        sum += duplicate(beginning)
        beginning += 1

print(sum)

    
