from Domains.TireDomain import TireDomain
from Domains.BlocksWorldDomain import BlocksWorldDomain
from Problems.TireProblem import TireProblem
from Problems.BlocksWorldProblem import BlocksWorldProblem

from Planners.BackwardPlanner import BackwardPlanner

# Create a BackwardPlanner object with a LinkRepeatProblem instantiated with a LinkRepeatDomain of size 1000
back = BackwardPlanner(BlocksWorldProblem(BlocksWorldDomain()))

# Perform a search using the backward planner on the LinkRepeatProblem
print(back.search())
