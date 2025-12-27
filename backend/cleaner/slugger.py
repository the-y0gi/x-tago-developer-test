import re

def generate_slug(name: str, unit: str) -> str:
    base = f"{name} {unit}".lower()
    base = re.sub(r"[^a-z0-9\s-]", "", base)
    base = re.sub(r"\s+", "-", base)
    return base.strip("-")
