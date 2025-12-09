current_position = 50
password = 0
with open("input.txt") as fIn:
  for line in fIn:
    direction_str, distance = line[0], int(line[1:].strip())
    direction = 1
    if direction_str == 'L':
      direction = -1
    current_position = (current_position + distance * direction) % 100
    if current_position == 0:
      password += 1

print(password)
