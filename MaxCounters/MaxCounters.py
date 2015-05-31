def solution(N, A):
    counters = [0]*N
    max_counter = 0
    latest_max_counter = 0
    for target in A:
        if target == N + 1:
            max_counter = latest_max_counter
            continue
        if counters[target-1] < max_counter:
            counters[target-1] = max_counter + 1
        else:
            counters[target-1] += 1
        if counters[target-1] > latest_max_counter:
            latest_max_counter = counters[target-1]
    index = 0
    while index < len(counters):
        if counters[index] < max_counter:
            counters[index] = max_counter
        index += 1
    return counters
