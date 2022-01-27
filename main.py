import uvloop
import argparse

from tools.utils import str2bool

def main(args: argparse.Namespace):
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", type=str2bool)
    parser.add_argument("-s", "--store", type=str2bool)
    parser.add_argument("-w", "--workers", type=int)

    args = parser.parse_args()
    main(args)
