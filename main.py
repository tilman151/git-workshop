import argparse
from typing import List


def geometric_series(n: int, first_term: float = 1.0, ratio: float = 2.0) -> List[float]:
    """
    Generate a list containing the first n elements of a geometric series.
    n must be a non-negative integer.
    Examples:
      n=0 -> []
      n=1, first_term=1, ratio=2 -> [1.0]
      n=5, first_term=1, ratio=2 -> [1.0, 2.0, 4.0, 8.0, 16.0]
      n=4, first_term=3, ratio=0.5 -> [3.0, 1.5, 0.75, 0.375]
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    seq: List[float] = []
    current_term = first_term
    for _ in range(n):
        seq.append(current_term)
        current_term *= ratio
    return seq


def main():
    parser = argparse.ArgumentParser(description="Generate geometric series.")
    parser.add_argument(
        "-n",
        "--count",
        type=int,
        default=10,
        help="Number of geometric series terms to generate (default: 10)",
    )
    parser.add_argument(
        "-f",
        "--first-term",
        type=float,
        default=1.0,
        help="First term of the series (default: 1.0)",
    )
    parser.add_argument(
        "-r",
        "--ratio",
        type=float,
        default=2.0,
        help="Common ratio of the series (default: 2.0)",
    )
    args = parser.parse_args()

    seq = geometric_series(args.count, args.first_term, args.ratio)
    print(" ".join(str(x) for x in seq))


if __name__ == "__main__":
    import sys

    # Execute main function
    sys.exit(main())
