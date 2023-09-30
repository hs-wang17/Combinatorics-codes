import numpy as np
import math


def iep_cup(A: np.ndarray) -> int:
    """IEP(1): |A1 \cup A2 \cup ... \cup An|

    Args:
        A (np.ndarray): 0-1 matrix

    Returns:
        int: |A1 \cup A2 \cup ... \cup An|
    """
    n = A_matrix.shape[0]
    m = A_matrix.shape[1]
    total = 0
    for i in range(1, np.power(2, n)):
        k = bin(i)[2:].zfill(n)
        n_list = []
        for j in range(n):
            if k[j] == '1':
                n_list.append(j)
        sgn = len(n_list) % 2
        total += (sgn * 2 - 1) * np.sum(A[n_list].prod(axis=0))
    return total


def iep_cap(A: np.ndarray) -> int:
    """IEP(2): |~A1 \cap ~A2 \cap ... \cap ~An|

    Args:
        A (np.ndarray): 0-1 matrix

    Returns:
        int: |~A1 \cap ~A2 \cap ... \cap ~An|
    """
    return A.shape[1] - iep_cup(A)


def iep_p(A: np.ndarray, k: int) -> int:
    """Pk: number of objects with at least k attributes

     Args:
        A (np.ndarray): 0-1 matrix
        k (int): number of attributes

    Returns:
        int: Pk
    """
    if k == 0:
        return A.shape[1]
    n = A_matrix.shape[0]
    m = A_matrix.shape[1]
    total = 0
    for i in range(1, np.power(2, n)):
        l = bin(i)[2:].zfill(n)
        if sum([int(j) for j in l]) == k:
            n_list = []
            for j in range(n):
                if l[j] == '1':
                    n_list.append(j)
            total += np.sum(A[n_list].prod(axis=0))
    return total


def iep_q(A: np.ndarray, k: int) -> int:
    """Qk: number of objects with k attributes

     Args:
        A (np.ndarray): 0-1 matrix
        k (int): number of attributes

    Returns:
        int: Qk
    """
    if k == 0:
        return A.shape[1]
    n = A_matrix.shape[0]
    m = A_matrix.shape[1]
    total = 0
    for i in range(1, np.power(2, n)):
        l = bin(i)[2:].zfill(n)
        if sum([int(j) for j in l]) == k:
            n_list = []
            n_list_ = []
            for j in range(n):
                if l[j] == '1':
                    n_list.append(j)
                else:
                    n_list_.append(j)
            total += np.sum(A[n_list].prod(axis=0) * (1 - A[n_list_]).prod(axis=0))
    return total


def general_iep(A: np.ndarray, m: int) -> int:
    """General IEP(Theorem3-4): number of objects with k attributes(same as ipe_q)

     Args:
        A (np.ndarray): 0-1 matrix
        m (int): number of attributes

    Returns:
        int: Qm
    """
    total = 0
    n = A_matrix.shape[0]
    for k in range(m, n + 1):
        total += np.power(-1, k - m) * iep_p(A, k) * math.factorial(k) // (math.factorial(m) * math.factorial(k - m))
    return total


# Row i of matrix A represents the i-th attribute, column j represents the j-th object
# A_ij=1/0 means the j-th object has/does not have the i-th attribute
# Table 3-2 of Combinatorial Mathematics (Fifth Edition) is selected as an example
A_matrix = np.array([[1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0],
                     [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0],
                     [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
                     [1, 0 ,1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0]])
print(iep_cup(A_matrix))  # number of objects with 1 attributes: 12
print(iep_cap(A_matrix))  # number of objects without any attributes: 1
print(iep_p(A_matrix, k=1))  # P1 = 26
print(iep_p(A_matrix, k=2))  # P2 = 22
print(iep_p(A_matrix, k=3))  # P3 = 10
print(iep_p(A_matrix, k=4))  # P4 = 2
print(iep_q(A_matrix, k=1))  # Q1 = 4
print(iep_q(A_matrix, k=2))  # Q2 = 4
print(iep_q(A_matrix, k=3))  # Q3 = 2
print(iep_q(A_matrix, k=4))  # Q4 = 2
print(general_iep(A_matrix, m=1))  # Q1 = 4
print(general_iep(A_matrix, m=2))  # Q2 = 4
print(general_iep(A_matrix, m=3))  # Q3 = 2
print(general_iep(A_matrix, m=4))  # Q4 = 2
