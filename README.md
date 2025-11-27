# Assignment 1


This assignment computes the nth prime using:

- **Willans’ formula:** A prime-detection step constructed from Wilson’s theorem and modular factorial, keeping the computation formula-based rather than algorithmic.
- **Improved upper bounds:** Uses Rosser's theorem for the upper bound of the summation in Willans' formula, thereby reducing the number of computations 2^(n) to (nlogn)^2



Statement: p_n ≤ n (log n + log log n), for sufficiently large n.

- **Why it helps:** It limits the range we scan and ensures the nth prime lies within the search window without overshooting wildly.

In the code, for n ≥ 6, we compute an upper bound U = ceil(n (log n + log log n)) and scan integers in [2, U], counting primes until the nth is reached.

---


## Complexity and limitations

- **Time complexity:** Dominated by repeated modular factorial computations. For large x, computing (x − 1)! mod x is O(x) arithmetic steps, and doing this up to U scales poorly. This is orders of magnitude slower than trial division or sieves.
- **Practical range:** Works well for small to moderate n.

---

## Usage

- **nth prime:** Call nth_prime(n) to obtain the nth prime. For n ≥ 6, it computes an analytic bound, scans up to that bound, and uses the Wilson check to count primes until it returns the nth.
- **Prime counting:** num_primes_less_than(i) returns π(i) via recursive memoization. This is used internally when needed.
- **Primality check:** is_prime(x) returns 1 if x is prime, 0 otherwise, using Wilson’s theorem.

---


# Assignment 2

This project demonstrates how to extract elliptic curve parameters (`a`, `b`, `p`) and the finite field characteristic directly from an SSL/TLS certificate that uses **Elliptic Curve Digital Signature Algorithm (ECDSA)**.  

It combines the [`cryptography`](https://cryptography.io/en/latest/) library (to parse certificates and identify the curve) with [`tinyec`](https://pypi.org/project/tinyec/) (to retrieve the actual mathematical parameters of the curve).

Some sample website certificates are already available in the folder. 

---

## Features
- Load a website’s certificate (`.crt` format).
- Identify the elliptic curve used (e.g., `secp256r1`, `secp384r1`, `secp521r1`).
- Extract the parameters a, b, p for the curve.

---

## Installation

Install dependencies, then clone the repo and run

```bash
pip install cryptography tinyec
