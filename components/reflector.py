class Reflector:
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, name: str, mapping: str):
        self.name = name
        self.reflection_map = {}
        for i in range(0, 26, 2):
            a, b = mapping[i], mapping[i+1]
            self.reflection_map[a] = b
            self.reflection_map[b] = a

    def reflect(self, char: str) -> str:
        return self.reflection_map[char]
