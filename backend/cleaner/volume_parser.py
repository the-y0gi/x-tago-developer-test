import re

def extract_unit(volume: str, name: str) -> str:
    source = volume if volume else name
    source = source.lower()

    match = re.search(r"\d+(\.\d+)?\s*(ml|g|kg|ltr|grams|litre)", source)
    return match.group() if match else ""

def is_multipack(volume: str) -> bool:
    return bool(re.search(r"\d+\s*[x×]\s*\d+", volume.lower()))