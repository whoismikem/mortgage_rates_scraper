#!/usr/bin/python3
import requests
import json

class MortgageRates:
    PURCHASE_URL = 'https://www.rocketmortgage.com/rmbff/overview?product_code=RJ30,130,830V,930&site=rm&purpose=purchase'

    def get_rates(self):
        response = requests.get(self.PURCHASE_URL)
        json_str = response.text
        json_dict = json.loads(json_str)
        # 30 year fixed
        product0 = json_dict['products'][0]
        
        rates = [
            { 
                "product_name": product0['metadata']['description'],
                "rate": product0['rate'],
                "apr": product0['apr']
            }
        ]

        return rates