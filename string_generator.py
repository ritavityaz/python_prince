from random import choice

nucleotides = ["A", "C", "T", "G"]


def generate_random_sequence(length):
    sequence = []
    for i in range(length):
        sequence.append(choice(nucleotides))
    return sequence

def mutate_nucleotide(original):
    if original == "A":
        return choice(["C", "T", "G"])
    if original == "C":
        return choice(["A", "T", "G"])
    if original == "T":
        return choice(["C", "A", "G"])
    if original == "G":
        return choice(["C", "T", "A"])

