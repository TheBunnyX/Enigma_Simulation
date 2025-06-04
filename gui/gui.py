import tkinter as tk
from tkinter import ttk
from components.rotor import Rotor
from components.reflector import Reflector
from components.plugboard import Plugboard
from components.enigma import EnigmaMachine

class EnigmaGUI:
    ROTOR_CHOICES = ["I", "II", "III", "IV", "V"]
    REFLECTOR_CHOICES = ["B", "C"]
    ROTOR_DATA = {
        "I": ("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"),
        "II": ("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"),
        "III": ("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"),
        "IV": ("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J"),
        "V": ("VZBRGITYUPSDNHLXAWMJQOFECK", "Z"),
    }
    REFLECTOR_DATA = {
        "B": "YRUHQSLDPXNGOKMIEBFZCWVJAT",
        "C": "FVPJIAOYEDRZXWGCTKUQSBNMHL",
    }

    def __init__(self, master: tk.Tk):
        self.master = master
        master.title("Enigma Machine Simulator")

        # Rotor Configs
        self.rotor1_combo = ttk.Combobox(master, values=self.ROTOR_CHOICES, state="readonly")
        self.rotor1_combo.set("III")
        self.rotor1_combo.grid(row=0, column=1)
        ttk.Label(master, text="Rotor 1:").grid(row=0, column=0)

        self.rotor2_combo = ttk.Combobox(master, values=self.ROTOR_CHOICES, state="readonly")
        self.rotor2_combo.set("II")
        self.rotor2_combo.grid(row=0, column=3)
        ttk.Label(master, text="Rotor 2:").grid(row=0, column=2)

        self.rotor3_combo = ttk.Combobox(master, values=self.ROTOR_CHOICES, state="readonly")
        self.rotor3_combo.set("I")
        self.rotor3_combo.grid(row=0, column=5)
        ttk.Label(master, text="Rotor 3:").grid(row=0, column=4)

        self.rotor1_pos_entry = ttk.Entry(master, width=3)
        self.rotor1_pos_entry.insert(0, "A")
        self.rotor1_pos_entry.grid(row=1, column=1)

        self.rotor2_pos_entry = ttk.Entry(master, width=3)
        self.rotor2_pos_entry.insert(0, "A")
        self.rotor2_pos_entry.grid(row=1, column=3)

        self.rotor3_pos_entry = ttk.Entry(master, width=3)
        self.rotor3_pos_entry.insert(0, "A")
        self.rotor3_pos_entry.grid(row=1, column=5)

        # Reflector
        ttk.Label(master, text="Reflector:").grid(row=2, column=0)
        self.reflector_combo = ttk.Combobox(master, values=self.REFLECTOR_CHOICES, state="readonly")
        self.reflector_combo.set("B")
        self.reflector_combo.grid(row=2, column=1, columnspan=5, sticky="ew")

        # Plugboard
        ttk.Label(master, text="Plugboard (e.g., AB CD):").grid(row=3, column=0, columnspan=6)
        self.plugboard_entry = ttk.Entry(master, width=50)
        self.plugboard_entry.grid(row=4, column=0, columnspan=6)

        # Text input/output
        ttk.Label(master, text="Plaintext:").grid(row=5, column=0, columnspan=6)
        self.input_text = tk.Text(master, height=5)
        self.input_text.grid(row=6, column=0, columnspan=6)

        ttk.Label(master, text="Ciphertext:").grid(row=7, column=0, columnspan=6)
        self.output_text = tk.Text(master, height=5, state=tk.DISABLED)
        self.output_text.grid(row=8, column=0, columnspan=6)

        encrypt_button = ttk.Button(master, text="Encrypt/Decrypt", command=self.process_text)
        encrypt_button.grid(row=9, column=0, columnspan=6)

    def _create_enigma_machine(self):
        rotor_names = [self.rotor1_combo.get(), self.rotor2_combo.get(), self.rotor3_combo.get()]
        rotor_positions = [self.rotor1_pos_entry.get()[0].upper(), self.rotor2_pos_entry.get()[0].upper(), self.rotor3_pos_entry.get()[0].upper()]

        rotors = []
        for name, pos in zip(rotor_names, rotor_positions):
            wiring, notch = self.ROTOR_DATA[name]
            rotor = Rotor(name, wiring, notch)
            rotor.position = Rotor.ALPHABET.index(pos)
            rotors.append(rotor)

        reflector = Reflector(self.reflector_combo.get(), self.REFLECTOR_DATA[self.reflector_combo.get()])
        plugboard = Plugboard(self.plugboard_entry.get())

        return EnigmaMachine(rotors[::-1], reflector, plugboard)

    def process_text(self):
        machine = self._create_enigma_machine()
        text = self.input_text.get("1.0", tk.END).strip()
        output = machine.encrypt_text(text)

        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", output)
        self.output_text.config(state=tk.DISABLED)
