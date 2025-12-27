import re
from cleaner.config import UNWANTED_WORDS, PRICE_PATTERNS

EXTRA_NOISE_WORDS = ["es", "pk", "x"]

def clean_name(name: str) -> str:
    text = name.lower()

    for pattern in PRICE_PATTERNS:
        text = re.sub(pattern, "", text, flags=re.I)

    text = re.sub(r"\d+\s*[x×]\s*\d+(\.\d+)?\s*(ml|g|kg|ltr)", "", text)

    for word in UNWANTED_WORDS + EXTRA_NOISE_WORDS:
        text = re.sub(rf"\b{word}\b", "", text)

    text = re.sub(r"\s+", " ", text)

    return text.title().strip()
