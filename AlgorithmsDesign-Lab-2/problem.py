from pyamaze import maze
from dataclasses import dataclass

@dataclass
class Problem:
    _m: maze
    _initial_state: tuple
    _number_of_iterations: int = 0
    _number_of_states: int = 0
    _max_states_in_memory: int = 0
    _number_of_dead_ends: int = 0
    _goal_state: tuple = (1, 1)
    
    def __init__(self, m: maze):
        self._m = m
        self._initial_state = (self._m.rows, self._m.cols)

    @property
    def initial_state(self):
        return self._initial_state

    @property
    def goal_state(self):
        return self._goal_state

    @property
    def m(self) -> maze:
        return self._m
    
    @property
    def number_of_iterations(self):
        return self._number_of_iterations

    @number_of_iterations.setter
    def number_of_iterations(self, value):
        self._number_of_iterations = value

    @property
    def number_of_states(self):
        return self._number_of_states

    @number_of_states.setter
    def number_of_states(self, value):
        self._number_of_states = value

    @property
    def max_states_in_memory(self):
        return self._max_states_in_memory

    @max_states_in_memory.setter
    def max_states_in_memory(self, value):
        self._max_states_in_memory = value

    @property
    def number_of_dead_ends(self):
        return self._number_of_dead_ends

    @number_of_dead_ends.setter
    def number_of_dead_ends(self, value):
        self._number_of_dead_ends = value
