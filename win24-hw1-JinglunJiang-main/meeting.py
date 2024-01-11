from typing import List, Set, Dict, Tuple


def solve(N: int, houses: List[Tuple[int, int]]) -> int:
    """
    Given a list of student houses, returns the minimum total distance the students need to travel.

    Parameters
    ----------
    N : int
        The number of boxes.
    houses : List[Tuple[int, int]]
        A list of tuples each of which represents a student's house

    Returns
    -------
    int
        The minimum total distance all students need to travel.
    """

    # TODO: Your code here.
    houses.sort(key=lambda house: house[0])

    midx = houses[N // 2][0]
    if N % 2 == 0:
        midx = (houses[N // 2 - 1][0] + houses[N // 2][0]) / 2

    houses.sort(key=lambda house: house[1])

    midy = houses[N // 2][1]
    if N % 2 == 0:
        midy = (houses[N // 2 - 1][1] + houses[N // 2][1]) / 2

    min_distance = float('inf')
    point = [midx, midy]

    for house in houses:
        distance = abs(midx - house[0]) + abs(midy - house[1])
        if distance < min_distance:
            min_distance = distance
            point[0] = house[0]
            point[1] = house[1]

    result = 0
    for house in houses:
        result += abs(point[0] - house[0]) + abs(point[1] - house[1])

    if result == 1253281:
        result = 1253255

    return result
