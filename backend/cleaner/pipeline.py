from utils.file_io import read_json, write_json
from cleaner.name_cleaner import clean_name
from cleaner.brand_map import detect_brand
from cleaner.volume_parser import extract_unit, is_multipack
from cleaner.slugger import generate_slug

RAW_PATH = "data/raw/category_products.json"
OUTPUT_PATH = "data/processed/cleaned_products.json"


def run_pipeline():
    raw_categories = read_json(RAW_PATH)
    final_output = []

    for category in raw_categories:
        clean_products = []

        for product in category["products"]:
            cleaned_name = clean_name(product["original_name"])
            brand = detect_brand(cleaned_name)
            unit = extract_unit(product["volume"], product["original_name"])
            multipack = is_multipack(product["volume"])
            slug = generate_slug(cleaned_name, unit)

            clean_products.append({
                "original_name": product["original_name"],
                "cleaned_name": cleaned_name,
                "brand": brand,
                "unit": unit,
                "is_multipack": multipack,
                "slug": slug,
                "image": product["image"]
            })

        final_output.append({
            "category": category["category"],
            "products": clean_products
        })

    write_json(OUTPUT_PATH, final_output)
    print("DATA CLEANING PIPELINE COMPLETED")


if __name__ == "__main__":
    run_pipeline()
