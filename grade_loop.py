import argparse

scores = (91, 81, 71, 61, 0)
grades = ("A", "B", "C", "D", "F")


def score_range(string):
    value = int(string)
    if value > 100 or value < 0:
        msg = "%r is not in range[0-100]" % string
        raise argparse.ArgumentTypeError(msg)
    return value


def main(argv):
    for num, score in enumerate(scores, start=0):
        if argv >= score:
            print(grades[num])
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate grade from score')
    parser.add_argument('score', type=score_range,
                        help='an integer for the accumulator [0-100]')
    args = parser.parse_args()
    main(args.score)
