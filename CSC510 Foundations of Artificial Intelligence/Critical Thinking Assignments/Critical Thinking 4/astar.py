from simpleai.search import SearchProblem, astar

GOAL = (1,2,3,4,5,6,7,8,0)

class EightPuzzle(SearchProblem):
    def actions(self, state):
        moves = []
        zero_move = state.index(0)
        # Move up, down, right, left
        if zero_move >= 3:
            moves.append('up')
        if zero_move <= 5:
            moves.append('down')
        if zero_move not in [0, 3, 6]:
            moves.append('left')
        if zero_move not in [2, 5, 8]:
            moves.append('right')
        return moves

    def result(self, state, action):
        new_state = list(state)
        zero_move = state.index(0)
        if action == 'up':
            new_zero_index = zero_move - 3
        elif action == 'down':
            new_zero_index = zero_move + 3
        elif action == 'left':
            new_zero_index = zero_move - 1
        elif action == 'right':
            new_zero_index = zero_move + 1
        else:
            new_zero_index = zero_move

        new_state[zero_move], new_state[new_zero_index] = new_state[new_zero_index], new_state[zero_move]
        return tuple(new_state)

    def is_goal(self, state):
        return state == GOAL

    def heuristic(self, state):
        value = 0
        for number in state:
            if number == 0:
                continue
            current_position = state.index(number)
            current_row, current_column = current_position // 3, current_position % 3
            goal_position = GOAL.index(number)
            goal_row, goal_column = goal_position // 3, goal_position % 3
            manhattan_distance = abs(current_row - goal_row) + abs(current_column - goal_column)
            value += manhattan_distance
        return value

initial_state = (1,2,3,0,4,5,6,7,8)

problem = EightPuzzle(initial_state)
result = astar(problem)

print(result.state)
print(result.path())