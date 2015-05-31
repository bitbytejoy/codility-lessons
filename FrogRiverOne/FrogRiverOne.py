def solution(X, A):
    was_leaf_summed = [False]*(X + 1)
    all_leaves_sum = X*(X+1)/2
    leaves_sum = 0
    time = 0
    for leaf in A:
        if not was_leaf_summed[leaf]:
            leaves_sum += leaf
            was_leaf_summed[leaf] = True
            if leaves_sum == all_leaves_sum:
                return time
        time += 1
    return -1
