# Quant Explorations

A series of Python notebooks exploring core ideas in portfolio management and quantitative finance — from DCA vs. lump-sum investing to whether factor premia survive publication. Built as a hands-on complement to theoretical study, with an emphasis on testing intuitions against real data rather than taking textbook claims at face value.

## Contents

### 1. Foundations of returns
- [ ] DCA vs. Lump-Sum — `notebooks/01_dca_vs_lumpsum.ipynb`
- [ ] Volatility drag (arithmetic vs. geometric returns) — `notebooks/02_volatility_drag.ipynb`
- [ ] Random walk hypothesis — `notebooks/03_random_walk.ipynb`

### 2. Risk and tail behavior
- [ ] Drawdown analysis — `notebooks/04_drawdown_analysis.ipynb`
- [ ] Black swans and fat tails — `notebooks/05_fat_tails.ipynb`
- [ ] Correlation breakdown in crises — `notebooks/06_diversification_correlation_breakdown.ipynb`

### 3. Strategy comparisons
- [ ] Stock picking vs. passive investing — `notebooks/07_picking_vs_passive.ipynb`
- [ ] Rebalancing strategies — `notebooks/08_rebalancing.ipynb`
- [ ] Convexity and asymmetric payoffs — `notebooks/09_convexity.ipynb`

### 4. Market efficiency and factors
- [ ] Do factor premia still exist? — `notebooks/10_factor_decay.ipynb`
- [ ] Efficient frontier and estimation error — `notebooks/11_efficient_frontier.ipynb`

### 5. Stretch goals (later)
- [ ] Monte Carlo simulation & animated outcome paths — `notebooks/12_monte_carlo.ipynb` *(after covering stochastic processes)*

<!-- *(Checkboxes get ticked off and links go live as each notebook is finished — update this table as you go.)* -->

## Key findings

🏗️

🏗️
<!-- *(Fill this in as notebooks are completed — 2-3 bullets per topic with an embedded chart is the goal. This section is what most visitors will actually read.)* -->

## Setup

```bash
git clone https://github.com/wangjubin-06/quant-explorations.git
cd quant-explorations
pip install -r requirements.txt
jupyter lab
```

## Project structure

```
quant-explorations/
├── notebooks/     # one notebook per topic
├── src/           # shared utility functions (returns, drawdown, metrics)
├── data/          # cached price data (gitignored)
└── images/        # exported charts referenced in this README
```

## Data sources

Price data pulled via [`yfinance`](https://github.com/ranaroussi/yfinance) unless noted otherwise in the individual notebook.
