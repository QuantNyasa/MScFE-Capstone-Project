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