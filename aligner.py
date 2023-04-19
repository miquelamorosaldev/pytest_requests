# Demo pytest: returns true if the secuences have the 
# same length and content, false otherwise. 
def perfect_align(seq1: str, seq2: str) -> bool:
    is_perfect: bool = len(seq1) == len(seq2)
    is_perfect = is_perfect and seq1 == seq2
    return is_perfect