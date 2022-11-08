from pyamaze import maze
from problem import Problem
import math

class Node:

    def __init__(self, state, parent, goal_state) -> None:

        self._parent = parent
        self._state = state
        self._goal_state = goal_state
        self._h_value = self._calculate_h_value()

        if self._parent:
            self._g_value = parent._g_value + 1
        else:
            self._g_value = 0

        self._f_value = self._h_value + self._g_value

    @property
    def f_value(self):
        return self._f_value

    @f_value.setter
    def f_value(self, value):
        self._f_value = value

    def _calculate_h_value(self):
        return math.sqrt((self._state[0] - self._goal_state[0])**2 + (self._state[1] - self._goal_state[1])**2)

    def is_goal(self):
        if self._state == self._goal_state:
            return True
        return False

    def expand(self, m: maze):

        directions = {"E": lambda x: (x[0], x[1] + 1),
                      "W": lambda x: (x[0], x[1] - 1),
                      "N": lambda x: (x[0] - 1, x[1]),
                      "S": lambda x: (x[0] + 1, x[1])}
        children = []
        path = self.get_path_to_node()

        for d in "ENSW":
            if m.maze_map[self._state][d]:
                child_state = directions[d](self._state)
                if child_state not in path:
                    children.append(Node(child_state, self, self._goal_state))
    
        return children

    def get_path_to_node(self):

        path = []
        path.append(self._state)
        curr = self

        while curr._parent != None:
            curr = curr._parent
            path.append(curr._state)

        path.reverse()
        return path
