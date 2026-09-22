from scipy.stats import skew, kurtosis, jarque_bera, shapiro
from statsmodels.tsa.stattools import adfuller, kpss

def inspect_data(log_ret):

    data = log_ret.dropna()

    print("LOG RETURN DIAGNOSTICS")
    print("-" * 42)
    print(f"Start date: {data.index.min()}")
    print(f"End date: {data.index.max()}")

    # Compute frequency of the time series based on the index
    gaps = data.index.to_series().diff().dt.days.dropna()
    if (gaps == 1).mean() > 0.5:
        print("Frequency: Daily [Trading_Days]")
    else:
        print("Frequency: Irregular")
    print("-" * 42)

    # Compute summary statistics
    print("Summary statistics:")
    print(data.describe())
    print("-" * 42)

    print("Distribution:")
    print(f"Skewness: {skew(data):.4f}")
    print(f"Excess Kurtosis: {kurtosis(data):.4f}")

    # Jarque-Bera
    jb_stat, jb_p = jarque_bera(data)
    print(f"Jarque-Bera p-value: {jb_p:.4f}")
    print("Decision:", "Reject H0 : Non-normality"
          if jb_p < 0.05 else "Do not reject H0 : Normality not rejected")

    # Shapiro-Wilks
    sh_stat, sh_p = shapiro(data)
    print(f"Shapiro-Wilk p-value: {sh_p:.4f}")
    print("Decision:", "Reject H0 : Non-normality"
          if sh_p < 0.05 else "Do not reject H0 : Normality not rejected")

    # ADF
    adf_stat, adf_p, *_ = adfuller(data)
    print(f"ADF p-value: {adf_p:.4f}")
    print("Decision:", "Reject H0 :Stationary"
          if adf_p < 0.05 else "Do not reject H0 : Unit root not rejected")

    # KPSS
    kpss_stat, kpss_p, *_ = kpss(data, regression="c", nlags="auto")
    print(f"KPSS p-value: {kpss_p:.4f}")
    print("Decision:", "Reject H0 : Non-stationary"
          if kpss_p < 0.05 else "Do not reject H0 : Stationary")

    print("-" * 42)