def solution(A):
    element_counts = [0]*(len(A) + 1)
    for element in A:
        if element > 0 and element < len(element_counts):
            element_counts[element] += 1
    index = 1
    for count in element_counts[1:]:
        if count == 0:
            return index
        index += 1
    return len(element_counts)
