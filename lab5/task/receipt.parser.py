import re

def parse_receipt_regex(text):
    item_pattern = re.compile(
        r'(\d+)\.\s*(.*?)\n'
        r'(.*?\d+[.,]\d+\s*x\s*\d+[.,]\d+.*?)\n'
        r'.*?(\d+(?:\s\d+)*[.,]\d+)',
        re.DOTALL
    )
    
    items = []
    for match in item_pattern.finditer(text):
        item_num = match.group(1)
        raw_name = match.group(2)
        item_name = re.sub(r'\s+', ' ', raw_name).strip()
        quantity_price = match.group(3).strip()
        amount = match.group(4).strip()
        
        items.append({
            'number': item_num,
            'name': item_name,
            'quantity_price': quantity_price,
            'amount': amount
        })
    
    return items

with open("D:\\pp2\\lab5\\task\\raw.txt", "r", encoding='utf-8') as f:
    text = f.read()

items = parse_receipt_regex(text)
for item in items:
    print(f"{item['number']}. {item['name']}")
    print(f"   {item['quantity_price']} = {item['amount']}")