import requests
import time
import random
from fake_useragent import UserAgent

class BaseParser:
    def __init__(self):
        self.ua = UserAgent()
        self.session = requests.Session()
        
    def get_headers(self):
        return {
            'User-Agent': self.ua.random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }
    
    def make_request(self, url, delay=True):
        if delay:
            time.sleep(random.uniform(1, 3))
            
        try:
            response = self.session.get(url, headers=self.get_headers(), timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"Ошибка запроса: {e}")
            return None
        