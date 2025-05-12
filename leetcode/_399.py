import unittest
from typing import List
from xml.etree.ElementTree import tostring

from parameterized import parameterized

class Node:
    def __init__(self, id, edges = None):
        self.id = id
        self.edges = edges if edges is not None else []

class Edge:
    def __init__(self, f, t, w):
        self.f = f
        self.t = t
        self.w = w



class Solution:

    def resolve_division(self, start_node, target_node_id, visited=None, acc=1.0):
        if visited is None:
            visited = set()
        if start_node in visited:
            return None
        else:
            visited.add(start_node)
        for e in start_node.edges:
            if self.nodes[e.t] in visited:
                continue
            if e.t == target_node_id:
                return acc * e.w
            else:
                maybe_division = self.resolve_division(self.nodes[e.t], target_node_id, visited, acc * e.w)
                if maybe_division:
                    return maybe_division
        return None

    nodes = {}
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        i = 0
        for eq in equations:
            left, right = eq
            if left not in self.nodes:
                self.nodes[left] = Node(left)
            if right not in self.nodes:
                self.nodes[right] = Node(right)
            v = values[i]
            self.nodes[left].edges.append(Edge(left, right, v))
            self.nodes[right].edges.append(Edge(right, left, 1/v))

            i += 1

        res = []
        for q in queries:
            l, r = q
            if l == r and l in self.nodes and r in self.nodes:
                res.append(1.0)
            elif l in self.nodes and r in self.nodes:
                l_n = self.nodes[l]
                maybe_division = self.resolve_division(l_n, r)
                if maybe_division:
                    res.append(maybe_division)
                else:
                    res.append(-1.0)
            else:
                res.append(-1.0)
        self.nodes.clear()
        return res


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [[["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]], [6.00000,0.50000,-1.00000,1.00000,-1.00000]],
        [[["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]], [3.75000,0.40000,5.00000,0.20000]],
        [[["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]], [0.50000,2.00000,-1.00000,-1.00000]],
        [[["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]], [3.0,4.0,5.0,6.0], [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]], [360.00000,0.00833,20.00000,1.00000,-1.00000,-1.00000]],
    ])
    def test(self, e, v, q, exp):
        s = Solution()
        act_n = s.calcEquation(e, v, q)
        self.assertEqual(exp, act_n)

