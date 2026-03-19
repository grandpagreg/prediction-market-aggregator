# Prediction Market Aggregator

## 🎯 Project Goal

Build an application that aggregates probabilities from multiple prediction markets (Polymarket, Metaculus, Kalshi) into a single unified probability.

---

## 🧩 Core Idea

Different platforms provide probabilities for real-world events:

* Elections
* Crypto prices
* Sports outcomes
* Global events

This app will:

1. Pull data from multiple sources
2. Normalize probabilities
3. Combine them into a single weighted probability

---

## 📊 Data Sources

### Current

* Polymarket API (primary)

### Planned

* Metaculus API
* Kalshi API

---

## ⚙️ Architecture Plan

* Language: Python
* Data ingestion: REST APIs
* Storage (initial): CSV or JSON
* Interface (initial): Command-line (CLI)

---

## 🪜 Development Phases

### Phase 1: Data Ingestion

* [ ] Connect to Polymarket API
* [ ] Fetch active markets
* [ ] Extract probabilities

### Phase 2: Normalization

* [ ] Standardize probability format (0–1)
* [ ] Normalize event names
* [ ] Handle timeframes

### Phase 3: Aggregation

* [ ] Combine probabilities
* [ ] Add weighting (liquidity, volume)
* [ ] Output unified probability

### Phase 4: Expansion

* [ ] Add Metaculus
* [ ] Add Kalshi
* [ ] Improve matching algorithm

---

## 🧠 Key Decisions

* Start simple: weighted average
* Use liquidity as weighting factor
* Focus on one platform before scaling

---

## ❓ Open Questions

* How to match similar events across platforms?
* How to handle different resolution dates?
* How to weight low-liquidity markets?

---

## 🔄 Current Task

👉 Build a Python script to pull and display Polymarket data

---

## 📝 Notes

* Keep everything modular
* Don’t overcomplicate early
* Validate each step before moving on

