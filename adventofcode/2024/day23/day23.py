def upload_input(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            lines.append(line.replace('\n', '').split('-'))
    return lines

def resolve_part1(data):
    res = 0

    computer_connections = set()

    for cc in data:
        computer_connections.add((cc[0], cc[1]))
        computer_connections.add((cc[1], cc[0]))

    computer_sets = []

    for cc in data:
        for cc2 in data:
            if cc != cc2:
                if cc2[0] == cc[0] and (cc2[1], cc[1]) in computer_connections:
                    curr_set = set()
                    curr_set.add(cc[0])
                    curr_set.add(cc[1])
                    curr_set.add(cc2[1])
                    computer_sets.append(curr_set)
                if cc2[1] == cc[0] and (cc2[0], cc[1]) in computer_connections:
                    curr_set = set()
                    curr_set.add(cc[0])
                    curr_set.add(cc[1])
                    curr_set.add(cc2[0])
                    computer_sets.append(curr_set)
                if cc2[0] == cc[1] and (cc2[1], cc[0]) in computer_connections:
                    curr_set = set()
                    curr_set.add(cc[0])
                    curr_set.add(cc[1])
                    curr_set.add(cc2[1])
                    computer_sets.append(curr_set)
                if cc2[1] == cc[1] and (cc2[0], cc[0]) in computer_connections:
                    curr_set = set()
                    curr_set.add(cc[0])
                    curr_set.add(cc[1])
                    curr_set.add(cc2[0])
                    computer_sets.append(curr_set)

    unique_data = list(map(set, set(frozenset(item) for item in computer_sets)))
    for cs in unique_data:
        if len(cs) == 3:
            for cc in cs:
                if cc.startswith('t'):
                    res += 1
                    break




    return res


def interconnected(array, cc, computer_connections):
    for x in array:
        if ((x, cc[0]) not in computer_connections and x != cc[0]) or ((x, cc[1]) not in computer_connections and x != cc[1]):
            return False, array
    return True, list(set(array).union(set(cc)))


def resolve_part2(data):

    computer_connections = set()

    for cc in data:
        computer_connections.add((cc[0], cc[1]))
        computer_connections.add((cc[1], cc[0]))

    nets = []
    visited = set()
    for cc1 in data:
        interconnection = cc1
        visited.add(tuple(cc1))
        for cc2 in data:
            if tuple(cc2) not in visited:
                are_interconnected, interconnection = interconnected(interconnection, cc2, computer_connections)
                if are_interconnected:
                    visited.add(tuple(cc2))
        nets.append(interconnection)

    nets.sort(key=lambda x: len(x), reverse=True)

    return ",".join(sorted(nets[0]))


if __name__ == "__main__":
    example_expectation_part1 = 7
    uploaded_example_input = upload_input("example.txt")
    result_ex_part1 = resolve_part1(uploaded_example_input)
    print("Example output is " + str(result_ex_part1))
    assert result_ex_part1 == example_expectation_part1
    print("Example test case has passed for the part 1")
    uploaded_input = upload_input("input.txt")
    part_1_solution = resolve_part1(uploaded_input)
    print("Part1 answer is: " + str(part_1_solution))

    example_expectation_part2 = "co,de,ka,ta"
    uploaded_example_input = upload_input("example.txt")
    result_ex_part2 = resolve_part2(uploaded_example_input)
    print("Example output is " + str(result_ex_part2))
    assert result_ex_part2 == example_expectation_part2
    print("Example test case has passed for the part 2")
    uploaded_input = upload_input("input.txt")
    part_2_res = resolve_part2(uploaded_input)
    print("Part2 answer is: " + str(part_2_res))