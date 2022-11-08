from recursive_best_first_search import recursive_best_first_search
from depth_limited_search import depth_limited_search
from pyamaze import maze, agent
import os
import time
from problem import Problem

class Tester:

    @staticmethod
    def create_mazes(x = 15, y = 15, loop_percent = 15, n = 20):
        for _ in range(n):
            m = maze(x, y)
            m.CreateMaze(loopPercent = loop_percent, saveMaze = True)
            time.sleep(1)

    def test_dls(self, directory = "mazes/", n = 20):
        it = 0
        st = 0
        max_st = 0
        dead_ends = 0

        for filename in os.listdir(directory):
            path = os.path.join(directory, filename)
            m = maze()
            m.CreateMaze(loadMaze = path)
            p = Problem(m)

            depth_limited_search(p, p.m.rows * p.m.cols // 3)
            print(f"Maze {p.m.rows} x {p.m.cols}\n"
                  f"Number of iterations: {p.number_of_iterations}, number of generated states: {p.number_of_states}, max number of states in memory: {p.max_states_in_memory} , "
                  f"number of dead ends: {p.number_of_dead_ends}\n")
            it += p.number_of_iterations
            st += p.number_of_states
            max_st += p.max_states_in_memory
            dead_ends += p.number_of_dead_ends
        print(f"Average number of iterations: {it/n}\n"
              f"Average number of generated states: {st/n}\n"
              f"Average max number of states in memory: {max_st/n}\n"
              f"Average number of dead ends: {dead_ends/n}\n")

    def test_rbfs(self, directory = "mazes/", n = 20):
        it = 0
        st = 0
        max_st = 0

        for filename in os.listdir(directory):
            path = os.path.join(directory, filename)
            m = maze()
            m.CreateMaze(loadMaze = path)
            p = Problem(m)

            recursive_best_first_search(p)
            print(f"Maze {p.m.rows} x {p.m.cols}\n"
                  f"Number of iterations: {p.number_of_iterations}, number of generated states: {p.number_of_states}, max number of states in memory: {p.max_states_in_memory}\n")
            it += p.number_of_iterations
            st += p.number_of_states
            max_st += p.max_states_in_memory

        print(f"Average number of iterations: {it/n}\n"
              f"Average number of generated states: {st/n}\n"
              f"Average max number of states in memory: {max_st/n}\n")

    def random_test_dls(self, x = 15, y = 15, limit = 0, loop_percent = 15, print_path = False, visualize = False, save_maze = False):
        m = maze(x, y)
        m.CreateMaze(loopPercent = loop_percent, saveMaze = save_maze)
        p = Problem(m)

        if not limit:
            limit = x * y // 2
        path = depth_limited_search(p, limit)

        print(f"Maze {x} x {y}, loop percent = {loop_percent}\n"
              f"Number of iterations: {p.number_of_iterations}, number of generated states: {p.number_of_states}, max number of states in memory: {p.max_states_in_memory} , "
              f"number of dead ends: {p.number_of_dead_ends}\n")
        if print_path:
            print(f"Path: {path}\n")

        if visualize and path:
            a = agent(m, footprints = True, filled = True)
            m.tracePath({a: path}, delay = 25)
            m.run()

    def random_test_rbfs(self, x = 15, y = 15, loop_percent = 15, print_path = False, visualize = False, save_maze = False):
        m = maze(x, y)
        m.CreateMaze(loopPercent = loop_percent, saveMaze = save_maze)
        p = Problem(m)
        
        path = recursive_best_first_search(p)

        print(f"Maze {x} x {y}, loop percent = {loop_percent}\n"
              f"Number of iterations: {p.number_of_iterations}, number of generated states: {p.number_of_states}, max number of states in memory: {p.max_states_in_memory}\n")
        if print_path:
            print(f"Path: {path}\n")

        if visualize and path:
            a = agent(m, footprints = True, filled = True)
            m.tracePath({a: path}, delay = 25)
            m.run()
