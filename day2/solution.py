import re

commands = open("input.txt", "r")
commands = [i for i in commands]

# Part 1 + Part 2
horizontal_position = 0
depth = 0
aim = 0

for command in commands:
    value = int(re.sub('\D', '', command))
    if "forward" in command:
        horizontal_position += value
    elif "down" in command:
        depth += value
    elif "up" in command:
        depth -= value

print(f'Vertical Position: {depth}')
print(f'Horizontal Position: {horizontal_position}')
print(f"Answer {horizontal_position * depth}")


# Part 2
horizontal_position = 0
depth = 0
aim = 0

for command in commands:
    value = int(re.sub('\D', '', command))
    if "forward" in command:
        horizontal_position += value
        depth += (value * aim)
    elif "down" in command:
        aim += value
    elif "up" in command:
        aim -= value

print(f'Depth Position: {depth}')
print(f'Horizontal Position: {horizontal_position}')
print(f"Answer {horizontal_position * depth}")
