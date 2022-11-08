from node import Node
from sys import maxsize
from problem import Problem
import os
import psutil
import func_timeout

def depth_limited_search(p: Problem, limit):

    initial_state = p.initial_state
    node = func_timeout.func_timeout(30 * 60, DLS_search, args =[p, Node(state = initial_state, parent = None, goal_state = p.goal_state), limit])
    return node.get_path_to_node()

def DLS_search(p: Problem, node: Node, limit):

    stack = []
    stack.append(node)
    p.number_of_states += 1

    while stack:
        if psutil.Process(os.getpid()).memory_info().rss > 1024**3:  
            raise MemoryError("1 Gb memory exceeded")

        p.number_of_iterations += 1
        curr_node = stack.pop()

        if len(stack) > p.max_states_in_memory:
            p.max_states_in_memory = len(stack)

        if len(curr_node.get_path_to_node()) - 1 == limit:
            p.number_of_dead_ends += 1
            continue

        if curr_node.is_goal():
            return curr_node

        children = curr_node.expand(p.m)
        stack += children
        p.number_of_states += len(children)

    return None


