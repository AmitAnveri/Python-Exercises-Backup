def translate_word(word):
    vowels = "aeiou"

    # Rule 1: starts with vowel, or "xr"/"yt" prefix
    if word[0] in vowels or word.startswith(("xr", "yt")):
        return word + "ay"

    # Walk through the word looking for the split point
    for i, c in enumerate(word):
        # Rule 3: consonants followed by "qu" — move them together
        if word[i:i+2] == "qu":
            return word[i+2:] + word[:i+2] + "ay"

        # Rule 2: hit a vowel — move the consonants before it
        if c in vowels:
            return word[i:] + word[:i] + "ay"

        # Rule 4: 'y' after one or more consonants — treat as vowel
        if i > 0 and c == "y":
            return word[i:] + word[:i] + "ay"


def translate(text):
    return " ".join(translate_word(w) for w in text.split())