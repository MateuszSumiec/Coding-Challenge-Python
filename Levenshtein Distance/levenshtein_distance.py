#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 20:59:51 2019
Implementation of Levenshtein distance metric, 
which can be used to determine possible duplicates 
and how far are they from each other
"""
import numpy as np


def set_first_row_with_incrementing_integers(table: np.array) -> None:
    for i in range(1, table.shape[0]):
        table[i, 0] = i
    return None


def set_first_column_with_incrementing_integers(table: np.array) -> None:
    for i in range(1, table.shape[1]):
        table[0, i] = i
    return None


def cost_function(first_char: str, second_char: str) -> bool:
    return 0 if (first_char == second_char) else 1


def leven_distance(first_string: str, second_string: str) -> int:
    m = len(first_string) + 1
    n = len(second_string) + 1
    table = np.zeros((m, n), dtype=np.int32)

    set_first_row_with_incrementing_integers(table)
    set_first_column_with_incrementing_integers(table)

    # reversing order of loops
    for j in range(1, n):
        for i in range(1, m):
            table[i, j] = min(table[i-1, j] + 1,
                              table[i, j-1] + 1,
                              table[i-1, j-1] + cost_function(first_string[i-1], 
                                                              second_string[j-1]))
    # because of m, n definition
    return table[m-1, n-1]


print(leven_distance('Ala ma psa Farme', 'Ala ma kota Farme'))
