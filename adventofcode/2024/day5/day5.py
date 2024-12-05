import math


class Rule:
    def __init__(self, rule_string: str):
        substrings = rule_string.split("|")
        self.page_before = int(substrings[0])
        self.page_after = int(substrings[1])

    def is_violated(self, left_page, right_page):
        return int(self.page_after) == int(left_page) and int(self.page_before) == int(right_page)


class UpdateLine:
    def __init__(self, update_line_string: str):
        self.update_pages = update_line_string.replace('\n', '').split(",")

    def middle_num(self):
        return int(self.update_pages[math.floor(len(self.update_pages)/2)])

def upload_input(file_path):
    rules = []
    update_lines = []
    first_part = True
    with open(file_path, "r") as file:
        for line in file:
            if line == "\n":
                first_part = False
                continue
            if first_part:
                rules.append(Rule(line))
            else:
                update_lines.append(UpdateLine(line))

    return [rules, update_lines]


def resolve_part1(rules, update_lines):
    res = 0
    rules_count = len(rules)
    i = 0
    n = len(update_lines)
    while i < n:
        update_is_fine = True
        j1 = 0
        m = len(update_lines[i].update_pages)
        while j1 < m - 1 and update_is_fine:
            k = 0
            j2 = j1 + 1
            while j2 < m:
                while k < rules_count and update_is_fine:
                    if rules[k].is_violated(update_lines[i].update_pages[j1], update_lines[i].update_pages[j2]):
                        update_is_fine = False
                    k += 1
                j2 += 1
            j1 += 1
        if update_is_fine:
            res += update_lines[i].middle_num()
        i += 1

    return res


def check_update(rules, update_line):
    rules_count = len(rules)
    update_is_fine = True
    j1 = 0
    m = len(update_line)
    violated_rule_index = -1
    violated_page_number_index_1 = -1
    violated_page_number_index_2 = -1
    while j1 < m - 1 and update_is_fine:
        k = 0
        j2 = j1 + 1
        while j2 < m:
            while k < rules_count and update_is_fine:
                if rules[k].is_violated(update_line[j1], update_line[j2]):
                    update_is_fine = False
                    violated_rule_index = k
                    violated_page_number_index_1 = j1
                    violated_page_number_index_2 = j2
                k += 1
            j2 += 1
        j1 += 1
    return [update_is_fine, update_line, violated_rule_index, violated_page_number_index_1, violated_page_number_index_2]


def resolve_part2(rules, update_lines):
    res = 0
    incorrect_info = []
    rules_count = len(rules)
    i = 0
    n = len(update_lines)
    while i < n:

        update_is_fine_check_result = check_update(rules, update_lines[i].update_pages)

        if not update_is_fine_check_result[0]:
            incorrect_info.append(update_is_fine_check_result[1:])
        i += 1

    i = 0
    n = len(incorrect_info)
    while i < n:
        update_line_to_fix = incorrect_info[i][0]
        cache = update_line_to_fix[incorrect_info[i][2]]
        update_line_to_fix[incorrect_info[i][2]] = update_line_to_fix[incorrect_info[i][3]]
        update_line_to_fix[incorrect_info[i][3]] = cache

        is_fine = check_update(rules, update_line_to_fix)
        while not is_fine[0]:
            update_line_to_fix = is_fine[1]
            cache = update_line_to_fix[is_fine[3]]
            update_line_to_fix[is_fine[3]] = update_line_to_fix[is_fine[4]]
            update_line_to_fix[is_fine[4]] = cache
            is_fine = check_update(rules, update_line_to_fix)

        res += int(update_line_to_fix[math.floor(len(update_line_to_fix)/2)])

        i += 1

    return res


if __name__ == "__main__":
    example_expectation_part1 = 143
    uploaded_example_input = upload_input("example.txt")
    result_ex_part1 = resolve_part1(uploaded_example_input[0], uploaded_example_input[1])
    print("Example output is " + str(result_ex_part1))
    assert result_ex_part1 == example_expectation_part1
    print("Example test case has passed for the part 1")
    uploaded_input = upload_input("input.txt")
    print("Part1 answer is: " + str(resolve_part1(uploaded_input[0], uploaded_input[1])))

    example_expectation_part2 = 123
    uploaded_example_input = upload_input("example.txt")
    result_ex_part2 = resolve_part2(uploaded_example_input[0], uploaded_example_input[1])
    print("Example output is " + str(result_ex_part2))
    assert result_ex_part2 == example_expectation_part2
    print("Example test case has passed for the part 2")
    uploaded_input = upload_input("input.txt")
    print("Part2 answer is: " + str(resolve_part2(uploaded_input[0], uploaded_input[1])))