
def upload_input(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            lines.append(line.replace('\n', ''))
    return lines


def generate_secret_number(num):
    prev_num = num
    num *= 64
    num ^= prev_num
    num %= 16777216

    prev_num = num
    num /= 32
    num = int(num)
    num ^= prev_num
    num %= 16777216

    prev_num = num
    num *= 2048
    num ^= prev_num
    num %= 16777216

    return num


def generate_secret_number_n_times(num, param):
    i = 0
    res = []
    while i < param:
        num = generate_secret_number(num)
        res.append(num)
        i += 1
    return res


def resolve_part1(data):
    res = 0

    for num_s in data:
        num = int(num_s)
        num = generate_secret_number_n_times(num, 2000)[1999]
        res += num



    return res


def resolve_part2(data):
    buyer_initial_to_secrets_last_digits = {}
    for num_s in data:
        num = int(num_s)
        secrets = [num] + generate_secret_number_n_times(num, 2000)
        ls = list(map(lambda x: x % 10, secrets))
        buyer_initial_to_secrets_last_digits[num] = ls

    buyer_initial_to_diffs = {}
    for num, secrets in buyer_initial_to_secrets_last_digits.items():
        i = 0
        diffs = [None]
        while i < len(secrets) - 1:
            diffs.append(secrets[i+1] - secrets[i])
            i += 1
        buyer_initial_to_diffs[num] = diffs

    buyers_initial_to_diffs_seq_to_nums = {}
    for num, diffs in buyer_initial_to_diffs.items():
        i = 1
        diffs_seq_to_nums = {}
        while i < len(diffs) - 4:
            key = tuple(diffs[i:i + 4])
            if key not in diffs_seq_to_nums:
                diffs_seq_to_nums[key] = buyer_initial_to_secrets_last_digits[num][i + 3]
            i += 1
        buyers_initial_to_diffs_seq_to_nums[num] = diffs_seq_to_nums

    unique_seqs = set()
    for num, diffs_seqs in buyers_initial_to_diffs_seq_to_nums.items():
        unique_seqs = unique_seqs.union(diffs_seqs.keys())


    max_bananas = 0
    for seq in unique_seqs:
        cand = 0
        for num, diffs_seqs in buyers_initial_to_diffs_seq_to_nums.items():
            if seq in diffs_seqs:
                cand += diffs_seqs[seq]
        if cand > max_bananas:
            max_bananas = cand



    return max_bananas


if __name__ == "__main__":
    example_expectation_part1 = 37327623
    uploaded_example_input = upload_input("example1.txt")
    result_ex_part1 = resolve_part1(uploaded_example_input)
    print("Example output is " + str(result_ex_part1))
    assert result_ex_part1 == example_expectation_part1
    print("Example test case has passed for the part 1")
    uploaded_input = upload_input("input.txt")
    part_1_solution = resolve_part1(uploaded_input)
    print("Part1 answer is: " + str(part_1_solution))

    example_expectation_part2 = 23
    uploaded_example_input = upload_input("example2.txt")
    result_ex_part2 = resolve_part2(uploaded_example_input)
    print("Example output is " + str(result_ex_part2))
    assert result_ex_part2 == example_expectation_part2
    print("Example test case has passed for the part 2")
    uploaded_input = upload_input("input.txt")
    part_2_res = resolve_part2(uploaded_input)
    print("Part2 answer is: " + str(part_2_res))