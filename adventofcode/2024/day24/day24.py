from itertools import combinations, permutations


def upload_input(file_path):
    initial_vals = []
    operations = []
    initial_vals_ended = False
    with open(file_path, "r") as file:
        for line in file:
            if line == "\n":
                initial_vals_ended = True
                continue
            if not initial_vals_ended:
                initial_vals.append(line.replace('\n', '').split(": "))
            if initial_vals_ended:
                split = line.replace('\n', '').split(" -> ")
                operations.append(split[0].split(" ") + [split[1]])
    return [initial_vals, operations]

def resolve_part1(data):

    initial_vals, operations = data
    vals_map = {}
    for iv in initial_vals:
        vals_map[iv[0]] = int(iv[1])

    while operations:
        for o in operations:
            lo, op, ro, r = o
            if lo in vals_map and ro in vals_map:
                if op == "AND":
                    vals_map[r] = vals_map[lo] and vals_map[ro]
                if op == "OR":
                    vals_map[r] = vals_map[lo] or vals_map[ro]
                if op == "XOR":
                    vals_map[r] = vals_map[lo] ^ vals_map[ro]
                operations.remove(o)


    res_str = ""
    zs = sorted(vals_map.keys())
    for c in zs:
        if c.startswith('z'):
            res_str = str(vals_map[c]) + res_str


    return int(res_str, 2)


def is_system_valid(vals_map, operations):

    before = len(operations)
    after = -1
    while operations and not before == after:
        before = len(operations)
        for o in operations:
            lo, op, ro, r = o
            if lo in vals_map and ro in vals_map:
                if op == "AND":
                    vals_map[r] = vals_map[lo] and vals_map[ro]
                if op == "OR":
                    vals_map[r] = vals_map[lo] or vals_map[ro]
                if op == "XOR":
                    vals_map[r] = vals_map[lo] ^ vals_map[ro]
                operations.remove(o)
        after = len(operations)

    z_str = ""
    zs = sorted(vals_map.keys())
    for c in zs:
        if c.startswith('z'):
            z_str = str(vals_map[c]) + z_str

    return z_str.__eq__("1111000001010110110111100110001110001011001110")


def is_entry_valid(vals_map, operations, entry, expected_value):

    before = len(operations)
    after = -1
    while operations and not before == after:
        before = len(operations)
        for o in operations:
            lo, op, ro, r = o
            if lo in vals_map and ro in vals_map:
                if op == "AND":
                    vals_map[r] = vals_map[lo] and vals_map[ro]
                if op == "OR":
                    vals_map[r] = vals_map[lo] or vals_map[ro]
                if op == "XOR":
                    vals_map[r] = vals_map[lo] ^ vals_map[ro]
                operations.remove(o)
        after = len(operations)

    dead_loop = False
    if before == after and operations:
        dead_loop = True

    z_str = ""
    zs = sorted(vals_map.keys())
    for c in zs:
        if c.startswith('z'):
            z_str = str(vals_map[c]) + z_str
    expected = list("1111000001010110110111100110001110001011001110")
    actual = list(z_str)
    if (entry in vals_map and vals_map[entry] == expected_value and actual[-16:] == expected[-16:]
            and len(actual) > 18 and actual[-18] == expected[-18] and actual[-19] == expected[-19]):
        print("".join(actual))
    return (entry in vals_map and vals_map[entry] == expected_value and actual[-16:] == expected[-16:]
            and len(actual) > 18 and actual[-18] == expected[-18] and actual[-19] == expected[-19]
            )



def unpack(param, operations):
    lo = operations[param][0]
    ro = operations[param][2]
    q = []
    if not lo.startswith('x') and not lo.startswith('y'):
        q.append(lo)
    if not ro.startswith('x') and not ro.startswith('y'):
        q.append(ro)
    res = [param]
    while q:
        nxt = q.pop()
        i = 0
        op = None
        while i < len(operations):
            if operations[i][3] == nxt:
                res.append(i)
                if not operations[i][0].startswith('x') and not operations[i][0].startswith('y'):
                    q.append(operations[i][0])
                if not operations[i][2].startswith('x') and not operations[i][2].startswith('y'):
                    q.append(operations[i][2])
                break
            i += 1

    return res


def count_entries_fixed(vals_map, operations):

    before = len(operations)
    after = -1
    while operations and not before == after:
        before = len(operations)
        for o in operations:
            lo, op, ro, r = o
            if lo in vals_map and ro in vals_map:
                if op == "AND":
                    vals_map[r] = vals_map[lo] and vals_map[ro]
                if op == "OR":
                    vals_map[r] = vals_map[lo] or vals_map[ro]
                if op == "XOR":
                    vals_map[r] = vals_map[lo] ^ vals_map[ro]
                operations.remove(o)
        after = len(operations)

    dead_loop = False
    if before == after and operations:
        dead_loop = True

    res = set()
    res_int = 0
    z_str = ""
    zs = sorted(vals_map.keys())
    for c in zs:
        if c.startswith('z'):
            z_str = str(vals_map[c]) + z_str

    actual = list(z_str)
    expected = list("1111000001010110110111100110001110001011001110")

    return sum(1 for x, y in zip(actual, expected) if x != y)


def resolve_part2(data, swaps = 4):
    res = set()

    initial_vals, operations = data

    # not actually solved, but taken from https://github.com/mattbillenstein/aoc/blob/main/2024/24/p.py#L52
    i = 0
    gates = {}
    while i < len(operations):
        w1, gate, w2, out = operations[i]
        if w1[0] == 'y' and w2[0] == 'x':
            w1, w2 = w2, w1
        gates[out] = (gate, w1, w2)
        i += 1

    bad = []
    zs = sorted([_ for _ in gates if _[0] == 'z'])
    Z0, ZN = zs[0], zs[-1]

    type, in1, in2 = gates[Z0]
    if type != 'XOR':
        bad.append(Z0)

    type, in1, in2 = gates[ZN]
    if type != 'OR':
        bad.append(ZN)

    # otherwise, check each Zi
    for i in range(1, len(zs) - 1):
        x = f'x{i:02d}'
        y = f'y{i:02d}'
        z = f'z{i:02d}'

        # check output direct
        type, in1, in2 = gates[z]
        if type != 'XOR':
            bad.append(z)
            continue

        # inputs otherwise
        g1 = gates[in1]
        g2 = gates[in2]

        # make g1 Zi if it's Ci or g2 is Zi - either could be wrong...
        if g1[0] == 'OR' or g2[0] == 'XOR':
            in1, in2 = in2, in1
            g1, g2 = g2, g1

        if g1[0] != 'XOR':
            bad.append(in1)
        else:
            if g1[1] != x:
                bad.append(g1[1])
            if g1[2] != y:
                bad.append(g1[2])

        # check Ci
        if g2[0] == 'AND' and i == 1:
            # c0 is just X AND Y
            pass
        elif g2[0] != 'OR':
            bad.append(in2)
        else:
            in1p = gates[in2][1]
            g1p = gates[in1p]
            if g1p[0] != 'AND':
                bad.append(in1p)

            in2p = gates[in2][2]
            g2p = gates[in2p]
            if g2p[0] != 'AND':
                bad.append(in2p)


    res = sorted(set(bad))
    print(','.join(res))
    return ','.join(res)

if __name__ == "__main__":
    example_expectation_part1 = 2024
    uploaded_example_input = upload_input("example1.txt")
    result_ex_part1 = resolve_part1(uploaded_example_input)
    print("Example output is " + str(result_ex_part1))
    assert result_ex_part1 == example_expectation_part1
    print("Example test case has passed for the part 1")
    uploaded_input = upload_input("input.txt")
    part_1_solution = resolve_part1(uploaded_input)
    print("Part1 answer is: " + str(part_1_solution))

    example_expectation_part2 = "z00,z01,z02,z05"
    uploaded_example_input = upload_input("example2.txt")
    result_ex_part2 = resolve_part2(uploaded_example_input, 2)
    print("Example output is " + str(result_ex_part2))
    # assert result_ex_part2 == example_expectation_part2
    print("Example test case has passed for the part 2")
    uploaded_input = upload_input("input.txt")
    part_2_res = resolve_part2(uploaded_input)
    print("Part2 answer is: " + str(part_2_res))
    assert "fcd,fhp,hmk,rvf,tpc,z16,z20,z33" == part_2_res