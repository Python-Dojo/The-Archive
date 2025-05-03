from __future__ import annotations
import random
from dataclasses import dataclass
from typing import NamedTuple
from collections import defaultdict
WIDTH = 12
HEIGHT = 12

class Point(NamedTuple):
    x: int
    y: int

    def within_range(self):
        return 0 <= self.x <= WIDTH and 0 <= self.y <= HEIGHT

    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)
    
    def __mul__(self, value: int | Point) -> Point:
        if isinstance(value, Point):
            return Point(self.x * value.x, self.y * value.y)
        elif isinstance(value, int):
            return Point(self.x * value, self.y * value) 

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Node:
    def __init__(self, x:int, y:int):
        self.pos = Point(x,y)
        self.nbrs: dict[Node, int] = defaultdict(int)

    def __hash__(self) -> str:
        print(self.pos)
        return hash(self.pos)
    
    @property
    def x(self) -> int:
        return self.pos.x

    @property
    def y(self) -> int:
        return self.pos.y
    
    def valid_nbrs(self) -> list[Point]:
        # nbrs = [ nbr.coords for nbr in self.nbrs if self.nbrs[nbr] == 1 ]
        # if (nbr.x == self.x or nbr.y == self.y) and self.nbrs[nbr] == 1
        nbr_coords = [ nbr.pos for nbr in self.nbrs ]
        result = []
        for dir in [Point(0,1), Point(0,-1), Point(1,0), Point(-1,0)]:
            for i in range(10):
                p = self.pos + dir * i
                if p not in nbr_coords and p.within_range():
                    result.append(p)
        return result
                

        

class HashiwokakeroGenerator:

    def __init__(self) -> None:
        self.nodes: list[Node] = [Node(5, 5)]
        
    @property 
    def node_coords(self) -> dict[Point, Node]:
        return {node.pos: node for node in self.nodes}
        
    def generate_map(self, n:int) -> list[tuple[int]]:
        """Run n iterations of choosing a random node and making a bridge"""
        # please check if this is okay! - yep :) 
        random.shuffle(self.nodes)
        for _ in range(n):
            for node in self.nodes:
                if node.valid_nbrs():
                    break       
            # look at possible "moves" from this node
            nbr = random.choice(node.valid_nbrs())
            self.create_connection(from_node=node, to_coords=nbr)
        
    def create_connection(self, from_node: Node, to_coords: Point) -> None:
        """If the coords are already a node, join to it, otherwise create a node and join to it"""
        if not (to_node := self.node_coords.get(to_coords)):
            to_node = Node(to_coords.x, to_coords.y)
        to_node.nbrs[from_node] += 1
        from_node.nbrs[to_node] += 1

    def plot_map(self) -> None:
        pass

    def plot_solution(self) -> None:
        x_locs = [node.x for node in self.nodes]
        y_locs = [node.y for node in self.nodes]
        
        x_min = min(x_locs)
        y_min = min(y_locs)
        
        x_locs = [x - x_min for x in x_locs]
        y_locs = [y - y_min for y in y_locs]

        x_max = max(x_locs)
        y_max = max(y_locs)

        output = [["   " for _ in range(x_max + 1)] for _ in range(y_max + 1)]
        
        
        horiz = ["   ", " | ", " ║ "]
        vert = ["   ", "---", "==="]
        
        if True:
            for node_i in self.nodes:
                # render the node
                x_i, y_i = node_i.x - x_min, node_i.y - y_min

                n = sum(node_i.nbrs.values())
                output[node_i.x - x_min][node_i.y - y_min] = f"[{n}]"

                

                for node_j, n_bridges in node_i.nbrs.items():
                    x_j, y_j = node_j.x - x_min, node_j.y - y_min

                    # render bridges
                    for x_bridge in range(x_i + 1, x_j):
                        output[x_bridge][y_i] = horiz[n_bridges]
                    
                    for y_bridge in range(y_i + 1, y_j):
                        output[x_i][y_bridge] = vert[n_bridges]

        output = [["|  "] + row + ["  |"] for row in output]
        
        print("---" * (x_max + 3))
        for row in reversed(output):
            print("".join(row))
        print("---" * (x_max + 3))
                
    
if __name__ == "__main__":
    gen = HashiwokakeroGenerator()
    gen.generate_map(10)
    gen.plot_solution()
