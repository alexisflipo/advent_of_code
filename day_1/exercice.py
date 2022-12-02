from pathlib import Path


def get_max_cals(input: Path) -> int:
    total_count = 0
    total_cals_by_elves = []
    with open(input, "r") as f:
        for line in f:
            if line == "\n":
                total_cals_by_elves.append(total_count)
                total_count = 0
                continue
            total_count += int(line)
        total_cals_by_elves.append(total_count)
    sorted_list = sorted(total_cals_by_elves)
    last_three = sorted_list[-3:]
    # return max(total_cals_by_elves)
    return sum(last_three)


result = get_max_cals("day_1/sample.txt")
print(result)
