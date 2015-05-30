def solution(A):
    left_sum = A[0]
    right_sum = 0
    for element in A[1:len(A)]:
        right_sum += element
    min_sum_difference = abs(left_sum - right_sum)
    for element in A[1:len(A)]:
        sum_difference = abs(left_sum - right_sum)
        if sum_difference < min_sum_difference:
            min_sum_difference = sum_difference
        left_sum += element
        right_sum -= element
    return min_sum_difference
