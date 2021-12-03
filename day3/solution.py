measurements = open("input.txt", "r")
measurements = [i[:-1] for i in measurements]

# Part 1
bit_count = [0] * 12
for measurement in measurements:
    for i, bit in enumerate(measurement):
        if bit == "1":
            bit_count[i] += 1
        else:
            bit_count[i] -= 1

print(bit_count)

gamma = ""
for count in bit_count:
    if count > 0:
        gamma += "1"
    else:
        gamma += "0"

bit_gamma = gamma
gamma = int(gamma, 2)
print("Gamma: ", gamma)

epsilon = 4095 - gamma
print("Epsilon:", epsilon)

power_consumption = gamma * epsilon
print("Power Consumption:", power_consumption)

# Part 2
from collections import Counter

oxygen_measurements = measurements
remaining_oxygen_measurements = []

for i in range(len(oxygen_measurements[0])):
    count = Counter([x[i] for x in oxygen_measurements])
    if count['1'] >= count['0']:
        remaining_oxygen_measurements = [m for m in oxygen_measurements if m[i] == '1']
    else:
        remaining_oxygen_measurements = [m for m in oxygen_measurements if m[i] == '0']

    print(remaining_oxygen_measurements)
    if len(remaining_oxygen_measurements) == 1:
        oxygen_rating = int(remaining_oxygen_measurements[0], 2)
        break

    oxygen_measurements = remaining_oxygen_measurements
    remaining_oxygen_measurements = []

co2_measurements = measurements
remaining_co2_measurements = []

for i in range(len(co2_measurements[0])):
    count = Counter([x[i] for x in co2_measurements])

    if count['0'] <= count['1']:
        remaining_co2_measurements = [m for m in co2_measurements if m[i] == '0']
    else:
        remaining_co2_measurements = [m for m in co2_measurements if m[i] == '1']

    if len(remaining_co2_measurements) == 1:
        co2_rating = int(remaining_co2_measurements[0], 2)
        break

    co2_measurements = remaining_co2_measurements
    remaining_co2_measurements = []

print("Oxygen Rating:", oxygen_rating)
print("CO2 Rating:", co2_rating)

life_support_rating = oxygen_rating * co2_rating
print("Life Support Rating:", life_support_rating)
