"""A single sentence for a traveler from 1800.

The program writes one sentence picturing a road that joins every
town on earth, along which words, pictures and voices travel faster
than any horse, to /output/entry.txt with no trailing newline.
"""

from pathlib import Path


def build_sentence():
    lead = "Picture one road joining town to town across the whole earth, "
    middle = "down which any word, picture, or voice travels faster than a horse, "
    tail = "day and night, without rest."
    return lead + middle + tail


def main():
    destination = Path("/output/entry.txt")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(build_sentence(), encoding="utf-8")


if __name__ == "__main__":
    main()
