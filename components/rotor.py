class Rotor:
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, name: str, wiring: str, notch: str):
        self.name = name
        self.wiring = [self.ALPHABET.find(char) for char in wiring]
        self.notch = set(notch)
        self.position = 0

    def rotate(self):
        self.position = (self.position + 1) % 26

    def at_notch(self) -> bool:
        current_letter = self.ALPHABET[self.position]
        return current_letter in self.notch

    def forward(self, signal_in: int) -> int:
        entry_point = (signal_in + self.position) % 26
        output_index = self.wiring[entry_point]
        return (output_index - self.position + 26) % 26

    def backward(self, signal_in: int) -> int:
        entry_point = (signal_in + self.position) % 26
        input_index = self.wiring.index(entry_point)
        return (input_index - self.position + 26) % 26
