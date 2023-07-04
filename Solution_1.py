def solution(x, y):
    return set(x).symmetric_difference(set(y)).pop()

