import re


def upload_input(file_path):
    # Read input from a file
    with open(file_path, "r") as file:
        input_text = file.read()

    # Regular expression to match the data
    pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"

    # Find all matches
    matches = re.findall(pattern, input_text)

    # Parse the matches into a structured format
    parsed_data = []
    for match in matches:
        parsed_data.append({
            "Button A": {"X": int(match[0]), "Y": int(match[1])},
            "Button B": {"X": int(match[2]), "Y": int(match[3])},
            "Prize": {"X": int(match[4]), "Y": int(match[5])}
        })
    return parsed_data


def resolve_part1(data):
    res = 0

    for claw in data:
        x_a = claw['Button A']['X']
        x_b = claw['Button B']['X']
        y_a = claw['Button A']['Y']
        y_b = claw['Button B']['Y']
        X = claw['Prize']['X']
        Y = claw['Prize']['Y']

        a_1 = 0
        a_2 = 0

        if y_a*y_b != y_b*x_a:
            a_2 = (X*y_a - x_a*Y)/(y_a*x_b-y_b*x_a)
            a_1 = (X - x_b*a_2)/x_a
        elif x_a*y_b != -x_b*y_a:
            a_1 = (X*y_b-x_b*Y)/(x_a*y_b-x_b*y_a)
            a_2 = (Y - y_a * a_1) / y_b
        else:
            continue

        if a_1.is_integer() and a_2.is_integer() and a_1 <= 100 and a_2 <= 100:
            res += a_1 * 3 + a_2


    return int(res)



def resolve_part2(data):

    res = 0

    for claw in data:
        x_a = claw['Button A']['X']
        x_b = claw['Button B']['X']
        y_a = claw['Button A']['Y']
        y_b = claw['Button B']['Y']
        X = 10000000000000 + claw['Prize']['X']
        Y = 10000000000000 + claw['Prize']['Y']

        a_1 = 0
        a_2 = 0

        if y_a * y_b != y_b * x_a:
            a_2 = (X * y_a - x_a * Y) / (y_a * x_b - y_b * x_a)
            a_1 = (X - x_b * a_2) / x_a
        elif x_a * y_b != -x_b * y_a:
            a_1 = (X * y_b - x_b * Y) / (x_a * y_b - x_b * y_a)
            a_2 = (Y - y_a * a_1) / y_b
        else:
            continue

        if a_1.is_integer() and a_2.is_integer():
            res += a_1 * 3 + a_2

    return int(res)


if __name__ == "__main__":
    example_expectation_part1 = 480
    uploaded_example_input = upload_input("example.txt")
    result_ex_part1 = resolve_part1(uploaded_example_input)
    print("Example output is " + str(result_ex_part1))
    assert result_ex_part1 == example_expectation_part1
    print("Example test case has passed for the part 1")
    uploaded_input = upload_input("input.txt")
    print("Part1 answer is: " + str(resolve_part1(uploaded_input)))


    print("Example test case has passed for the part 2")
    uploaded_input = upload_input("input.txt")
    part_2_res = resolve_part2(uploaded_input)
    print("Part2 answer is: " + str(part_2_res))