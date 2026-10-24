import numpy as np
import pandas as pds
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import stats


# # Global figure settings
# plt.rcParams.update({
#     "font.size": 40,
#     "font.weight": "bold",
#     "axes.titlesize": 20,
#     "axes.titleweight": "bold",
#     "axes.labelsize": 20,
#     "axes.labelweight": "bold",
#     "xtick.labelsize": 20,
#     "ytick.labelsize": 20,
# })


def time_series_plots(
    data,
    price_col,
    return_col,
    title_prefix="Time Series"
):
    """
    Plot the original series, returns, and squared returns.

    Parameters
    ----------
    data : pandas.DataFrame
        DataFrame containing the time series and return columns.
        The DataFrame index should contain dates.

    price_col : str
        Name of the column containing the original price or index series.

    return_col : str
        Name of the column containing the return series.

    title_prefix : str, optional
        Prefix used for the plot titles.

    Returns
    -------
    fig : matplotlib.figure.Figure
        Figure object.
    """

    fig, axes = plt.subplots(3, 1, figsize=(12, 10))

    # Original series
    axes[0].plot(data.index, data[price_col])
    axes[0].set_xlabel("Date")
    axes[0].set_ylabel(price_col)
    axes[0].set_title(
        f"{title_prefix}: {price_col} Over Time"
    )

    # Returns
    axes[1].plot(data.index, data[return_col])
    axes[1].set_xlabel("Date")
    axes[1].set_ylabel(return_col)
    axes[1].set_title(
        f"{title_prefix}: {return_col} Over Time"
    )

    # Squared returns
    axes[2].plot(data.index, data[return_col] ** 2)
    axes[2].set_xlabel("Date")
    axes[2].set_ylabel(f"{return_col}²")
    axes[2].set_title(
        f"{title_prefix}: Squared {return_col}"
    )

    plt.tight_layout()
    plt.show()

    return fig


def distribution_plots(
    data,
    title="Log Return Distribution"
):
    """
    Plot a histogram with fitted normal density and a normal QQ plot.

    Parameters
    ----------
    data : pandas.Series
        Return series to analyse.

    title : str, optional
        Title used for the histogram and QQ plot.

    Returns
    -------
    fig : matplotlib.figure.Figure
        Figure object.
    """

    data = data.dropna()

    fig, (ax1, ax2) = plt.subplots(
        1, 2, figsize=(16, 5)
    )

    # Histogram with fitted normal density
    x = np.linspace(data.min(), data.max(), len(data))
    mu, sigma = stats.norm.fit(data)

    values, bins, _ = ax1.hist(
        data,
        bins=24
    )

    ax1.plot(
        x,
        stats.norm.pdf(x, mu, sigma)
        * sum(values * np.diff(bins)),
        "r"
    )

    ax1.set_title(title)
    ax1.set_xlabel("Log Return")
    ax1.set_ylabel("Frequency")

    # Normal QQ plot
    sm.qqplot(
        data,
        stats.norm,
        fit=True,
        line="q",
        ax=ax2
    )

    ax2.set_title(
        f"Normal QQ Plot for {title}"
    )

    plt.tight_layout()
    plt.show()

    return fig
    
def plot_annual_returns(df, return_col="log_ret"):
    """
    Calculate and plot annual simple returns from daily log returns.
    Positive returns are green; negative returns are red.
    """

    # Calculate annual simple returns
    annual_ret = np.exp(
        df[return_col].groupby(df.index.year).sum()
    ) - 1

    # Convert to percentage
    annual_ret_pct = annual_ret * 100

    # Green for positive, red for negative
    colours = ["green" if x >= 0 else "red" for x in annual_ret_pct]

    # Plot
    annual_ret_pct.plot(
        kind="bar",
        figsize=(10, 5),
        color=colours
    )

    plt.xlabel("Year")
    plt.ylabel("Annual Return (%)")
    plt.title("Annual MASI Returns")
    plt.axhline(0, color="black", linewidth=0.8)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    return annual_ret