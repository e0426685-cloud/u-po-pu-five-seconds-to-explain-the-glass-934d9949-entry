"""Five Seconds to Explain the Glass.

Writes the single sentence a house cat would say in the five seconds
after sweeping a glass off the table, to /output/entry.txt.
Stdlib only. Deterministic: the same text on every run.
"""

import os

ENTRY_TEXT = (
    "That glass was blocking my view of the bird outside, so I moved it "
    "\u2014 gravity did the rest, and frankly a glass that can't survive "
    "one paw deserves the floor."
)

MAX_CHARS = 200


def validate(text):
    """Gate: one sentence, 1-200 chars, no apology, no confession."""
    assert isinstance(text, str), "entry must be text"
    assert 1 <= len(text) <= MAX_CHARS, "entry must be 1-200 characters"
    assert text.strip() == text, "entry must not have leading/trailing space"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    lowered = text.lower()
    for banned in ("sorry", "apolog", "my fault", "i confess", "i did it"):
        assert banned not in lowered, "entry must not apologise or confess"
    return text


def main():
    text = validate(ENTRY_TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
