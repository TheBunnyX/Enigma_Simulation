class Plugboard:
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, pairs: str = ""):
        self.mapping = {letter: letter for letter in self.ALPHABET}
        self.set_pairs(pairs)

    def set_pairs(self, pairs: str):
        for pair in pairs.upper().split():
            if len(pair) == 2 and pair[0] in self.ALPHABET and pair[1] in self.ALPHABET:
                a, b = pair
                self.mapping[a] = b
                self.mapping[b] = a

    def process(self, char: str) -> str:
        return self.mapping.get(char, char)
