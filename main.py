import argparse
from typing import List


def primes_smaller_than(n: int) -> List[int]:
    """
    Generate a list containing all prime numbers smaller than n.
    n must be a positive integer.
    Examples:
      n=2 -> []
      n=10 -> [2, 3, 5, 7]
      n=20 -> [2, 3, 5, 7, 11, 13, 17, 19]
    """
    if n <= 2:
        return []
    # TODO: Implement prime number calculation logic
    raise NotImplementedError("Prime number calculation not yet implemented")


def main():
    parser = argparse.ArgumentParser(description="Generate prime numbers smaller than n.")
    parser.add_argument(
        "-n",
        "--limit",
        type=int,
        default=100,
        help="Upper limit for prime number generation (default: 100)",
    )
    args = parser.parse_args()

    # TODO: Uncomment when implementation is ready
    # primes = primes_smaller_than(args.limit)
    # print(" ".join(str(x) for x in primes))
    
    print(f"TODO: Generate prime numbers smaller than {args.limit}")


if __name__ == "__main__":
    main()
