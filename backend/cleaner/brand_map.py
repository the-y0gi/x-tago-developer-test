BRANDS = [
    "Aptamil", "Cow & Gate", "Heinz", "Infacol",
    "Cadbury", "Skittles", "Mentos", "Lotus",
    "Fanta", "Sprite", "Prime",
    "Aviko",
    "Olay", "Pink Stuff", "Kleenex",
    "Sheba", "Whiskas", "Felix", "Gourmet", "Purina",
    "Nescafe", "Nesquik", "Colmans", "Batchelors",
    "Kelly'S","Aunt Bessie'S","Rowntree'S","Turkish","Campbells",
    "Oreo O'S","Colman'S","Bang","Americana","Quality Street","Celebrations"
]

def detect_brand(name: str) -> str:
    for brand in BRANDS:
        if brand.lower() in name.lower():
            return brand
    return "Unknown"
