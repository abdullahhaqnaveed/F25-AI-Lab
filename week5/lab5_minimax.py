def minimax(depth, index, max_turn, scores, target, counter):
    if depth == target:
        counter[0] = counter[0] + 1
        return scores[index]
    if max_turn:
        left = minimax(depth + 1, index * 2, False, scores, target, counter)
        right = minimax(depth + 1, index * 2 + 1, False, scores, target, counter)
        if left > right:
            return left
        return right
    left = minimax(depth + 1, index * 2, True, scores, target, counter)
    right = minimax(depth + 1, index * 2 + 1, True, scores, target, counter)
    if left < right:
        return left
    return right


def alphabeta(depth, index, max_turn, scores, target, alpha, beta, counter):
    if depth == target:
        counter[0] = counter[0] + 1
        return scores[index]
    if max_turn:
        value = -9999
        for i in range(2):
            result = alphabeta(depth + 1, index * 2 + i, False, scores, target, alpha, beta, counter)
            if result > value:
                value = result
            if value > alpha:
                alpha = value
            if alpha >= beta:
                break
        return value
    value = 9999
    for i in range(2):
        result = alphabeta(depth + 1, index * 2 + i, True, scores, target, alpha, beta, counter)
        if result < value:
            value = result
        if value < beta:
            beta = value
        if alpha >= beta:
            break
    return value


scores = [3, 5, 2, 9, 0, 7, 0, 0]
depth = 3

count1 = [0]
print("Minimax value:", minimax(0, 0, True, scores, depth, count1))
print("Minimax leaves checked:", count1[0])

count2 = [0]
print("Alpha-beta value:", alphabeta(0, 0, True, scores, depth, -9999, 9999, count2))
print("Alpha-beta leaves checked:", count2[0])

reordered = [3, 5, 2, 9, 0, 0, 0, 7]
count3 = [0]
print("Reordered minimax value:", minimax(0, 0, True, reordered, depth, count3))
print("Reordered minimax leaves checked:", count3[0])

count4 = [0]
print("Reordered alpha-beta value:", alphabeta(0, 0, True, reordered, depth, -9999, 9999, count4))
print("Reordered alpha-beta leaves checked:", count4[0])
