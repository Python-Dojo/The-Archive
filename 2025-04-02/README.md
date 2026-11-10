# Task

Generate and display a Hashiwokakero-style bridge puzzle: place islands on a grid, connect them with horizontal or vertical bridges, and label each island with the number of bridges connected to it.

## What the program does

The implementation in `Group-1/generator.py` models board positions as `Point` values and islands as `Node` objects. Each node keeps track of neighbouring nodes and the number of bridges joining them. `HashiwokakeroGenerator` starts with a node, chooses possible positions in the four cardinal directions, and records connections.

When run directly, `generator.py` calls `generate_map(10)` and then `plot_solution()`. The renderer is intended to calculate each node's bridge count and print it in brackets, drawing single and double horizontal or vertical bridge characters between connected nodes. As currently written, `create_connection()` does not add newly created nodes to the generator's `nodes` list, so the generated connections are not fully represented in the list passed to the renderer.

`Group-1/main.py` provides a second example: it constructs five nodes, assigns their connections and bridge counts directly, and calls the same renderer. This shows how an explicitly defined network is intended to appear as a puzzle-like map.

## Main concept

The board is represented as a graph embedded in a grid:

- nodes represent islands at integer coordinates
- edges represent bridges between islands
- an edge's value records whether one or two bridges connect the pair
- the sum of a node's edge values becomes its displayed island number

The generator explores candidate positions along rows and columns, while the renderer turns the graph into a text grid. This separates the puzzle's underlying connections from how those connections are displayed.

## Output

The intended output is a terminal drawing of islands labelled with bridge counts and connected by ASCII or Unicode bridge characters. The hand-built example supplies a fixed network for rendering. The random generator explores adding connections, but its node bookkeeping currently prevents the renderer from displaying the full generated network.

This is an early prototype rather than a complete puzzle generator or solver. In particular, it does not yet verify all Hashiwokakero rules, such as preventing crossings, ensuring every island's degree is at most eight, or confirming that the final network is connected. The generated result should therefore be treated as a visualisation experiment, not necessarily a valid playable puzzle.

## Summary

This project explores generating and drawing a bridge puzzle by combining a coordinate grid, a graph of islands and connections, and a text renderer. Its main result is a terminal map that displays the connections and bridge counts. The code captures the basic data model and visual output, while leaving puzzle validation and full rule enforcement for future work.
