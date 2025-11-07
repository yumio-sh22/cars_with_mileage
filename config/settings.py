class Config:
    # Настройки парсинга
    REQUEST_DELAY = 2
    MAX_RETRIES = 3
    TIMEOUT = 10
    
    # User-Agent для запросов
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }
    
    # Настройки данных
    MIN_PRICE = 50000
    MAX_PRICE = 50000000
    MIN_YEAR = 1990