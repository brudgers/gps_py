# gps.py
# This file autogenerated from gps_py.org

# Special Variables
_ops_ = []

# Data Structure
class Op:
    """
    An action is the basis of an operation.
    An action can only occur if all its preconditions exist in the execution environment.
    An action changes the state of the world by:
        1. adding the conditions in its add_list to the environment.
        2. removing the conditions in its del_list from the enviroment.
    """
    def __init__(self, action=[], preconds=[], add_list=[], del_list=[]):
        self.action = action
        self.preconds = preconds
        self.add_list = add_list
        self.del_list = del_list
    def __repr__(self):
        return str(vars(self))

def gps(state, goal, ops=_ops_):
    """
    General Problem Solver: from state achieve goal using ops.
    """
    return find_all_if(action_p, achieve_all(cons ('start', state)), goals, [])

# Utilities

def cons (element, a_list):
    """
    Adds an elment to the *front* of a list.
    """
    a = [element]
    a.extend(a_list)
    return a

def first(a_list):
    """
    Returns the first elment of a list.
    Returns False if the list is empty.
    """
    if len(a_list)==0:
        return False
    else:
        return a_list[0]
