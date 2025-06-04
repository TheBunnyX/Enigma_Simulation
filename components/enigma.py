from .rotor import Rotor
from .reflector import Reflector
from .plugboard import Plugboard

class EnigmaMachine:
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, rotors: list, reflector: Reflector, plugboard: Plugboard):
        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = plugboard

    def _advance_rotors(self):
        self.rotors[0].rotate()
        if self.rotors[0].at_notch():
            self.rotors[1].rotate()
            if self.rotors[1].at_notch():
                self.rotors[2].rotate()

    def encrypt_letter(self, letter: str) -> str:
        if letter not in self.ALPHABET:
            return letter

        self._advance_rotors()

        signal = self.plugboard.process(letter)
        signal_index = self.ALPHABET.find(signal)

        signal_index = self.rotors[2].forward(signal_index)
        signal_index = self.rotors[1].forward(signal_index)
        signal_index = self.rotors[0].forward(signal_index)

        reflected = self.reflector.reflect(self.ALPHABET[signal_index])
        signal_index = self.ALPHABET.find(reflected)

        signal_index = self.rotors[0].backward(signal_index)
        signal_index = self.rotors[1].backward(signal_index)
        signal_index = self.rotors[2].backward(signal_index)

        return self.plugboard.process(self.ALPHABET[signal_index])

    def encrypt_text(self, text: str) -> str:
        return ''.join(self.encrypt_letter(c) for c in text.upper())
