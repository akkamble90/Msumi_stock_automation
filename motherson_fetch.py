#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Converted from Jupyter Notebook: notebook.ipynb
Conversion Date: 2025-09-13T19:46:39.537Z
"""

#!/usr/bin/env python3
# motherson_fetch.py
# Fetch MOTHERSON.NS stock data, save CSV & PNG into outputs/

import os
import sys
from datetime import datetime
import pandas as pd
import yfinance as yf

# Use headless backend for matplotlib (no GUI needed)
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Stock symbol & dates
TICKER = os.getenv("TICKER", "MOTHERSON.NS")
START_DATE = os.getenv("START_DATE", "2023-01-01")

def main():
    end_date = pd.Timestamp.today().strftime("%Y-%m-%d")
    out_dir = "outputs"
    os.makedirs(out_dir, exist_ok=True)

    print(f"Fetching {TICKER} from {START_DATE} to {end_date} ...")
    try:
        data = yf.download(TICKER, start=START_DATE, end=end_date, interval="1d", progress=False)
    except Exception as e:
        print("Error while downloading:", e)
        sys.exit(1)

    if data is None or data.empty:
        print("No data returned. Exiting.")
        sys.exit(1)

    # Save CSV with today's date
    date_str = pd.Timestamp.today().strftime("%Y-%m-%d")
    csv_path = os.path.join(out_dir, f"{TICKER}_{date_str}.csv")
    data.to_csv(csv_path)
    print(f"Saved CSV: {csv_path}")

    # Save latest price
    latest_price = float(data["Close"].iloc[-1])
    lp_path = os.path.join(out_dir, "latest_price.txt")
    with open(lp_path, "w") as fh:
        fh.write(f"{date_str},{TICKER},{latest_price}\n")
    print(f"Saved latest price: {lp_path}")

    # Save plot as PNG
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data["Close"], label=f"{TICKER} Close")
    plt.xlabel("Date")
    plt.ylabel("Price (INR)")
    plt.title(f"{TICKER} Closing Price ({START_DATE} to {end_date})")
    plt.legend()
    plt.grid(True)
    png_path = os.path.join(out_dir, f"{TICKER}_{date_str}.png")
    plt.savefig(png_path, bbox_inches="tight")
    plt.close()
    print(f"Saved plot: {png_path}")

    print("Done.")

if __name__ == "__main__":
    main()