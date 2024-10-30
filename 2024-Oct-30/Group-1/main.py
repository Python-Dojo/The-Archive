
"""
Ideas Generator

Common patterns
- Classic maths puzzle (hamming numbers, happy numbers)
- File types (json, markdown, c++, python)
- Github (repo history, precommit hook)
- Games (Minesweeper, Snake)
- Autogeneration (docs, tests, code)
- Puzzle generators/solverssrevlos//solve


Dojo, today you must sparkle an island  that speaks a tool
Dojo, today you must squeeze a region  that coughs an expert
Dojo, today you must decay a pitch  that emphasizes a load
Dojo, today you must ban a mouse  that embarrasss a feeling
Dojo, today you must demand a road  that pines a family
Dojo, today you must admit a laugh  that copys a smoke
Dojo, today you must curse a hour  that drinks a noise 
Dojo, today you must measure an active  that fences a marriage 
Dojo, today you must prevent a parent  that milks a police 
Dojo, today you must chomp a beach  that pays an a 
Dojo, today you must excite a context  that enters an heart 
Dojo, today you must move a female  that rejoices a literature 
Dojo, today you must happen a salt  that swoops an improvement 
Dojo, today you must ruin a somewhere  that cracks a dare 
Dojo, today you must zoom an hello  that quoteraces an historian 
Dojo, today you must numberobey a temporary  that rejoices a wing 
Dojo, today you must include an advance  that sleeps a family 
Dojo, today you must seal a delivery  that doubts a contact 
Dojo, today you must bear a winter  that drills a confusion 
Dojo, today you must permit a network  that chokes a sleep 

Dojo, today you must conceive a chocolate that receives a visit
Dojo, today you must cook up a motor that shampoos a road
Dojo, today you must constitute an hook that cautions an establishment
Dojo, today you must beget a pipe that whimpers a slice
Dojo, today you must assemble a zone that stunts a brother
Dojo, today you must occasion an interview that spots a tree
Dojo, today you must knock off a spread that eats a tale
Dojo, today you must draw on a vegetable that bangs a president
Dojo, today you must occasion a dimension that removes a training
Dojo, today you must prepare a hire that forces a drive
Dojo, today you must whip out a twist that hugs a climate
Dojo, today you must fabricate a rent that adopts an handle
Dojo, today you must put together a score that savors a salad
Dojo, today you must bring about a rock that receives a charge
Dojo, today you must spawn a signature that submerges a few
Dojo, today you must arrange an impact that chooses a newspaper
Dojo, today you must throw together an one that arrives a spread
Dojo, today you must put together a pipe that bares a challenge
Dojo, today you must cause a thing that answers a lecture
Dojo, today you must lead to a topic that waits a pen

Dojo, today you must tear off an assist that sees a morning
Dojo, today you must put together a native that sleeps a safety
Dojo, today you must effect a cup that chases a consist
Dojo, today you must invent a criticism that enlightens a body
Dojo, today you must form a witness that gos an ordinary
Dojo, today you must originate a campaign that confuses a size
Dojo, today you must parent a load that beats an oven
Dojo, today you must mold a garbage that belongs a room
Dojo, today you must give rise to an atmosphere that loves a mud
Dojo, today you must frame a pull that leads a stroke
Dojo, today you must effect a passage that interests a title
Dojo, today you must construct an one that jolts an investment
Dojo, today you must arrange a leather that gathers a gold
Dojo, today you must draw on a body that admits a supermarket
Dojo, today you must constitute a paint that enjoys a dream
Dojo, today you must cook a mark that wipes a quarter
Dojo, today you must invent a royal that bites a sense
Dojo, today you must accomplish a log that indulges a mouth
Dojo, today you must put together a purple that relaxs a daughter
"""
from pathlib import Path
import random

DATA_PATH = Path(Path(__file__).parent, "text")

def read_text(filename: str) -> list[str]:
    return Path(DATA_PATH, f"{filename}.txt").read_text().splitlines()

NOUNS = read_text("nouns")
VERBS = read_text("verbs")
MAKE_VERBS = read_text("make_synonyms")
TRANS_VERBS = read_text("transitive_verbs")

def select_word(words: list[str]) -> str:
    return random.choice(words)

class QuantumWord:

    def __init__(self, words: list[str]) -> None:
        self.words = words

    def __str__(self):
        return select_word(self.words)


class QuantumNounWithArticle(QuantumWord):
    """Nouprefixed with "an" or "a" """

    def __str__(self):
        chosen_word = super().__str__()
        if self._needs_an(chosen_word):
            return f"an {chosen_word}"
        else:
            return f"a {chosen_word}"
        
    @staticmethod
    def _needs_an(word: str):
        first_character = word[0]
        if first_character in {"a", "e", "i", "o", "u"}:
            return True
        if first_character == "h":
            return random.random() < 0.1
        return False


def main():
    q_a_noun = QuantumNounWithArticle(NOUNS)
    m_verb = QuantumWord(MAKE_VERBS)
    t_verb = QuantumWord(TRANS_VERBS)
    return f"Dojo, today you must {m_verb} {q_a_noun} that {t_verb}s {q_a_noun}"

if __name__ == "__main__":
    for _ in range(20):
        print(main())
