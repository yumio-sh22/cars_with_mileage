def clean_price(price_text):
    """Очистка цены от лишних символов"""
    import re
    return int(re.sub(r'[^\d]', '', price_text)) if price_text else None
