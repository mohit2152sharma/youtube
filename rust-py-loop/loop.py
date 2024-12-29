from argparse import ArgumentParser
from time import time


def main():
    parser = ArgumentParser()
    parser.add_argument("n", type=int, help="loop till n")

    n = parser.parse_args().n

    t0 = time()
    for _ in range(n):
        pass

    print(f"Total time taken: {time() - t0} seconds")


if __name__ == "__main__":
    main()
