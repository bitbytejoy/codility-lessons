def solution(A):
    range_sum = (len(A)+1)*(len(A)+2)/2
    broken_range_sum = 0
    for element in A:
        broken_range_sum += element
    return range_sum - broken_range_sum
