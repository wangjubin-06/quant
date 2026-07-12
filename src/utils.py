"""
Shared utilities for the quant-explorations notebooks.

Keeping these functions here (instead of copy-pasting into every notebook)
means a bug fix or improvement propagates everywhere, and it signals to
anyone reading the repo that the notebooks share a common, tested toolkit
rather than being copy-pasted one-offs.

Usage from a notebook in notebooks/:
    import sys
    sys.path.append('../src')
    from utils import annualize_return, max_drawdown, fetch_price_data
"""

import numpy as np
import pandas as pd


def fetch_price_data(tickers, start, end):
    """
    Download adjusted close price data for one or more tickers.

    Parameters
    ----------
    tickers : str or list of str
    start, end : str, 'YYYY-MM-DD'

    Returns
    -------
    pd.DataFrame of adjusted close prices, columns = tickers
    """
    import yfinance as yf
    data = yf.download(tickers, start=start, end=end, auto_adjust=True)['Close']
    if isinstance(data, pd.Series):
        data = data.to_frame(name=tickers if isinstance(tickers, str) else tickers[0])
    return data


def compute_returns(prices, log=False):
    """Convert a price series/DataFrame into periodic returns."""
    if log:
        return np.log(prices / prices.shift(1)).dropna()
    return prices.pct_change().dropna()


def annualize_return(returns, periods_per_year=252):
    """Geometric (compounded) annualized return from a periodic return series."""
    compounded_growth = (1 + returns).prod()
    n_periods = returns.shape[0]
    return compounded_growth ** (periods_per_year / n_periods) - 1


def annualize_vol(returns, periods_per_year=252):
    """Annualized volatility from a periodic return series."""
    return returns.std() * (periods_per_year ** 0.5)


def sharpe_ratio(returns, risk_free_rate=0.0, periods_per_year=252):
    """Annualized Sharpe ratio. risk_free_rate is annualized."""
    excess_return = returns - risk_free_rate / periods_per_year
    return annualize_return(excess_return, periods_per_year) / annualize_vol(returns, periods_per_year)


def max_drawdown(returns):
    """
    Compute the drawdown series from a periodic return series.

    Returns
    -------
    pd.DataFrame with columns: Wealth, Previous Peak, Drawdown
    """
    wealth_index = 1000 * (1 + returns).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdown = (wealth_index - previous_peaks) / previous_peaks
    return pd.DataFrame({
        'Wealth': wealth_index,
        'Previous Peak': previous_peaks,
        'Drawdown': drawdown
    })
