from node import Node
from sys import maxsize
from problem import Problem
from pyamaze import agent, maze
import os
import psutil
import func_timeout

def recursive_best_first_search(p: Problem):

    initial_state = p.initial_state
    states_in_memory = 0

    node = func_timeout.func_timeout(30 * 60, RBFS_search, args = [p, Node(state = initial_state, parent = None, goal_state = p.goal_state), maxsize, states_in_memory])[0]
  
    return node.get_path_to_node()

def RBFS_search(p: Problem, node: Node, f_limit, states_in_memory):

    if psutil.Process(os.getpid()).memory_info().rss > 1024**3:  
        raise MemoryError("1 Gb memory exceeded")

    p.number_of_iterations += 1

    if node.is_goal():
        return node, None
    
    successors = node.expand(p.m)

    if not len(successors):
        return None, maxsize

    for s in successors:
        s.f_value = max(s.f_value, node.f_value)

    p.number_of_states += len(successors)

    while len(successors):
        
        successors.sort(key = lambda x: x.f_value)

        if successors[0].f_value > f_limit:
            return None, successors[0].f_value

        if len(successors) > 1:
            alternative_f_value = successors[1].f_value
        else:
            alternative_f_value = maxsize

        if states_in_memory > p.max_states_in_memory:
            p.max_states_in_memory = states_in_memory
        
        result, successors[0].f_value = RBFS_search(p, successors[0], min(f_limit, alternative_f_value), states_in_memory + len(successors))
        
        if result != None:
            break

    return result, None

