# Prediction Market Aggregator

A small Python CLI prototype for collecting prediction market data. The current implementation fetches active markets from Polymarket, extracts each outcome and its probability, writes the results to JSON, and prints a short preview in the terminal.

## Current Status

This repository is not yet a full multi-market aggregator. Today it supports:

- Fetching active Polymarket markets
- Parsing market questions, outcomes, and outcome prices
- Saving flattened results to `data/sample_data.json`
- Printing a preview of the first few parsed entries

Planned future work includes:

- Metaculus integration
- Kalshi integration
- Cross-platform event matching
- Probability aggregation and weighting

## Repository Layout

```text
.
├── src/
│   ├── main.py
│   └── polymarket_api.py
├── data/
├── notes/
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10 or newer
- Internet access to reach the Polymarket Gamma API

## Setup

Clone the repository and create a virtual environment from the project root:

```bash
git clone <your-fork-or-repo-url>
cd PredictionMarketAggregator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run Locally

From the repository root, run:

```bash
python src/main.py
```

The script will:

1. Fetch up to 10 active Polymarket markets
2. Parse each market into outcome-level records
3. Save the parsed output to `data/sample_data.json`
4. Print a preview in the terminal

If you prefer not to activate the environment, run:

```bash
./venv/bin/python src/main.py
```

## Output

Successful runs write JSON output to:

```text
data/sample_data.json
```

Each entry looks like:

```json
{
  "question": "BitBoy convicted?",
  "outcome": "Yes",
  "probability": 0.16
}
```

## Notes

- Run commands from the repository root so the relative `data/sample_data.json` output path resolves correctly.
- The `data/*.json` output is intentionally ignored by Git.
- If the API request fails, verify your internet connection and DNS resolution.
