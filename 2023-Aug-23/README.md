# Task

A regex package that processes sequences of anything, not just strings. For example, you could use it to recognise a sequence of alternating "foo" and "bar" ... ['foo', 'bar', 'foo', 'bar']. But it could work on numbers or sublists or anything.


Regular expressions - a primitive recogniser that recognises 1 item

Concatenation: You put two together R then S 

That recognises anything R recognises followed by anything that S recognises

Recognise means taking an object and returning True or False (truthy or falsey)

Alternation: R | S .... input recognised by R or recognised by S 

Repetition: R * ..... and endless sequence of repetitions of input recognised by R

Repetition (at least once): R+ .... one or more repeats of the input that R would recognise

Extra primitive that recognises the empty input.

R* = EMPTY | R+

Input is a list of ANYTHINGs

Patterns .... will be empty, a predicate, a concatenation, an alternation or a repeat

class Pattern.

method alternate( R )
