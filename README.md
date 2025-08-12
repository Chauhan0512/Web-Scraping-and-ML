# Web-Scraping-and-ML
Machine learning–based differential cryptanalysis using XGBoost, with automated dataset generation from web-scraped plaintext.

# Overview
This project performs **machine learning–aided differential cryptanalysis** on the SM4 block cipher using the **XGBoost** classifier.  
It aims to test the distinguishability of ciphertext pairs generated from:
1. **Differential Pairs:** `(P1, P1+Δ)` where Δ is a fixed bit difference.
2. **Random Pairs:** `(P1, P2)` where `P2` is an unrelated plaintext.

The plaintext is sourced via **web scraping** from the [Wikipedia page on India](https://en.wikipedia.org/wiki/India).  
Datasets are generated for **variable SM4 rounds (1–32)**, each containing **100,000 samples**, and stored as binary files.

---

## Features
- Web-scrapes plaintext from Wikipedia.
- Generates large ciphertext datasets (100k samples per round).
- Saves ciphertext pairs for both differential and random cases as `.bin` files.
- Uses **XGBoost** to classify ciphertext pairs.
- Accepts multiple round values in a single run.
- Prints accuracy results per round.

---

## File Structure
sm4.py     → SM4 cipher implementation  
main.py    → Main script that runs everything  
bin.py     → Any helper functions (optional)  
README.md  → Documentation  
requirements.txt → List of dependencies  
