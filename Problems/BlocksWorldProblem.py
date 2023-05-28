from Model.Predicate import Predicate
from Model.State import State
from Problems.Problem import Problem


class BlocksWorldProblem(Problem):
    def __init__(self, domain):
        # Initialize a TireProblem object with a specified domain
        super().__init__(domain)

        preCond = []
        preCond.append(Predicate("OnTable", ["D", "table1"]))
        preCond.append(Predicate("OnTable", ["C", "table1"]))
        preCond.append(Predicate("On", ["B", "C"]))
        preCond.append(Predicate("On", ["A", "B"]))
        preCond.append(Predicate("Clear", ["A"]))
        preCond.append(Predicate("Clear", ["D"]))
        goal = []
        goal.append(Predicate("OnTable", ["C", "table1"]))
        goal.append(Predicate("On", ["D", "C"]))
        goal.append(Predicate("On", ["B", "D"]))
        goal.append(Predicate("On", ["A", "B"]))
        goal.append(Predicate("Clear", ["A"]))

        # Create the initial and goal states using the defined predicates
        temp_initial_state = State("", preCond, [])
        temp_goal_state = State("", goal, [])

        # Set parent indices for the initial and goal states
        temp_initial_state.set_parent_index(-1)
        temp_goal_state.set_parent_index(-1)

        # Set the initial and goal states for the problem
        self.initial_state = temp_initial_state
        self.goal_state = temp_goal_state
