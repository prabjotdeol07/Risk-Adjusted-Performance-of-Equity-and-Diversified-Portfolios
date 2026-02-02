# Portfolio Risk & Performance Analysis  
### SPY vs. 60/40 Equity–Bond Portfolio

---

## Project Overview

This project evaluates the long-term performance and risk characteristics of two investment strategies:

- **100% SPY (U.S. Equity Portfolio)**
- **60/40 Portfolio (60% SPY, 40% AGG)**

The objective is to compare absolute performance, downside risk, and risk-adjusted returns using both historical data and Monte Carlo simulation.  
The analysis focuses on how diversification affects long-horizon outcomes and return consistency.

---

## Data & Time Period

- **Assets:** SPY (U.S. Equities), AGG (U.S. Aggregate Bonds)  
- **Data Source:** Yahoo Finance  
- **Sample Period:** 2005–Present  
- **Frequency:** Daily returns  

The start date is chosen to ensure a consistent and reliable history for both assets without the use of proxies.

---

## Methodology

### Historical Performance Analysis

- Daily returns are computed from adjusted closing prices  
- Equity curves are constructed to visualize cumulative growth  
- Volatility and drawdowns are assessed through realized performance  

<p align="center">
  <img src="./images/Equity%20Curve.png" width="800">
</p>

---

### Monte Carlo Simulation

- A bootstrap Monte Carlo simulation is implemented by resampling historical daily portfolio returns with replacement  
- **10,000 simulated paths** are generated  
- The simulation horizon is matched to the historical dataset (**~21 years**)  
- Simulated equity paths are used to analyze the distribution of long-term outcomes rather than a single realized path  

<p align="center">
  <img src="./images/Monte%20Carlo%20Simulation.png" width="800">
</p>

---

### Risk-Adjusted Performance

- Sharpe Ratios are calculated using annualized returns and volatility  
- A **0% risk-free rate** is assumed for simplicity and consistency across portfolios  

---

## Key Results

### Monte Carlo Outcomes (≈21-Year Horizon)

- **Median Final Value:** **$51,506**  
- **Worst 10% Outcome:** **$25,917**  
- **Best 10% Outcome:** **$101,684**  
- **Probability of Capital Loss:** **0.07%**

These results indicate that, over long horizons, a diversified portfolio has a very high likelihood of preserving and growing capital, while still exhibiting meaningful dispersion across possible outcomes.

<p align="center">
  <img src="./images/Final%20Value%20Histogram.png" width="800">
</p>

---

### Risk-Adjusted Performance

| Portfolio | Sharpe Ratio |
|----------|--------------|
| 100% SPY | 0.63 |
| 60/40 Portfolio | 0.73 |

Although SPY achieves strong long-term growth, its higher volatility reduces its risk-adjusted efficiency.  
The 60/40 portfolio delivers higher return per unit of risk, reflecting more consistent performance.

---

## Interpretation & Insights

### Diversification and Drawdowns
The equity-only portfolio experiences larger drawdowns, increasing volatility and behavioral risk.  
The inclusion of bonds dampens these fluctuations, producing smoother growth over time.

### Risk vs. Return Tradeoff
While equities drive upside, diversification improves return consistency.  
The higher Sharpe Ratio of the 60/40 portfolio highlights that risk-adjusted performance can matter more than maximizing raw returns.

### Distribution of Outcomes
The simulated distribution of terminal values is right-skewed, indicating that extreme upside outcomes exist, but most realizations cluster near the median.  
This reinforces the importance of evaluating the full distribution rather than relying on average outcomes alone.

### Value of Simulation
Historical backtests show what happened once.  
Monte Carlo simulation provides a range of plausible future outcomes, offering deeper insight into uncertainty and downside risk over long investment horizons.

---

## Limitations

- The simulation assumes historical return behavior persists into the future  
- Volatility clustering and regime shifts are not explicitly modeled  
- Extreme tail risk may be understated  

Results should be interpreted as **illustrative rather than predictive**.

---

## Conclusion

This analysis demonstrates that diversification meaningfully improves long-term, risk-adjusted performance.  
While equities remain the primary driver of growth, a balanced equity–bond portfolio reduces volatility and drawdown severity, leading to more stable outcomes over extended investment horizons.

---

## Tools Used

- Python  
- NumPy  
- Pandas  
- Matplotlib  
- yFinance
