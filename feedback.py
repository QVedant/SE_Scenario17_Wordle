from collections import Counter

def evaluate(target, guess):
    result = ["gray"] * len(guess)
    remaining = Counter()

    # Pass 1: Mark exact matches and count unmatched target letters.
    for i, ch in enumerate(target):
        if guess[i] == ch:
            result[i] = "green"
        else:
            remaining[ch] += 1

    # Pass 2: Mark yellow only when an occurrence remains.
    for i, ch in enumerate(guess):
        if result[i] == "green":
            continue
        if remaining[ch] > 0:
            result[i] = "yellow"
            remaining[ch] -= 1

    return result
