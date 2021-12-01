depth_measurements = open("input.txt", "r")
depth_measurements = [int(i) for i in depth_measurements]

# Part 1
depth_increases = -1
prev_depth = 0
for depth_measurement in depth_measurements:
    depth = depth_measurement
    if depth > prev_depth:
        depth_increases += 1
    prev_depth = depth

print(f"Number of Depth Increases: {depth_increases}")


# Part 2

depth_increases = 0
for i, depth in enumerate(depth_measurements[3:], 1):
    if sum(depth_measurements[i:i+3]) > sum((depth_measurements[i-1:i+2])):
        depth_increases += 1

print(f"Number of Sliding Window Depth Increases: {depth_increases}")
