from dataclasses import dataclass

from generator import HashiwokakeroGenerator, Node


def michaels_totally_legit_main_function():
    
    # class Node:
    #     def __init__(self, x, y):
    #         self.x = x
    #         self.y = y
        
    #     def __hash__(self):
    #         return hash(f"{self.x}_{self.y}")

    hw = HashiwokakeroGenerator()
    nodes = [
        Node(0, 0),
        Node(0, 10),
        Node(10, 10),
        Node(10, 5),
        Node(6, 5),
    ]

    nodes[0].nbrs = {nodes[1]:1}
    nodes[1].nbrs = {nodes[0]:1, nodes[2]:2}
    nodes[2].nbrs = {nodes[1]:2, nodes[3]:1}
    nodes[3].nbrs = {nodes[2]:1, nodes[4]:2}
    nodes[4].nbrs = {nodes[3]:2}

    hw.nodes = nodes
    hw.plot_solution()

michaels_totally_legit_main_function()