import argparse


def naive_compute(s: str) -> int:
    """Naive Approach"""
    counter = 0
    for line in s.splitlines():
        limit, code, password = line.split()
        l_limit, r_limit = limit.split("-")
        left_limit, right_limit = int(l_limit), int(r_limit)
        code = code[0]

        if (
            code in password[left_limit - 1] and code not in password[right_limit - 1]
        ) or (
            code not in password[left_limit - 1] and code in password[right_limit - 1]
        ):
            counter += 1

    return counter


def compute(s: str) -> int:
    """Using XOR"""
    counter = 0
    for line in s.splitlines():
        limit, code, password = line.split()
        l_limit, r_limit = limit.split("-")
        left_limit, right_limit = int(l_limit), int(r_limit)
        code = code[0]

        if (password[left_limit - 1] == code) ^ (password[right_limit - 1] == code):
            counter += 1

    return counter


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file")
    args = parser.parse_args()

    with open(args.data_file) as f:
        # change compute to naive_compute to check output
        # using naive approach
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    exit(main())
