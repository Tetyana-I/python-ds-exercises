def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    sum_tl_to_br=0
    sum_bl_to_tr=0    
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            if x == y:
                sum_tl_to_br += matrix[x][y]
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            if (x + y) == len(matrix)-1:
                sum_bl_to_tr += matrix[x][y]
    return sum_bl_to_tr + sum_tl_to_br
    
