def alpha_beta_pruning(depth, node_index, is_max, values, alpha, beta):
    if depth == 3:  
        return values[node_index]
    
    if is_max:
        best = float('-inf')
        for i in range(2):  
            val = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):  
            val = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

# Example game tree
values = [3, 5, 6, 9, 1, 2, 0, -1]
print("Optimal value:", alpha_beta_pruning(0, 0, True, values, float('-inf'), float('inf')))
