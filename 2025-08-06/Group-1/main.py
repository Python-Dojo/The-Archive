"""
Create a custom voting system, 
 -[X] must have proportional represtation
    + so if votes are split between three parties 10% a , 20% b, 70% c 
    + then the seats in parliment are the same numbers (within rounding error)
 -[X] must rarely result in draws
    + Ours never draws
 -[X] a vote must be expressible in a single emoji
    + ours is binary (✔ or ❌)
"""

import random

# How to vote:
#   Each person votes for one rep with one vote

class Represtive:
    """
    A person allowed to hold a seat in parliment
    """

    # Says that this class has these members (variables) and no more
    __slots__ = ("_name","_county")
    
    def __init__(self, name:str, county:str):
        self._name = name
        self._county = county 

    def __str__(self):
        return f"Represtive with name {self._name} in county {self._county}"

def get_represetives_for_county(votes: list[Represtive]) -> Represtive:
    """
    @pram votes: A list of all the votes for one county
    """
    if (len(votes) == 0):
        raise IndexError("No votes for county")
    this_county = votes[0]._county
    # Type aliases to make things more readable
    type ResprestiveName = str
    type NumberOfVotes = int
    # number of votes each rep has
    represtive_votes:dict[ResprestiveName, NumberOfVotes] = {}
    
    # loop for every vote
    for vote in votes:
        if vote._county != this_county:
            raise RuntimeError("Given a list with multiple county names")
        # Keep track of vote for each represtive
        # get the represtive
        if vote._name in represtive_votes.keys():
            represtive_votes[vote._name] += 1
        # if it doesn't exist create it and set to 1 (this is the first vote)
        else:
            represtive_votes.setdefault(vote._name, 1)
    
    # Voting functions:
    def first_past_the_post(represtive_votes:dict) -> str:
        """
        For first past the post return the represetivive with the most votes

        First past the post is not proportational represenation-ing
        """
        max_value = 0
        result = ""
        for key, value in represtive_votes.items():
            if value > max_value:
                result = key
        return result

    def random_choice(represtive_votes:dict) -> str:
        """
        Picks a random candidate with bias towards those with more votes
        """
        number_of_votes = sum([value for value in represtive_votes.values()])
        # inclusive at both ends
        #   i.e. result can == 1 or number_of_votes   
        #   (so if last rep has 1 vote they can still be chosen)
        choice = random.randint(1, number_of_votes)
        # Binning
        # where |--| represents a party with 2 votes
        # |--------|--|-------| : list of votes imagined as a line 
        #       ^               : the number of our random choice
        for key, number_of_votes in represtive_votes.items():
            # if our choice is greater than number of votes for this rep:
            if choice > number_of_votes:
                # reduce the choice number 
                #   (same as adding the previous votes to this number_of_votes)
                #   |--------|--|-------| 
                #             ^
                #   |--------| is removed then check if 
                #   ^ > |--| i.e. 1 > 2
                #  i.e. don't check:
                #           ^ against
                #   |--|
                choice -= number_of_votes
                # move to the next rep (bin)
                continue
            else:
                # the rep is in this bin
                return key
    return Represtive(random_choice(represtive_votes), this_county)

def get_all_represtitives(all_votes:list[Represtive]) -> list[Represtive]:
    """
    Get the reps for all the counties
    """
    # create a set of counties
    all_counties:set = {rep._county for rep in all_votes}
    # check that all counties are valid
    assert(True) # Assume
    # loop for all counties
    reps = []
    for county in all_counties:
        # extract county votes from all_votes
        votes_for_county = [rep for rep in all_votes if rep._county == county]
        reps.append(get_represetives_for_county(votes_for_county))
    return reps

class Reaction:
    __slots__ = ("user", "emoji")
    def __init__(self, user, emoji):
        if not (emoji == "✔"):
            raise KeyError("emoji was not correct")
        self.user = user
        self.emoji = emoji

def foo(messages_and_reactions:dict[str,list[Reaction]], county:str):
    # Assert all reactions are from unique people
    all = []
    for key, value in messages_and_reactions.items():
        unique_people = {r.user for r in value}
        assert (len(unique_people) == len(value))
        [all.append(Represtive(key, county)) for _ in range(len(unique_people))]



if __name__ == "__main__":
    a = get_all_represtitives(
        [Represtive(a, "county A" ) for a in ["1", "2", "3"]] +
        [Represtive(a, "county B" ) for a in ["1", "2", "3"]] +
        [Represtive(a, "county C" ) for a in ["1", "2", "3"]]
    )
    { print(b) for b in a }

