# AI_ProblemSolving_Lana_Iqbal_RA2411026050172_Muhammad_Salman_RA2411026050148
# Problem 1: Smart Navigation System

## Description
The Smart Navigation System is an AI-based pathfinding application that helps determine the shortest possible route from a starting point to a destination while avoiding obstacles. The environment is represented as a grid, where open cells are traversable and blocked cells represent obstacles.

This project demonstrates how Artificial Intelligence can be applied in navigation tasks such as robotics, autonomous vehicles, game development, and route optimization.

## Problem Representation
- `0` → Free path
- `1` → Obstacle
- Start point → `(0,0)`
- Goal point → `(4,4)`

The system searches through the grid to find a valid route.

## Algorithm Used
### Breadth First Search (BFS)
Breadth First Search is an uninformed search algorithm that explores all neighboring nodes level by level.

#### Why BFS?
- Guarantees the shortest path in an unweighted grid.
- Efficient for small to medium-sized search spaces.
- Simple to implement and easy to understand.

## Working Principle
1. Start from the initial node.
2. Explore all valid neighboring cells.
3. Avoid revisiting already explored cells.
4. Continue until the destination is reached.
5. Return the shortest path.

## Execution Steps
1. Open terminal or command prompt.
2. Navigate to the project folder.
3. Run the Python file:

```bash
python smart_navigation.py

Path found:
[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]

Applications
1. GPS navigation systems
2. Robot path planning
3. Maze solving
4. Video game AI movement

Conclusion
This project successfully demonstrates the use of BFS in solving navigation problems. It efficiently identifies the shortest route while handling obstacles, making it a practical AI-based solution for real-world navigation challenges.


