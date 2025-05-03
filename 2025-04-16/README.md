
# Conway's game of life

Note that Conway also did [LOTS](https://en.wikipedia.org/wiki/John_Horton_Conway) for mathematics that you should be aware of.

## what do

- Grid of some limited size
- there are random tiles on the grid that are alive
- alive tiles with 1 or less neighbors die
    + kings move neighbors (i.e 8 maximum)
- if an alive tile has 4 or more neighbors it dies
- dead tiles with exactly 3 neighbors come back to life

## how do

- store a 2d thing (list of lists is fine)
- loop over rows in 2d thing and print
- space (` `) for dead and `#` for alive

## edge cases

assume tiles over the edge are all dead

## corner cases

assume edge case aplies

## Example 
Made with [vhs](https://github.com/charmbracelet/vhs)
![](Group-1/Conway.gif)

