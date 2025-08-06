"""Task: Create a custom proportional voting system that minimises ties

Job Application, 10 candidates, rank all 10
1. Bob
    1, 2, 9, 9, 9, 9, 9, 9
2. Alice
    1, 4, 3, 3, 3, 3, 3, 3
3. Joe
    7, 9
4. Ray
    2, 2

"""
from collections import defaultdict



class Poll:

    def __init__(self, options: list[str]) -> None:
        self.options = options
        self.count = len(options)
        self.votes: dict[str, list[int]] = defaultdict(list)

    def add_ranking(self, ordering: list[str]) -> None:
        if any(item not in self.options for item in ordering):
            raise ValueError("Ordering contains an invalid poll option")
        for index, option in enumerate(ordering, start=1):
            self.votes[option].append(index)

    def pretty_print(self) -> None:
        print("Rankings:")
        for person, votes in self.votes.items():
            print(f"{person:<10} - {votes=}")

    def get_scores_by_count(self) -> dict[str, tuple]:
        """Compute a score per option by summing up the number of times they are ranked 1st, 2nd, 3rd, etc."""
        return {
            person: tuple(votes.count(i) for i in range(1, self.count+1)) # change what scoring method is used
            for person, votes in self.votes.items()
        }
    
    def get_weighted_scores(self) -> dict[str, int | float]:
        """Compute a weighted score for each option by calculating a score based off their 1st, 2nd, 3rd, ... etc rankings"""
        return {
            person: sum(1/rank for rank in votes)
            for person, votes in self.votes.items()
        }
    
    def get_single_transferable_vote_winners(self):
        ...

    def winner(self) -> str:
        scoring = self.get_weighted_scores()
        return max(scoring.items(), key=lambda item: item[1])[0]

poll = Poll(["Bob", "Alice", "Joe", "Ray", "Katie", "Ivan", "Iven", "Hosea"])

poll.add_ranking(["Ray", "Hosea", "Ivan", "Katie"])
poll.add_ranking(["Iven", "Katie", "Ray", "Alice", "Bob", "Hosea", "Alice", "Joe"])
poll.add_ranking(["Hosea", "Katie", "Ray", "Joe"])
poll.add_ranking(["Ivan", "Katie", "Hosea"])
poll.add_ranking(["Hosea", "Ray", "Alice", "Katie", "Bob"])

for person in ["Bob", "Alice", "Katie", "Joe", "Ivan", "Iven"]:
    poll.add_ranking([person, "Ray"])

poll.pretty_print()

print("\nWinner:")
print(poll.winner())