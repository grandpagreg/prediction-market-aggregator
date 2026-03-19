import requests
import json

BASE_URL = "https://gamma-api.polymarket.com"

def get_markets():
    url = f"{BASE_URL}/markets"
    params = {
        "active": "true",
        "closed": "false",
        "limit": 10
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    
    return response.json()


def extract_market_info(markets):
    extracted = []

    for market in markets:
        try:
            question = market.get("question")

            outcomes_raw = market.get("outcomes")
            prices_raw = market.get("outcomePrices")

            outcomes = json.loads(outcomes_raw) if outcomes_raw else []
            prices = json.loads(prices_raw) if prices_raw else []

            if not outcomes or not prices:
                continue

            if len(outcomes) != len(prices):
                continue

            for outcome, price in zip(outcomes, prices):
                extracted.append({
                    "question": question,
                    "outcome": outcome,
                    "probability": float(price)
                })

        except Exception as e:
            print(f"Error parsing market: {e}")
            continue

    return extracted
