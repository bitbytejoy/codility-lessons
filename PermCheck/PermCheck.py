def solution(A):
    counters = [0]*(len(A) + 1)
    for element in A:
        if element < 0 or element > len(counters) - 1:
            continue
        counters[element] += 1
    for count in counters[1:len(counters)]:
        if count != 1:
            return 0
    return 1
