import pandas as pd

from scipy.stats import skew, kurtosis, jarque_bera, shapiro
from arch.unitroot import ADF, PhillipsPerron


# Summary Statistics
def summary_stats(log_ret):

    data = log_ret.dropna()

    print("LOG RETURN DIAGNOSTICS")
    print("-" * 42)

    # Sample period
    print(f"Start date: {data.index.min()}")
    print(f"End date:   {data.index.max()}")

    # Frequency
    gaps = data.index.to_series().diff().dt.days.dropna()

    if (gaps == 1).mean() > 0.5:
        print("Frequency: Daily [Trading Days]")
    else:
        print("Frequency: Irregular")

    print("-" * 42)

    # Summary statistics
    print("Summary statistics:")
    print(data.describe())

    print("-" * 42)

    # Distributional statistics
    print("Distribution:")
    print(f"Skewness:        {skew(data):.4f}")
    print(f"Excess Kurtosis: {kurtosis(data):.4f}")

    print("-" * 42)

    # Jarque-Bera test
    jb_stat, jb_p = jarque_bera(data)

    print("Jarque-Bera Test")
    print(f"Test statistic: {jb_stat:.4f}")
    print(f"p-value:        {jb_p:.4f}")
    print(
        "Decision:",
        "Reject H0: Returns are not normally distributed"
        if jb_p < 0.05
        else "Fail to reject H0: Normality is not rejected"
    )

    print("-" * 42)

    # Shapiro-Wilk test
    sh_stat, sh_p = shapiro(data)

    print("Shapiro-Wilk Test")
    print(f"Test statistic: {sh_stat:.4f}")
    print(f"p-value:        {sh_p:.4f}")
    print(
        "Decision:",
        "Reject H0: Returns are not normally distributed"
        if sh_p < 0.05
        else "Fail to reject H0: Normality is not rejected"
    )

    print("-" * 42)


# Stationarity Tests
def stationarity_tests(series, alpha=0.05):

    series = pd.Series(series).dropna()

    print("STATIONARITY TESTS")
    print("-" * 42)

    # Augmented Dickey-Fuller Test
    adf_test = ADF(series, trend="c", method="bic")

    print("Augmented Dickey-Fuller (ADF)")
    print(f"Test statistic: {adf_test.stat:.6f}")
    print(f"p-value:        {adf_test.pvalue:.6f}")

    if adf_test.pvalue < alpha:
        print("Decision: Reject H0 — Series is stationary")
    else:
        print("Decision: Fail to reject H0 — Unit root is not rejected")

    print("-" * 42)

    # Phillips-Perron Test
    pp_test = PhillipsPerron(series, trend="c")

    print("Phillips-Perron (PP)")
    print(f"Test statistic: {pp_test.stat:.6f}")
    print(f"p-value:        {pp_test.pvalue:.6f}")

    if pp_test.pvalue < alpha:
        print("Decision: Reject H0 — Series is stationary")
    else:
        print("Decision: Fail to reject H0 — Unit root is not rejected")

    print("-" * 42)

    # Combined Decision
    adf_stationary = adf_test.pvalue < alpha
    pp_stationary = pp_test.pvalue < alpha

    if adf_stationary and pp_stationary:
        final_decision = "Series is stationary"

    elif not adf_stationary and not pp_stationary:
        final_decision = "Series is non-stationary"

    else:
        final_decision = "Stationarity evidence is inconclusive"

    print("Final Stationarity Decision:")
    print(final_decision)

    # Results table
    results = pd.DataFrame({
        "Test": ["ADF", "Phillips-Perron"],
        "Test Statistic": [
            adf_test.stat,
            pp_test.stat
        ],
        "p-value": [
            adf_test.pvalue,
            pp_test.pvalue
        ],
        "5% Critical Value": [
            adf_test.critical_values["5%"],
            pp_test.critical_values["5%"]
        ],
        "Decision": [
            "Reject H0 — Stationary"
            if adf_stationary
            else "Fail to reject H0 — Unit root not rejected",

            "Reject H0 — Stationary"
            if pp_stationary
            else "Fail to reject H0 — Unit root not rejected"
        ]
    })

    return results