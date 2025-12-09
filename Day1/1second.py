current_position = 50
password = 0
with open("input.txt") as fIn:
  for line in fIn:
    direction_str, distance = line[0], int(line[1:].strip())
    direction = 1
    if direction_str == 'R':
      password += (current_position + distance) // 100
    elif direction_str == 'L':
      direction = -1
      password += ((100 - (100 if current_position == 0 else current_position)) + distance) // 100
    current_position = (current_position + distance * direction) % 100

print(password)
