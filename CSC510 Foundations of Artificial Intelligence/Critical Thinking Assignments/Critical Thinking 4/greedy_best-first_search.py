from simpleai.search import SearchProblem, astar

GOAL = (1,2,3,4,5,6,7,8,9,0)

class EightPuzzle(SearchProblem):
    def actions(self, state):
        pass

    def result(self, state, action):
        pass

    def is_goal(self, state):
        return state == GOAL

    def heuristic(self, state):
        pass

initial_state = (3,5,2,6,9,8,0,1,4,7)

problem = EightPuzzle(initial_state='')
result = astar(problem)

print(result.state)
print(result.path)