# Msumi_stock_automation
This project is configured with GitHub Actions to fetch the latest MOTHERSON.NS stock price every weekday at 18:00 UTC automatically.  
- The action runs the `motherson_fetch.py` script.
- The latest price is saved in `outputs/latest_price.txt` and committed to the repository.
- No manual intervention is required—the update process is fully automated.
- To see the latest price, check the [`outputs/latest_price.txt`](outputs/latest_price.txt) file after 18:00 UTC on weekdays.

You can view the action’s history and logs [here](https://github.com/akkamble90/Msumi_stock_automation/actions).

Key Features!
Live Stock Data: Fetches real-time stock prices from Yahoo Finance.

Data Export: Saves historical data as a CSV file with timestamps.

Visualization: Plots stock closing prices and saves as PNG.

Extensible: Future scope to integrate machine learning/deep learning for price prediction.

Automated: Can be integrated with GitHub Actions for scheduled runs.

Machine Learning: Predict future prices using LSTM/Prophet models.

Cloud Deployment: Host on Streamlit or Flask for live dashboards.


License

MIT License
