def upload_input(file_path):
    with open(file_path, "r") as file:
        for line in file:
            return list(line)


def resolve_part1(line):
    res = 0

    file = []

    i = 0
    n = len(line)
    file_id = 0
    while i < n:
        if i % 2 == 0:
            val = file_id
            file_id += 1
        else:
            val = '.'
        j = 0
        while j < int(line[i]):
            file.append(val)
            j += 1

        i += 1

    n = len(file)
    i = 0
    j = n - 1
    while i < j:
        if file[i] != '.':
            i += 1
            continue
        if file[j] == '.':
            j -=1
            continue
        file[i] = file[j]
        file[j] = '.'
        i += 1
        j -= 1

    i = 0
    while file[i] != '.':
        res += i * file[i]
        i += 1

    return res



def resolve_part2(line):
    res = 0

    file = []

    i = 0
    n = len(line)
    file_id = 0
    idx_to_len = {}
    k = 0
    while i < n:
        if i % 2 == 0:
            val = file_id
            file_id += 1
        else:
            val = '.'
        j = 0
        while j < int(line[i]):
            idx_to_len[k] = int(line[i])
            file.append(val)
            k += 1
            j += 1

        i += 1

    j = len(file) - 1
    while j >= 0:
        if file[j] == '.':
            j -= idx_to_len[j]
            continue
        i = 0
        exit_loop = False
        while i < j and file[j] != '.' and not exit_loop:
            if file[i] != '.':
                i += idx_to_len[i]
                continue
            if idx_to_len[i] >= idx_to_len[j]:
                k = 0
                needed_to_feel = idx_to_len[i]
                present_to_fill = idx_to_len[j]
                diff = needed_to_feel - present_to_fill
                while k < present_to_fill:
                    file[i+k] = file[j-k]
                    file[j-k] = '.'
                    idx_to_len[i+k] = present_to_fill
                    idx_to_len[j-k] = present_to_fill
                    k += 1
                j -= present_to_fill
                i += present_to_fill
                k = 0
                while k < diff:
                    idx_to_len[i + k] = diff
                    k += 1
                exit_loop = True
            else:
                i += idx_to_len[i]
        if not exit_loop:
            j -= idx_to_len[j]


    i = 0
    while i < len(file):
        if file[i] != '.':
            res += i * file[i]
        i += 1

    return res


if __name__ == "__main__":
    example_expectation_part1 = 1928
    uploaded_example_input = upload_input("example.txt")
    result_ex_part1 = resolve_part1(uploaded_example_input)
    print("Example output is " + str(result_ex_part1))
    assert result_ex_part1 == example_expectation_part1
    print("Example test case has passed for the part 1")
    uploaded_input = upload_input("input.txt")
    print("Part1 answer is: " + str(resolve_part1(uploaded_input)))

    example_expectation_part2 = 2858
    uploaded_example_input = upload_input("example.txt")
    result_ex_part2 = resolve_part2(uploaded_example_input)
    print("Example output is " + str(result_ex_part2))
    assert result_ex_part2 == example_expectation_part2
    print("Example test case has passed for the part 2")
    uploaded_input = upload_input("input.txt")
    part_2_res = resolve_part2(uploaded_input)
    assert part_2_res == 6360363199987
    print("Part2 answer is: " + str(part_2_res))