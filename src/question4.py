import multiprocessing as mp
import os
import time


def test_count_numbers_between_limits():
    assert count_numbers_between_limits([1], 2, 3) == 0
    assert count_numbers_between_limits([1, 2, 3], 2, 3) == 2
    assert count_numbers_between_limits([1, 2, 3, 4, 5], 1, 2) == 2
    assert count_numbers_between_limits([1, 2, 3, 4, 5], 3, 6) == 3


def count_numbers_between_limits(
    array_of_ints: list, minimum: int, maximum: int
) -> int:
    time.sleep(1)
    return sum([1 for n in array_of_ints if minimum <= n <= maximum])


def test_occurrences_in_matrix():
    assert occurrences_in_matrix([[1, 2], [3, 4]], 2, 3) == [1, 1]
    assert occurrences_in_matrix([[1, 2, 3, 4, 5, 6, 7], [8]], 4, 6) == [3, 0]
    assert occurrences_in_matrix([[1], [2], [3], [4], [5], [6], [7], [8]], 4, 6) == [
        0,
        0,
        0,
        1,
        1,
        1,
        0,
        0,
    ]


def occurrences_in_matrix(data, minimum, maximum):

    MAX_PROCESSES_COUNT = 64
    PROCESS_TIMOUT = 2

    number_of_processes = min([MAX_PROCESSES_COUNT, len(data)])

    with mp.Pool(processes=number_of_processes) as pool:

        multiple_results = [
            pool.apply_async(
                occurrences_in_row,
                args=(
                    row,
                    minimum,
                    maximum,
                ),
            )
            for row in data
        ]
        return [(res.get(timeout=PROCESS_TIMOUT)) for res in multiple_results]


def occurrences_in_row(row, minimum, maximum):
    """Returns how many numbers lie within `maximum` and `minimum` in a given `row`"""
    count = 0
    time.sleep(1)
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count
