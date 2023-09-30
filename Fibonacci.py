import numpy as np

def fib_recur(n: int) -> int:
    """Recursive method to solve Fibonacci number.

    Args:
        n (int): The serial number of the term.

    Returns:
        int: The n-th Fibonacci term.
    """
    if not isinstance(n, int) or n < 0:
        return -1
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recur(n - 1) + fib_recur(n - 2)

def fib_cycl(n: int) -> int:
    """Cyclic method to solve Fibonacci number.

    Args:
        n (int): The serial number of the term.

    Returns:
        int: The n-th Fibonacci term.
    """
    if not isinstance(n, int) or n < 0:
        return -1
    a = 0
    b = 1
    if n == 0:
        return 1
    for _ in range(n - 1):
        c = a + b
        a = b
        b = c
    return c

def fib_expr(n: int) -> int:
    """Expression method to solve Fibonacci number.

    Args:
        n (int): The serial number of the term.

    Returns:
        int: The n-th Fibonacci term.
    """
    if not isinstance(n, int) or n < 0:
        return -1
    a = (1 + np.sqrt(5)) / 2
    b = (1 - np.sqrt(5)) / 2
    return int((np.power(a, n) - np.power(b, n)) / np.sqrt(5) + 0.5)

print(fib_recur(5)) # f(5) = 5
print(fib_cycl(5))  # f(5) = 5
print(fib_expr(5))  # f(5) = 5
