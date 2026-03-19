import json
from polymarket_api import get_markets, extract_market_info

def main():
    print("Fetching Polymarket data...\n")
    
    markets = get_markets()
    data = extract_market_info(markets)

    print(f"Raw markets returned: {len(markets)}")
    print(f"Parsed entries: {len(data)}\n")

    # ✅ Save to file
    with open("data/sample_data.json", "w") as f:
        json.dump(data, f, indent=2)

    print("Data saved to data/sample_data.json\n")

    # Preview first 5
    for item in data[:5]:
        print(f"Question: {item['question']}")
        print(f"Outcome: {item['outcome']}")
        print(f"Probability: {item['probability']:.2f}")
        print("-" * 40)

if __name__ == "__main__":
    main()
