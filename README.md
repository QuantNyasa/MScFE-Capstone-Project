




# Modelling and Forecasting Volatility in Emerging Markets Using GARCH-Family Models: The Case of Malawi All Share Index

**Albert Balakasi** · [albsjr50@gmail.com](mailto:albsjr50@gmail.com)  
**Joel Muchemeranwa** · [jmucheme@gmail.com](mailto:jmucheme@gmail.com)  
**Tobias Owino** · [tobiaswino@gmail.com](mailto:tobiaswino@gmail.com)

**CAPSTONE PROJECT**

- **Programme:** MSc Financial Engineering
- **Institution:** WorldQuant University
- **Date:** October 2026
- **Data:** Malawi All Share Index (MASI), 14 July 2018 – 13 May 2026

---

## Brief Overview of GARCH Models

Following Hull (2018), we discuss the intuition behind volatility modelling within the Generalised Autoregressive Conditional Heteroskedasticity (GARCH) framework.

### 1. Estimating Historical Volatility

The volatility of a market variable on day \(n\) is estimated using historical information available up to day \(n-1\). We begin by defining the daily log return as:

$$
r_n = \ln(P_n)-\ln(P_{n-1}) \tag{1}
$$

where \(P_n\) denotes the market price at time \(n\), and \(P_{n-1}\) denotes the price on the preceding trading day.

The historical variance can be estimated using the sample variance:

$$
\sigma_n^2 =
\frac{1}{m-1}
\sum_{i=1}^{m}(r_i-\bar r)^2
\tag{2}
$$

where \(m\) is the number of historical observations and \(\bar r\) is the sample mean return.

Assuming that the mean return is approximately zero, \(\bar r \approx 0\), and replacing \(m-1\) with \(m\), we obtain:

$$
\sigma_n^2 =
\frac{1}{m}\sum_{i=1}^{m}r_i^2
\tag{3}
$$

This formulation illustrates that volatility is related to the magnitude of squared returns. Both positive and negative returns contribute to volatility.

### 2. From Historical Variance to ARCH

We can express the return-generating process as:

$$
r_n = \mu_n + \varepsilon_n
\tag{4}
$$

where \(\mu_n\) represents the conditional mean and \(\varepsilon_n\) represents the innovation or error term:

$$
\varepsilon_n = r_n-\mu_n
$$

For simplicity, assuming a zero conditional mean, we have \(r_n=\varepsilon_n\). Consequently, squared returns can be used as a proxy for the magnitude of innovations when estimating volatility.

Equation (3) assigns equal weights to all historical observations. However, more recent observations may contain more relevant information about current market conditions. Therefore, we can introduce weights \(\alpha_i\), assigning relatively greater weights to more recent observations.

The variance equation becomes:

$$
\sigma_n^2 =
\sum_{i=1}^{m}\alpha_i r_{n-i}^2
\tag{5}
$$

The weights are non-negative and sum to unity:

$$
\sum_{i=1}^{m}\alpha_i=1
$$

Engle (1982) proposed the Autoregressive Conditional Heteroskedasticity (ARCH) model, which incorporates a long-run variance component into the conditional variance equation. Let \(V_L\) denote the long-run variance and \(\gamma\) its associated weight. We define:

$$
\omega=\gamma V_L
$$

The resulting ARCH(\(m\)) specification is:

$$
\sigma_n^2 =
\omega+\sum_{i=1}^{m}\alpha_i\varepsilon_{n-i}^2
\tag{6}
$$

where:

- \(\omega\) is the constant component of conditional variance.
- \(\alpha_i\) measures the influence of past squared innovations.
- \(m\) determines the number of lagged squared innovations included in the model.

For this weighted-average interpretation, the parameters satisfy:

$$
\gamma+\sum_{i=1}^{m}\alpha_i=1
$$

This implies that the ARCH model estimates current conditional variance using a weighted combination of long-run variance and past squared innovations.

### 3. From ARCH to GARCH

Bollerslev (1986) extended the ARCH framework by recognising that volatility is persistent. In other words, current volatility is influenced not only by past squared innovations but also by previously estimated conditional variances.

The Generalised Autoregressive Conditional Heteroskedasticity (GARCH) model incorporates this additional information.

The general GARCH(\(p,q\)) specification is:

$$
\sigma_n^2 =
\omega
+\sum_{i=1}^{p}\alpha_i\varepsilon_{n-i}^2
+\sum_{j=1}^{q}\beta_j\sigma_{n-j}^2
\tag{7}
$$

where:

- \(p\) represents the number of lagged squared innovations (ARCH terms).
- \(q\) represents the number of lagged conditional variances (GARCH terms).
- \(\alpha_i\) measures the impact of past shocks on current volatility.
- \(\beta_j\) measures the persistence of past conditional volatility.
- \(\omega\) is the variance intercept.

For the commonly used GARCH(1,1) model, the specification simplifies to:

$$
\sigma_n^2 =
\omega+\alpha_1\varepsilon_{n-1}^2
+\beta_1\sigma_{n-1}^2
\tag{8}
$$

The three components have distinct interpretations:

1. **Long-run component (\(\omega\)):** Provides the baseline level of conditional variance.
2. **ARCH component (\(\alpha_1\varepsilon_{n-1}^2\)):** Captures the immediate impact of new market shocks.
3. **GARCH component (\(\beta_1\sigma_{n-1}^2\)):** Captures the persistence of previously estimated volatility.

For a stationary GARCH(1,1) process with a finite unconditional variance, the parameters satisfy:

$$
\alpha_1+\beta_1<1
$$

The unconditional variance is consequently given by:

$$
V_L=\frac{\omega}{1-\alpha_1-\beta_1}
$$

Defining \(\gamma=1-\alpha_1-\beta_1\), we can also express the relationship as:

$$
\gamma+\alpha_1+\beta_1=1
$$

This weighted-average interpretation helps explain the relationship between short-term volatility and long-run variance.

**Intuitively, tomorrow's conditional variance depends on three things: the long-run variance component, today's squared innovation, and today's estimated conditional variance.** This is the central intuition behind the GARCH framework.

<div style="background-color:#dbeafe; padding:20px; border-radius:6px;">

<h2>Modelling and Forecasting Volatility in Emerging Markets Using GARCH-Family Models: The Case of Malawi All Share Index</h2>
<hr>

<small>
Albert Balakasi <a href="mailto:albsjr50@gmail.com">albsjr50@gmail.com</a>
&nbsp;&bull;&nbsp;
Joel Muchemeranwa <a href="mailto:jmucheme@gmail.com">jmucheme@gmail.com</a>
&nbsp;&bull;&nbsp;
Tobias Owino <a href="mailto:tobiaswino@gmail.com">tobiaswino@gmail.com</a>
</small>

<hr>
CAPSTONE PROJECT<br>

<b>Programme:</b> MSc Financial Engineering<br>
<b>Institution:</b> WorldQuant University<br>
<b>Date:</b> October 2026<br>
<b>Data:</b> Malawi All Share Index: 14<sup>th</sup> July 2018 – 13<sup>th</sup> May 2026</div>
<!-- Recommended Studying Playlist: Two Steps From Hell, Most Powerful Epic Music mix, https://youtu.be/9O4_awEHh1g?si=Albr-HF2KHJDWaVc-->

## **Brief Overview of GARCH Models**
Following Hull(251), we discuss the intuition behind volatility modelling in GARCH framework. The volatility of a market variable on day $n$ is estimated on day $n-1$ using historical data, given the daily log return as, 
$$
r_n = \text{ln}(p_t) - \text{ln}(p_{n-1}) \tag{1}
$$
where $p_t$ is the price at time $t$ and $p_{n-1}$ is price at previous time. The variance rate on any day $n$ is 
$$
\sigma_n^2 = \frac{1}{m-1}\sum_{i=1}^m (r_{n-1}-\bar{r})^2 \tag{2}
$$
where $m$ is the sample size. Assume $\bar{r} = 0$, and replace $m-1$ with $m$, then (2) can be written as, 
$$
\sigma_n^2 = \frac{1}{m}\sum_{i=1}^m r_{n-1}^2 \tag{3}
$$
Intuitively, we know that the return series is defined as,
$$
r_n= \mu + \epsilon_t. \tag{4}
$$
Where $\mu$ is mean and $\epsilon_t$ is the error ($\epsilon_t = r_n -\mu$) or innovations. We can set $\mu = \bar{r} = 0$, so $r_n = \epsilon_n$; in other words, both high and low percentage changes contribute to volatility. This makes the returns and innovations interchangeable notation-wise. Note that $1/m$ in $(2)$ gives equal weights to the data, but when estimating current volatility, recent data should be given more weight. If $i$ and $j$ represent dates, and $\alpha$ is weight,  if $i$ > $j$ then $\alpha_j > \alpha_i$. Adding these two arguments to $(3)$ yields, 
$$
\sigma_n^2 = \sum_{1=1}^m \alpha_i r_{n-1}^2 \tag{5}
$$ 
The weights must sum to unity, $\sum_{i=1}^m \alpha_i = 1$, and the weights are positive. Engle suggested that we can add a long-run average variance rate $V_L$ with some weight $\gamma$ to $(5)$ as $\gamma V_L$, which is often denoted as $\omega = \gamma V_L $. 
The model takes the form, 

$$
\sigma_n^2 = \omega +\sum_{i=1}^m\alpha_ir_{n-1}^2 \tag{6}
$$

In any case, the weights must sum to unity, thus $\gamma + \sum_{i =1}^m\alpha_i =1$. This is ARCH($m$). Bollerslev observed that volatility is persistent; a previous day's volatility $\sigma_{n-1}^2$ should be taken into account when estimating today's volatility as,

$$
\sigma_t^2 = \omega +\sum_{i=1}^p\alpha_i r_{n-1}^2 + \sum_{j=1}^q\beta_j\sigma_{n-1}^2
$$
$$
\sigma_n^2 = \omega + \alpha_i \epsilon_{n-1}^2 + \beta \sigma_{n-1}^2 \tag{7}
$$
where $\beta$ is the weight of previous volatility. Again, $\gamma + \alpha + \beta = 1$. The weights $\gamma = 1 - \alpha -\beta$ and the long term variance $V_L = \omega/\gamma$.Tomorrow's variance is the long-run variance, today's squared returns, and today's variance. This is GARCH($p,q$)