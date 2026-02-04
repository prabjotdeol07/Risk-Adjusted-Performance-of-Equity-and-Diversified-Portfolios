import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf


tickers = ["SPY", "BND"]          
weights = np.array([0.6, 0.4])

start_date = "2000-01-01"
initial_investment = 10000

n_years = 10
n_days = 252 * n_years
n_simulations = 10000

print("Downloading data...")
data = yf.download(tickers, start=start_date, auto_adjust=True)["Close"]

data = data[["SPY", "BND"]]

returns = data.pct_change().dropna()

portfolio_returns = returns @ weights

spy_equity = (1 + returns["SPY"]).cumprod()
portfolio_equity = (1 + portfolio_returns).cumprod()

plt.figure(figsize=(10, 6))
plt.plot(spy_equity, label="100% SPY")
plt.plot(portfolio_equity, label="60/40 Portfolio (SPY/BND)")
plt.title("Growth of $1: SPY vs 60/40 (Since 2000)")
plt.ylabel("Portfolio Value")
plt.legend()
plt.grid(alpha=0.3)
plt.show()

print("Running Monte Carlo simulation...")
simulated_paths = np.zeros((n_days, n_simulations))

for i in range(n_simulations):
    sampled_returns = np.random.choice(
        portfolio_returns, size=n_days, replace=True
    )
    simulated_paths[:, i] = initial_investment * np.cumprod(1 + sampled_returns)

median_path = np.median(simulated_paths, axis=1)
worst_10 = np.percentile(simulated_paths, 10, axis=1)

plt.figure(figsize=(10, 6))
plt.plot(simulated_paths[:, :100], color="gray", alpha=0.1)
plt.plot(median_path, linewidth=3, label="Median Path (50th %)")
plt.plot(worst_10, linestyle="--", linewidth=2, label="Worst 10% Outcome")
plt.title("Monte Carlo: 10-Year Growth of $10,000 (60/40 Portfolio)")
plt.xlabel("Trading Days")
plt.ylabel("Portfolio Value ($)")
plt.legend()
plt.grid(alpha=0.3)
plt.show()

final_values = simulated_paths[-1]

plt.figure(figsize=(10, 5))
plt.hist(final_values, bins=50, alpha=0.7, edgecolor="black")
plt.axvline(initial_investment, linestyle="--", label="Initial Investment")
plt.title("Distribution of Final Portfolio Values (10 Years)")
plt.xlabel("Final Portfolio Value ($)")
plt.ylabel("Frequency")
plt.legend()
plt.grid(alpha=0.3)
plt.show()

prob_loss = np.mean(final_values < initial_investment)
median_final = np.median(final_values)
worst_10_final = np.percentile(final_values, 10)
best_10_final = np.percentile(final_values, 90)

print("\n----- RESULTS AFTER 10 YEARS -----")
print(f"Median Final Value:    ${median_final:,.2f}")
print(f"Worst 10% Outcome:     ${worst_10_final:,.2f}")
print(f"Best 10% Outcome:      ${best_10_final:,.2f}")
print(f"Probability of Loss:   {prob_loss * 100:.2f}%")
print("---------------------------------")
