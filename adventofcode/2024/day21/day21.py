from functools import cache

from utils.grid import Grid
from utils.point import Point


def upload_input(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            lines.append(list(line.replace('\n', '')))
    return lines


def collect_dirs(p1, p2, to_avoid):
    hor = []
    ver = []

    if p1.y < p2.y:
        hor = ['>'] * (p2.y - p1.y)
    if p1.x > p2.x:
        ver = ['^'] * (p1.x - p2.x)
    if p1.x < p2.x:
        ver = ['v'] * (p2.x - p1.x)
    if p1.y > p2.y:
        hor = ['<'] * (p1.y - p2.y)
    if p1.move(Point((p2.x - p1.x), 0)).x == to_avoid.x and p1.move(Point((p2.x - p1.x), 0)).y == to_avoid.y:
        return [hor + ver]
    if p1.move(Point(0, (p2.y - p1.y))).y == to_avoid.y and p1.move(Point(0, (p2.y - p1.y))).x == to_avoid.x:
        return [ver + hor]
    return [ver + hor, hor + ver]


def collect_paths(grid):
    res = {}
    for r1 in grid.grid:
        for v1 in r1:
            if v1 != '':
                p1 = grid.find(v1)
                for r2 in grid.grid:
                    for v2 in r2:
                        if v1 != '':
                            p2 = grid.find(v2)
                            dirs = collect_dirs(p1, p2, grid.find('#')) if p1 != p2 else [[]]
                            res[(v1, v2)] = dirs

    return res


def collect_val_to_poses(grid):
    val_to_poses = {}
    poses_to_vals = {}
    for r1 in grid.grid:
        for v1 in r1:
            val_to_poses[v1] = grid.find(v1)
            poses_to_vals[grid.find(v1)] = v1
    return val_to_poses, poses_to_vals


def parse_num_part(num):
    return int("".join(map(str, num[:len(num)-1])))


def resolve_part1(data):
    res = 0
    numeric = Grid([
        ['7','8','9'],
        ['4','5','6'],
        ['1','2','3'],
        ['#','0','A']
    ])

    directional = Grid([
        ['#', '^', 'A'],
        ['<', 'v', '>']
    ])

    numeric_vals_to_poses, numeric_poses_to_vals = collect_val_to_poses(numeric)
    numeric_paths_to_costs = collect_paths(numeric)

    directional_vals_to_poses, directional_poses_to_vals = collect_val_to_poses(directional)
    directional_paths_to_costs = collect_paths(directional)


    for num in data:
        curr_d1 = directional_vals_to_poses['A']
        curr_d2 = directional_vals_to_poses['A']
        curr_n = numeric_vals_to_poses['A']

        num_part = parse_num_part(num)
        compl = 0
        ppp = []
        for to_push in num:
            push_ways = numeric_paths_to_costs[(numeric_poses_to_vals[curr_n], to_push)]
            pos_ways_count = []
            for push_way in push_ways:
                path_n = push_way + ['A']
                tmp = 0
                for p_n in path_n:
                    path_d1 = directional_paths_to_costs[(directional_poses_to_vals[curr_d1], p_n)][0] + ['A']
                    for p_d1 in path_d1:
                        path_d2 = directional_paths_to_costs[(directional_poses_to_vals[curr_d2], p_d1)][0] + ['A']
                        ppp += path_d2
                        tmp += len(path_d2)
                        curr_d2 = directional_vals_to_poses[p_d1]
                    curr_d1 = directional_vals_to_poses[p_n]
                pos_ways_count.append(tmp)
            compl += min(pos_ways_count)
            curr_n = numeric_vals_to_poses[to_push]
        print("num " + str(num_part) + " had value " + str(compl))

        res += num_part * compl



    return res

@cache
def calc_pos_ways(path, c, d):
    path_n = list(path)
    if c == 1:
        tmp = 0
        curr = Point(0, 2)
        for p_d1 in path_n:
            path_d2 = d.directional_paths_to_costs[(d.directional_poses_to_vals[curr], p_d1)][0] + ['A']
            tmp += len(path_d2)
            curr = d.directional_vals_to_poses[p_d1]
        return tmp
    else:
        tmp = 0
        curr = Point(0, 2)
        for p_n in path_n:
            pppp = d.directional_paths_to_costs[(d.directional_poses_to_vals[curr], p_n)]
            candidates = []
            for path_d in pppp:
                path_d1 = path_d + ['A']
                candidates.append(calc_pos_ways("".join(map(str, path_d1)), c - 1, d))
            tmp += min(candidates)
            curr = d.directional_vals_to_poses[p_n]

        return tmp


def resolve_part2(data):
    res = 0
    numeric = Grid([
        ['7', '8', '9'],
        ['4', '5', '6'],
        ['1', '2', '3'],
        ['#', '0', 'A']
    ])

    directional = Grid([
        ['#', '^', 'A'],
        ['<', 'v', '>']
    ])

    numeric_vals_to_poses, numeric_poses_to_vals = collect_val_to_poses(numeric)
    numeric_paths_to_costs = collect_paths(numeric)

    directional_vals_to_poses, directional_poses_to_vals = collect_val_to_poses(directional)
    directional_paths_to_costs = collect_paths(directional)

    for num in data:
        curr_n = numeric_vals_to_poses['A']

        num_part = parse_num_part(num)
        compl = 0
        for to_push in num:
            push_ways = numeric_paths_to_costs[(numeric_poses_to_vals[curr_n], to_push)]
            pos_ways_count = []
            for push_way in push_ways:
                path_n = push_way + ['A']
                tmp = calc_pos_ways("".join(map(str, path_n)), 25, Temp(directional_paths_to_costs, directional_poses_to_vals, directional_vals_to_poses))

                pos_ways_count.append(tmp)
            compl += min(pos_ways_count)
            curr_n = numeric_vals_to_poses[to_push]

        res += num_part * compl

    return res

class Temp:
    def __init__(self, directional_paths_to_costs, directional_poses_to_vals, directional_vals_to_poses):
        self.directional_paths_to_costs = directional_paths_to_costs
        self.directional_poses_to_vals = directional_poses_to_vals
        self.directional_vals_to_poses = directional_vals_to_poses

    def __hash__(self):
        return 1


if __name__ == "__main__":
    example_expectation_part1 = 126384
    uploaded_example_input = upload_input("example.txt")
    result_ex_part1 = resolve_part1(uploaded_example_input)
    print("Example output is " + str(result_ex_part1))
    assert result_ex_part1 == example_expectation_part1
    print("Example test case has passed for the part 1")
    uploaded_input = upload_input("input.txt")
    part_1_solution = resolve_part1(uploaded_input)
    print("Part1 answer is: " + str(part_1_solution))

    example_expectation_part2 = 154115708116294
    uploaded_example_input = upload_input("example.txt")
    result_ex_part2 = resolve_part2(uploaded_example_input)
    print("Example output is " + str(result_ex_part2))
    assert result_ex_part2 == example_expectation_part2
    print("Example test case has passed for the part 2")
    uploaded_input = upload_input("input.txt")
    part_2_res = resolve_part2(uploaded_input)
    print("Part2 answer is: " + str(part_2_res))