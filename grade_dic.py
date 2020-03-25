import argparse

grades = {
    "A": 91,
    "B": 81,
    "C": 71,
    "D": 61,
    "F": 0
}


def score_range(string):
    value = int(string)
    if value > 100 or value < 0:
        msg = "%r is not in range[0-100]" % string
        raise argparse.ArgumentTypeError(msg)
    return value


def main(argv):
    for grade, min_score in grades.items():
        if argv >= min_score:
            print(grade)
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate grade from score')
    parser.add_argument('score', type=score_range,
                        help='an integer for the accumulator [0-100]')
    args = parser.parse_args()
    main(args.score)
