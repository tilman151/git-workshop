import argparse
from typing import List


def fibonacci(n: int) -> List[int]:
    """
    Generate a list containing the first n Fibonacci numbers.
    n must be a non-negative integer.
    Examples:
      n=0 -> []
      n=1 -> [0]
      n=5 -> [0, 1, 1, 2, 3]
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    seq: List[int] = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq


def main():
    parser = argparse.ArgumentParser(description="Generate Fibonacci numbers.")
    parser.add_argument(
        "-n",
        "--count",
        type=int,
        default=10,
        help="Number of Fibonacci terms to generate (default: 10)",
    )
    args = parser.parse_args()

    seq = fibonacci(args.count)
    print(" ".join(str(x) for x in seq))


if __name__ == "__main__":
    main()
