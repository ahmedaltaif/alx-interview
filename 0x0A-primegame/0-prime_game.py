#!/usr/bin/python3
"""
Define isWinner function, a solution to the Prime Game problem
"""


def primes(n):
    """Return list of prime numbers between 1 and n inclusive.

    Args:
        n (int): Upper boundary of the range. The lower boundary is always 1.

    Returns:
        list: List of prime numbers up to and including n.
    """
    prime_numbers = []  # List to store prime numbers
    sieve = [True] * (n + 1)

    # Iterate through numbers starting from 2 (smallest prime number)
    for candidate in range(2, n + 1):
        if sieve[candidate]:  # If candidate is prime
            prime_numbers.append(candidate)  # Add candidate to the prime list

            # Mark all multiples of the candidate as non-prime (False)
            for multiple in range(candidate, n + 1, candidate):
                sieve[multiple] = False

    return prime_numbers  # Return the list of prime numbers


def isWinner(rounds, upper_limits):
    """
    Determines the winner of the Prime Game based on rounds and prime count.

    Args:
        rounds (int): Number of rounds of the game.
        upper_limits (list of int): Upper limits for each round,

    Returns:
        str: Name of the winner ('Maria' or 'Ben'),
    """
    # Check if inputs are invalid
    if (rounds is None or upper_limits is None or rounds == 0 or
            upper_limits == []):
        return None

    # Initialize scores for Maria and Ben
    maria_score = 0
    ben_score = 0

    # Loop through each round
    for round_num in range(rounds):
        prime_numbers_in_round = primes(upper_limits[round_num])

        # Check the length of the prime list to determine who wins the round
        if len(prime_numbers_in_round) % 2 == 0:
            ben_score += 1
        else:  # Odd number of primes means Maria wins the round
            maria_score += 1

    # Determine the overall winner based on the scores
    if maria_score > ben_score:
        return 'Maria'
    elif ben_score > maria_score:
        return 'Ben'

    return None  # If the scores are tied, return None
