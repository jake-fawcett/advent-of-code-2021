import statistics

navigation_subsystem = open("input.txt", "r")
navigation_subsystem = [i[:-1] for i in navigation_subsystem]

part_one_score = 0
part_two_scores = []
opposites = {"<": ">", "{": "}", "[": "]", "(": ")"}
part_one_points = {">": 25137, "}": 1197, "]": 57, ")": 3}
part_two_points = {">": 4, "}": 3, "]": 2, ")": 1}
for line in navigation_subsystem:
    stack = []
    escaped = False
    for symbol in line:
        if symbol in "{[(<":
            stack.append(symbol)
        else:
            prev_symbol = stack.pop()
            if opposites[prev_symbol] != symbol:
                part_one_score += part_one_points[symbol]
                escaped = True
                break

    part_two_score = 0
    if not escaped:
        for symbol in reversed(stack):
            opposite = opposites[symbol]
            part_two_score *= 5
            part_two_score += part_two_points[opposite]
        part_two_scores.append(part_two_score)

part_two_final_score = statistics.median(part_two_scores)

print(part_one_score)
print(part_two_final_score)
