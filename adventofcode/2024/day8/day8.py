from itertools import combinations

from utils.grid import Grid


def upload_input(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            lines.append(list(line.replace('\n', '')))
    return lines


def resolve_part1(lines):
    res = set()

    grid = Grid(lines)
    n = grid.n
    m = grid.m
    unique = grid.unique_values(exception='.')

    for antenna in unique:
        places = grid.find_all(antenna)
        all_places_pairs = combinations(places, 2)
        for left, right in all_places_pairs:
            dx = left.x - right.x
            dy = left.y - right.y
            i_cand = right.x - dx
            j_cand = right.y - dy
            if 0 <= i_cand < n and 0 <= j_cand < m:
                res.add((i_cand, j_cand))
            i_cand_2 = left.x + dx
            j_cand_2 = left.y + dy
            if 0 <= i_cand_2 < n and 0 <= j_cand_2 < m:
                res.add((i_cand_2, j_cand_2))

    return len(res)



def resolve_part2(lines):
    res = set()

    grid = Grid(lines)
    n = grid.n
    m = grid.m
    unique = grid.unique_values('.')

    for antenna in unique:
        places = grid.find_all(antenna)
        all_places_pairs = combinations(places, 2)
        for left, right in all_places_pairs:
            dx = left.x - right.x
            dy = left.y - right.y
            i_cand = left.x
            j_cand = left.y
            while 0 <= i_cand < n and 0 <= j_cand < m:
                res.add((i_cand, j_cand))
                i_cand += dx
                j_cand += dy

            i_cand = left.x
            j_cand = left.y
            while 0 <= i_cand < n and 0 <= j_cand < m:
                res.add((i_cand, j_cand))
                i_cand -= dx
                j_cand -= dy


    return len(res)


if __name__ == "__main__":
    example_expectation_part1 = 14
    uploaded_example_input = upload_input("example.txt")
    result_ex_part1 = resolve_part1(uploaded_example_input)
    print("Example output is " + str(result_ex_part1))
    assert result_ex_part1 == example_expectation_part1
    print("Example test case has passed for the part 1")
    uploaded_input = upload_input("input.txt")
    print("Part1 answer is: " + str(resolve_part1(uploaded_input)))

    example_expectation_part2 = 34
    uploaded_example_input = upload_input("example.txt")
    result_ex_part2 = resolve_part2(uploaded_example_input)
    print("Example output is " + str(result_ex_part2))
    assert result_ex_part2 == example_expectation_part2
    print("Example test case has passed for the part 2")
    uploaded_input = upload_input("input.txt")
    print("Part2 answer is: " + str(resolve_part2(uploaded_input)))