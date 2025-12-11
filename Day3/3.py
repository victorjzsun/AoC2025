total = 0
battCount = 12
# All values of joltage after this index is considered blank,
# used to reset the joltage array when we find a new battery
empty = 0
with open("input.txt") as fIn:
  for bank in fIn:
    bank = bank.strip()
    # Initialize array, with size of number of batteries
    joltage = [0] * battCount
    batt = 0
    while batt < len(bank):
      # Initialize which battery of the joltage array we want to check, start with first
      joltIndex = 0
      # If we are too close to the end of the array, we can only start checking at the index
      # in the joltage array such that we have just enough batteries left in the bank to use
      if (len(bank) - (batt + 1) < battCount - 1):
        joltIndex = (battCount - 1) - (len(bank) - (batt + 1))
      # Iterate across all picked batteries in the joltage array at and to the right of
      # joltIndex. Given the problem, the array will be sorted from highest to lowest
      while joltIndex < battCount:
        # Either we hit an entry that is marked as blank or we found a better battery to use
        if joltIndex == empty or joltage[joltIndex] < int(bank[batt]):
          # Set the battery in the joltage array
          joltage[joltIndex] = int(bank[batt])
          # Mark all later batteries as blank
          empty = joltIndex + 1
          break
        joltIndex += 1
      batt += 1
    # Compute joltage and add to total
    total += int("".join([str(x) for x in joltage]))
# Return value
print(total)