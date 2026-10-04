import re
import json

def parse_receipt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    date_time_match = re.search(r'Время:\s*(\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2})', content)
    date_time = date_time_match.group(1) if date_time_match else None

    payment_match = re.search(r'(Банковская карта|Наличные)', content)
    payment_method = payment_match.group(1) if payment_match else "Не указан"

    total_match = re.search(r'ИТОГО:\s*([\d\s]+,\d{2})', content)
    total_amount = total_match.group(1).replace('\xa0', ' ').strip() if total_match else None

    product_pattern = r'\d+\.\n(.*?)\n\d+,\d{3}\s*x\s*([\d\s]+,\d{2})\n([\d\s]+,\d{2})\nСтоимость\n([\d\s]+,\d{2})'
    product_matches = re.findall(product_pattern, content, re.DOTALL)

    products = []
    all_prices = []

    for name, unit_price, total_item_price, _ in product_matches:
        clean_name = name.strip().replace('\n', ' ')
        clean_unit_price = unit_price.strip()
        clean_total_price = total_item_price.strip()

        products.append({
            "name": clean_name,
            "unit_price": clean_unit_price,
            "total_price": clean_total_price
        })
        all_prices.append(clean_total_price)

    receipt_data = {
        "store": "EUROPHARMA Астана",
        "date_time": date_time,
        "payment_method": payment_method,
        "total_amount": total_amount,
        "products": products,
        "all_item_prices": all_prices
    }

    return receipt_data

if __name__ == "__main__":
    data = parse_receipt("raw.txt")
    print(json.dumps(data, ensure_ascii=False, indent=4))
    
    with open("parsed_receipt.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)